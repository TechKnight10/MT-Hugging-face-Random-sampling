import random
from datasets import load_dataset
import openpyxl

dataset = load_dataset("csebuetnlp/xlsum", "punjabi", split="test")

random_indices = random.sample(range(len(dataset)), 150)

sampled_data = dataset.select(random_indices)

for i, article in enumerate(sampled_data):
    print(f"Article {i+1} ID: {article['id']}, URL: {article['url']}")


output_file = "urls_and_ids punjabi.txt"
with open(output_file, "w") as file:
    for article in sampled_data:
        file.write(f"ID: {article['id']}, URL: {article['url']}\n")
excel_file = "urls_and_ids punjabi.xlsx"
wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = f'=HYPERLINK("{output_file}", "Click here for URLs and IDs for punjabi")'

wb.save(excel_file)
print(f"Excel file saved: {excel_file}")