from etl_process.extract import download_kaggle_dataset

if __name__ == "__main__":

    dataset_name_v1 = "realkiller69/gaia-data-set-for-stellar-classificationdr3"
    dataset_name_v2 = "realkiller69/gaia-stars-dataset-from-dr3-data-release-3"  # Replace with the actual dataset name
    TARGET_DIR = "./data"  # Replace with the desired download path
    
    download_kaggle_dataset(dataset_name_v1, TARGET_DIR)
    download_kaggle_dataset(dataset_name_v2, TARGET_DIR)