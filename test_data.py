from datasets import load_dataset
import os

base_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_path, "sample_data", "sample.csv")

ratio = 80
dataset = load_dataset(
  path="csv",
  data_files=csv_path,
  split={
    "train": f"train[:{ratio}%]",
    "test": f"train[{ratio}%:]"
  }
)

print(dataset)