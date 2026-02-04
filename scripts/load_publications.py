import pandas as pd
from zipfile import ZipFile
import os

DROP_REGIONS = ["EU27"]

def load_publications(zip_file):
    # Extract from zip
    extract_dir = 'data/raw'
    with ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    # Path to extracted csv
    csv_path = os.path.join(extract_dir, zip_ref.namelist()[1])

    # Read
    df = pd.read_csv(csv_path)

    # Select columns
    df = df[['Country_label', 'publications', 'year']]

    # Rename
    df = df.rename(columns={'Country_label': 'country_first', 'publications': 'publication_count'})

    # Drop EU region
    df = df[~df["country_first"].isin(DROP_REGIONS)].reset_index(drop=True)

    return df