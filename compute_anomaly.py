import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()


def min_max_standardization(x):
    return (x - x.min()) / (x.max() - x.min())

def compute_num_anomaly(df, id_df, icu_df):
    df = df.merge(id_df, on=["LAT_DG", "LON_DG"], how="left").merge(icu_df, on="ID", how="left").assign(standardized_temperature=lambda df: df.groupby('date')['daily_average_temperature'].transform(min_max_standardization), is_hot=lambda df: np.where(df["standardized_temperature"] > 0.5, 1, 0)).fillna(0)

    num_anomaly = []
    num_days = []
    for id in df["ID"].unique():
        info = df.loc[lambda df: df["ID"] == id]["is_hot"].value_counts()
        if (icu_df.loc[lambda df: df["ID"] == id]["nbICU"].reset_index(drop=True)[0] < 10) and (1 in info.keys()):
            num_anomaly.append(df.loc[lambda df: df["ID"] == id]["is_hot"].value_counts()[1])
        elif (icu_df.loc[lambda df: df["ID"] == id]["nbICU"].reset_index(drop=True)[0] >= 10) and (0 in info.keys()):
            num_anomaly.append(df.loc[lambda df: df["ID"] == id]["is_hot"].value_counts()[0])
        else:
            num_anomaly.append(0)
        num_days.append(df.loc[lambda df: df["ID"] == id].shape[0])

    result_df = pd.DataFrame({"ID": df["ID"].unique(), "num_anomaly": num_anomaly, "num_days": num_days}).assign(percent_num_anomaly=lambda df: df["num_anomaly"]/df["num_days"] * 100)

    return result_df

def plot(result_df):
    station_ids = result_df['ID']
    pourcentage_anomalie = result_df['percent_num_anomaly']

    plt.figure(figsize=(10, 6))
    plt.bar(station_ids, pourcentage_anomalie)

    plt.title('Histogramme des pourcentages d\'anomalie par station')
    plt.xlabel('Station ID')
    plt.ylabel('Pourcentage d\'anomalie')

    plt.show()

if __name__ == "__main__":
    data_folder = "data/processed/"
    base_df = pd.read_csv(data_folder + "Base_IDF.csv", sep=";")
    sim_df = pd.read_csv(data_folder + "SIM_IDF.csv", sep=";")

    base_id_df = pd.read_csv(data_folder + "Base_IDF_for_projection.csv", sep=";")
    sim_id_df = pd.read_csv(data_folder + "SIM_IDF_for_projection.csv", sep=";")

    base_icu_df = pd.read_csv(data_folder + "base_nbICU.csv")
    sim_icu_df = pd.read_csv(data_folder + "sim_nbICU.csv")

    base_result_df = compute_num_anomaly(base_df, base_id_df, base_icu_df)
    sim_result_df = compute_num_anomaly(sim_df, sim_id_df, sim_icu_df)

    plot(base_result_df)
    plot(sim_result_df)