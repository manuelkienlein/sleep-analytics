import os
import pandas as pd

def concatenate_csv_files(directory, output_file):
    # Get a list of all CSV files in the directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

    # Check if there are any CSV files
    if not csv_files:
        print("No CSV files found in the directory.")
        return

    # Initialize an empty DataFrame to store concatenated data
    concatenated_data = pd.DataFrame()

    # Concatenate data from all CSV files
    for csv_file in csv_files:
        file_path = os.path.join(directory, csv_file)
        df = pd.read_csv(file_path)
        concatenated_data = pd.concat([concatenated_data, df], ignore_index=True)

    # Write the concatenated data to the output file
    concatenated_data.to_csv(output_file, index=False)
    print(f"Concatenated data written to {output_file}")

# Example usage:
input_directory = './data/P12/supersapiens/'
output_csv = './data/P12/supersapiens/merged.csv'

concatenate_csv_files(input_directory, output_csv)