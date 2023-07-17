# below is a python code for comparison of two codelists in CSV format. 
# using CODEBROWSER save your code list as text file, open in excel and save as a CSV file after changing the SNOMED coloumn to a 'Id' and the descriptive terms file to 'term' (lowercase)
# now you can run the code after swapping out the file paths to where you desire
# you may have to edit the comaprison file columns to 'Id' and 'term' depending where you sourced it from
# the output_id file is the most useful in my work. 

import pandas as pd

def compare_csv_files(file1, file2, output_file_id, output_file_term):
    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Compare the 'Id' column
    unique_ids = set(df1['Id']).symmetric_difference(set(df2['Id']))
    output_data_id = pd.DataFrame({'Id': list(unique_ids)})
    output_data_id['Source File'] = output_data_id['Id'].apply(lambda x: file1 if x in set(df1['Id']) else file2)
    output_data_id = output_data_id.merge(df1, on='Id', how='left').merge(df2, on='Id', how='left', suffixes=('_file1', '_file2'))
    output_data_id.to_csv(output_file_id, index=False)

    # Compare the 'term' column
    unique_terms = set(df1['term']).symmetric_difference(set(df2['term']))
    output_data_term = pd.DataFrame({'term': list(unique_terms)})
    output_data_term['Source File'] = output_data_term['term'].apply(lambda x: file1 if x in set(df1['term']) else file2)
    output_data_term = output_data_term.merge(df1, on='term', how='left').merge(df2, on='term', how='left', suffixes=('_file1', '_file2'))
    output_data_term.to_csv(output_file_term, index=False)

# Specify the file paths
file1_path = r'COMPARISON FILE URL PATH'
file2_path = r'CODELIST FILE URL PATH'
output_file_path_id = r'WHERE YOU WANT THE FILE SAVED AND FILE NAME , E.G. BELOW'
output_file_path_term = r'C:\Users\.....\CODELISTS\output_term.csv'

# Compare the CSV files and generate the output files
compare_csv_files(file1_path, file2_path, output_file_path_id, output_file_path_term)

