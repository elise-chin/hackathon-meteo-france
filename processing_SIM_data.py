import pandas as pd

def main():
    # Read the main CSV file
    filename = "raw/SIM/QUOT_SIM2_latest-20240301-20240407.csv"
    df = pd.read_csv(f"data/{filename}", sep=";")

    # Define columns of interest and rename them
    columns_of_interest = {"LAMBX": "e_lambert", "LAMBY": "n_lambert", "DATE": "date", "T_Q": "daily_average_temperature", "TINF_H_Q" : "daily_max_temperature", "TSUP_H_Q" : "daily_min_temperature"}
    filtered_df = df[columns_of_interest.keys()].rename(columns=columns_of_interest)

    # Read the coordinates CSV file
    filename_coordonnees = "raw/SIM/coordonnees_grille_safran_lambert-2-etendu.csv"
    df_coordonnees = pd.read_csv(f"data/{filename_coordonnees}", sep=";")

    # Rename coordinate columns
    rename_columns_coordonnees = {"LAMBX (hm)" : "e_lambert", "LAMBY (hm)" : "n_lambert"}
    df_coordonnees = df_coordonnees.rename(columns = rename_columns_coordonnees)

    # Merge the main DataFrame with the coordinates DataFrame based on Lambert coordinates
    merged_df = pd.merge(filtered_df, df_coordonnees, on=["e_lambert", "n_lambert"], how="left")

    # Reorder columns
    cols = list(merged_df.columns)
    cols = cols[-2:] + cols[:-2]
    merged_df = merged_df[cols]

    # Replace commas with periods in LAT_DG and LON_DG columns
    merged_df['LAT_DG'] = merged_df['LAT_DG'].str.replace(',', '.')
    merged_df['LON_DG'] = merged_df['LON_DG'].str.replace(',', '.')

    # Define columns of interest for the final DataFrame
    columns_of_interest2 = ["LAT_DG", "LON_DG", "date", "daily_average_temperature", "daily_max_temperature", "daily_min_temperature"]

    # Filter the final DataFrame based on columns of interest
    merged_df = merged_df[columns_of_interest2]

    # Define Île-de-France coordinates intervals
    LAT_DG_interval = [48.111728, 49.405512]
    LONG_DG_interval = [1.368147, 3.587385]

    # Filter DataFrame based on latitude and longitude intervals
    filtered_df = merged_df[
        (merged_df['LAT_DG'].astype(float) >= LAT_DG_interval[0]) & 
        (merged_df['LAT_DG'].astype(float) <= LAT_DG_interval[1]) &
        (merged_df['LON_DG'].astype(float) >= LONG_DG_interval[0]) & 
        (merged_df['LON_DG'].astype(float) <= LONG_DG_interval[1])
    ]


    # Save the SIM file
    filtered_df.to_csv(f"data/processed/SIM_IDF.csv", sep=";", index=False)

    colmuns_of_interset_projection = ["LAT_DG", "LON_DG"]


    filtered_df_projection = filtered_df[colmuns_of_interset_projection]

    filtered_df_projection = filtered_df_projection.drop_duplicates(subset=['LAT_DG', 'LON_DG'], keep='first')

    filtered_df_projection['ID'] = range(1, len(filtered_df_projection) + 1)

    # Insert the 'ID' column as the first column
    filtered_df_projection.insert(0, 'ID', filtered_df_projection.pop('ID'))

    # Save the SIM file
    filtered_df_projection.to_csv(f"data/processed/SIM_IDF_for_projection.csv", sep=";", index=False)

if __name__ == "__main__":
    main()