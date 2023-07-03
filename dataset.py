from datasets import load_dataset

## loading text dataset
dataset = load_dataset('text', data_files={'train': ['my_train.txt'], 'test': 'my_test.txt'})
print(dataset['test'][0])

## loading json dataset
dataset = load_dataset('json', data_files={'train': ['my_train_json.json'], 'test': 'my_train_json.json'})
