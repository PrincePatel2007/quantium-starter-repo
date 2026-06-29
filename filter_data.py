import pandas as pd

INPUT_FILES = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
OUTPUT_FILE = 'data/filtered_sales_data.csv'

def filter_data(input_files, output_file):
    filtered_data = pd.DataFrame()

    for file in input_files:
        df = pd.read_csv(file)
        filtered_df = df[df['product'] == 'pink morsel']
        filtered_df = filtered_df.copy()
        filtered_df['sales'] = filtered_df['price'].str.replace('$', '', regex=False).astype(float) * filtered_df['quantity']
        filtered_data = pd.concat([filtered_data, filtered_df], ignore_index=True)
        filtered_data = filtered_data[['sales', 'date', 'region']].sort_values('region', ascending=True)

    filtered_data.to_csv(output_file, index=False)

if __name__ == '__main__':
    filter_data(INPUT_FILES, OUTPUT_FILE)