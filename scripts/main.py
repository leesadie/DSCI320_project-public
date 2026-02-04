# To run, copy the below in terminal to allow for package-like imports from other folders:
# python -m scripts.main

# Imports
import pandas as pd
from scripts.load_export_controls import load_export_controls
from scripts.load_publications import load_publications

COUNTRY_MAP = {
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "United Kingdom Of Great Britain And Northern Ireland": "United Kingdom",
    "United States of America": "United States",
    "United States Of America": "United States",
    "China (People's Republic Of)": "China",
    "China (People'S Republic Of)": "China",
    "Korea (Republic Of)": "South Korea",
    "Korea, Rep.": "South Korea",
    "Republic of Korea": "South Korea",
    "Russian Federation": "Russia"
}

# Load data
export_controls = load_export_controls('data/raw/interventions.csv')
publications = load_publications('data/raw/oecd-ai-data.zip')
models = pd.read_csv('data/processed/all_models_clean.csv')

# Standardize countries
def standardize_country(df, country_col1="country_first", country_col2=None):
    df[country_col1] = df[country_col1].str.strip().str.title()
    df[country_col1] = df[country_col1].replace(COUNTRY_MAP)

    if country_col2:
        df[country_col2] = df[country_col2].str.strip().str.title()
        df[country_col2] = df[country_col2].replace(COUNTRY_MAP)
        
    return df
export_controls = standardize_country(export_controls)
publications = standardize_country(publications)
models = standardize_country(models, country_col2='country')

# Make copy for merge: base = models
merged_df = models.copy()

# Merge export controls
merged_df = merged_df.merge(export_controls, on=['country_first', 'year'], how='left')

# Merge publications
merged_df = merged_df.merge(publications, on=['country_first', 'year'], how='left')

# Save
merged_df.to_csv('data/processed/models_final.csv', index=False)
