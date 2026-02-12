from datasets import load_dataset
from pprint import pprint

dataset = load_dataset("klue", "ynat")

# print(dataset)


# pprint(dataset)
raw_train_dataset = dataset["train"]
# pprint(raw_train_dataset[0])

# print('----' * 30)

# print(raw_train_dataset)

import pandas as pd

df = pd.DataFrame(dataset['train'])
print(df[['title', 'label']].head())