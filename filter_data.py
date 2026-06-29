import pandas as pd

INPUT_FILES = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
OUTPUT_FILE = 'data/filtered_sales_data.csv'

def filter_data(input_files, output_file):

    data = []

    for file in input_files:
        df = pd.read_csv(file)
        filtered_df = df[df['product'] == 'pink morsel'].copy()
        filtered_df.loc[:, 'sales'] = filtered_df['price'].str.replace('$', '', regex=False).astype(float) * filtered_df['quantity']
        data.append(filtered_df[['sales', 'date', 'region']])

    filtered_data = pd.concat(data, ignore_index=True).sort_values(by='region', ascending=True)
    filtered_data.to_csv(output_file, index=False)

if __name__ == '__main__':
    filter_data(INPUT_FILES, OUTPUT_FILE)