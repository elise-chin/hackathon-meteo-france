import pandas as pd

def main():
    list_df = []

    # Define the specific values for iteration
    values = [75, 92, 93, 94]

    # Loop over the specified values
    for i in values:
        # Construct the filename based on the current value of i
        filename = f"raw/base/Q_{i}_latest-2023-2024_RR-T-Vent.csv"
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(f"data/{filename}", sep=";")
        
        # Define columns of interest and rename them
        columns_of_interest = {"LAT" : "LAT_DG", "LON" : "LON_DG", "AAAAMMJJ" : "date", "TM" : "daily_average_temperature", "TX" : "daily_max_temperature", "TN" : "daily_min_temperature"}
        df = df[columns_of_interest.keys()].rename(columns=columns_of_interest)
        
        # Append the DataFrame to the list
        list_df.append(df)

    
    # Concatenate all DataFrames in list_df
    concatenated_df = pd.concat(list_df, ignore_index=True)

    # Save the SIM file
    concatenated_df.to_csv(f"data/processed/Base_IDF.csv", sep=";", index=False)

    colmuns_of_interset_projection = ["LAT_DG", "LON_DG"]
    concatenated_df_projection = concatenated_df[colmuns_of_interset_projection]

    concatenated_df_projection = concatenated_df_projection.drop_duplicates(subset=['LAT_DG', 'LON_DG'], keep='first')

    concatenated_df_projection['ID'] = range(1, len(concatenated_df_projection) + 1)

    # Insert the 'ID' column as the first column
    concatenated_df_projection.insert(0, 'ID', concatenated_df_projection.pop('ID'))


    # Save the SIM file
    concatenated_df_projection.to_csv(f"data/processed/Base_IDF_for_projection.csv", sep=";", index=False)

if __name__ == "__main__":
    main()