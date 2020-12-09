import pandas as pd


total_time_file = pd.read_csv('total_time_test_no10.csv')
laughing_time_file = pd.read_csv('laughing_time_test_no10.csv')
print(total_time_file)
print(laughing_time_file)
merged = total_time_file.merge(laughing_time_file)
print(merged)
merged.to_csv('final_test.csv', index=False)