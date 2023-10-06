import tarfile
import urllib
import os


DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
DATA_URL = DOWNLOAD_ROOT + "datasets/data/data.tgz"  # Update for your data
DATA_PATH = os.path.join("../../datasets", "data")


def fetch_tgz_data(housing_url=DATA_URL, data_path=DATA_PATH):
    try:
        os.makedirs(data_path, exist_ok=True)
        tgz_path = os.path.join(data_path, "data.tgz")
        urllib.request.urlretrieve(housing_url, tgz_path)
        data_tgz = tarfile.open(tgz_path)
        data_tgz.extractall(path=data_path)
        data_tgz.close()
        print('Data downloaded')
    except Exception as e:
        print("Error in fetch_housing_data: ", e)