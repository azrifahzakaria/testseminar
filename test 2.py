import pandas as pd

# Read the first CSV file
df1 = pd.read_csv('/Users/sundaramrajashree/PycharmProjects/Webscraping/tagger1_counts/aggregated_tagger1_counts.csv')

# Read the second CSV file
df2 = pd.read_csv('/Users/sundaramrajashree/PycharmProjects/Webscraping/output_folder/total_words_summary.csv')

# Extract relevant columns from the first file
columns_to_match = df1.columns[1:]

# Initialize the output dataframe
result_df = pd.DataFrame(columns=['Filename'] + list(columns_to_match))

# Strip extra words from 'Filename' column in df1
df1['Filename'] = df1['Filename'].str.replace('_pos_tagged$', '', regex=True)

# Iterate through rows in the second file
for index, row in df2.iterrows():
    filename = row['Filename']
    total_words = row['Total Words']