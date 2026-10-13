import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

api = KaggleApi()
api.authenticate()

def download_kaggle_dataset(dataset_name, download_path):
    """
    Downloads a dataset from Kaggle.

    Parameters:
    dataset_name (str): The name of the dataset in the format 'username/dataset-name'.
    download_path (str): The local path where the dataset will be downloaded.
    """
    # Ensure the download path exists
    os.makedirs(download_path, exist_ok=True)

    # Download the dataset
    api.dataset_download_files(dataset_name, path=download_path)

    # Unzip the downloaded file
    zip_file_path = os.path.join(download_path, f"{dataset_name.split('/')[-1]}.zip")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)

    # Remove the zip file after extraction
    os.remove(zip_file_path)

    csv_file_path = os.path.join(download_path, f"{dataset_name.split('/')[-1]}.csv")
    parquet_file_path = os.path.join(download_path, f"{dataset_name.split('/')[-1]}.parquet")

    if os.path.exists(csv_file_path):
        # Convert CSV to Parquet
        df = pd.read_csv(csv_file_path)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, parquet_file_path)

        # Remove the CSV file after conversion
        os.remove(csv_file_path)

    if os.path.exists(parquet_file_path):
        print(f"Dataset downloaded and converted to Parquet at: {parquet_file_path}")