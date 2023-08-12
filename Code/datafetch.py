import pandas as pd
import os

def data_fetch(input_file_path, csv_file):
    data = [] 
    line_num=0; 

    try:
        with open(input_file_path, "r") as input_file:
            for line in input_file:
                if len(line.strip()) == 0 or line[0] in ('@', '%', ' '):
                    continue

                line_num+=1
                elements = line.strip().split(',')  # Split line into elements
                target = elements[-1]
                elements.pop();

                for day, element in enumerate(elements):
                    data.append((line_num,day,element,target));

        # Create a DataFrame from the collected data
        df = pd.DataFrame(data, columns=['company', 'day', 'pricechange','target'])
        print(df.head(4));

        # Save DataFrame to a CSV file
        csv_filename = csv_file
        
        df.to_csv(csv_filename, index=False)  # Set index=False to exclude index column
        print(f"DataFrame saved as '{csv_filename}'.")
        
    except FileNotFoundError:
        print(f"File '{input_file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


train_file_path = "./SharePriceIncrease_TRAIN.arff"
train_data='train_data.csv'
data_fetch(train_file_path, train_data);

test_file_path = "./SharePriceIncrease_TEST.arff"
test_data='test_data.csv'
data_fetch(test_file_path, test_data);