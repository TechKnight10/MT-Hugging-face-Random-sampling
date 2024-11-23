import random
from datasets import load_dataset
import pandas as pd


dataset = load_dataset("csebuetnlp/xlsum", "gujarati", split="test")


random_indices = random.sample(range(len(dataset)), 150)


sampled_data = dataset.select(random_indices)


data = []
for article in sampled_data:
    data.append({
        'URL Source': article['url'], 
        'Article': article['text'],   
        'Summary': article['summary']  
    })


df = pd.DataFrame(data)


csv_file = "urls_and_articles_summary_gujarati.csv"
df.to_csv(csv_file, index=False, encoding='utf-8-sig')  

print(f"CSV file saved: {csv_file}")