# pip install kaggle
import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi


def download_kaggle_dataset(dataset, path='datasets/'):
    """
    Download a Kaggle dataset to the specified path.

    Parameters:
    - dataset: str, full dataset path on Kaggle in format "USERNAME/DATASET_NAME".
    - path: str, local path where the dataset will be downloaded.
    """
    # Ensure the Kaggle API token is set up
    kaggle_json_path = os.path.expanduser('~/.kaggle/kaggle.json')
    if not os.path.exists(kaggle_json_path):
        raise ValueError(
            f"Kaggle API credentials not found at {kaggle_json_path}. Download kaggle.json from Kaggle and place it in ~/.kaggle/.")

    # Initialize the Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Ensure the path exists
    if not os.path.exists(path):
        os.makedirs(path)

    # Download dataset
    api.dataset_download_files(dataset, path=path, unzip=True)

    # Since Kaggle datasets can have nested directories, we want to unzip and place them in a flattened structure
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.zip'):
                with zipfile.ZipFile(os.path.join(root, file), 'r') as zip_ref:
                    zip_ref.extractall(path)

    print(f"Dataset {dataset} downloaded successfully to {path}")

# Example use
# download_kaggle_dataset('shivamb/netflix-shows')
