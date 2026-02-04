import pandas as pd
import numpy as np
import os
import re

#----UTILS----#
RAW_DIR = "data/raw"
PROC_DIR = "data/processed"
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROC_DIR, exist_ok=True)

# Domain synonyms to group
DOMAIN_MAP = {
    'language': 'Language',
    'text': 'Language',

    'vision': 'Vision',
    'image': 'Vision',
    'images': 'Vision',
    'video': 'Vision',
    'image generation': 'Vision',
    'video generation': 'Vision',

    'audio': 'Audio',
    'speech': 'Audio',

    'robotics': 'Robotics',
    'robot': 'Robotics',

    'recommendation': 'Recommendation',
    'recommender': 'Recommendation',

    'search': 'Search',

    'biology': 'Biology',
    'bio': 'Biology',

    'games': 'Games',
    'game': 'Games',

    'materials science': 'Materials science',
    'material science': 'Materials science',
    'materials': 'Materials science',

    'earth science': 'Earth science',
    'geo': 'Earth science',

    '3d modeling': '3D modeling',
    '3d': '3D modeling',

    'medicine': 'Medicine',
    'medical': 'Medicine',
    'health': 'Medicine',

    'driving': 'Driving',
    'autonomous': 'Driving',

    'psychology': 'Psychology',
    
    'astronomy': 'Astronomy',

    'cybersecurity': 'Cybersecurity',

    'mathematics': 'Mathematics',
    'math': 'Mathematics'

}

# Organization categories
ORG_CATEGORIES = ['Academia', 'Industry', 'Government', 'Research collective']

# Cloud compute vendors map
CLOUD_MAP = {
    'AWS': ['AWS', 'Amazon Web Services'],
    'Google Cloud': 'Google Cloud',
    'Microsoft': 'Microsoft',
    'IBM': 'IBM',
    'Azure AI': 'Azure AI',
    'Cerebras': 'Cerebras',
    'Oracle': 'Oracle',
    'Nebius AI': 'Nebius AI',
    'LambdaLabs': 'LambdaLabs',
    'Databricks': 'Databricks'
}
# Reverse vendors map to make lookup easier later
REVERSE_CLOUD_MAP = {alias: canonical for canonical, aliases in CLOUD_MAP.items() for alias in aliases}

#----HELPER FUNCTIONS-----#
def process_countries(df):
    # Standardize 
    df['country'] = df['country'].astype(str).str.strip()

    # Drop rows where country is 'Nan' or NaN
    df = df[df['country'].notna() & (df['country'].str.lower() != 'nan')].copy()

    # Create country_main = first listed country
    df['country_first'] = df['country'].str.split(',').str[0].str.strip()

    def normalize_country(value):
        if not value:
            return None 
        
        # Split and clean
        countries = [c.strip().title() for c in value.split(',') if c.strip()]
        unique_countries = list(set(countries))

        # Multinational exists in value
        if any(c.lower() == 'multinational' for c in unique_countries):
            return 'Multinational'
        
        # More than one unique country
        if len(unique_countries) > 1:
            return 'Multinational'

        # All same country
        return unique_countries[0]

    df['country'] = df['country'].apply(normalize_country)
    return df

def keyword_match(text, mapping):
    text = text.lower()
    for k, v in mapping.items():
        if re.search(rf"\b{re.escape(k)}\b", text):
            return v
    return None

def extract_domain_group(value):
    if pd.isna(value):
        return pd.NA 
    
    text = value.lower()

    # Direct multimodal flag
    if "multimodal" in text:
        return "Multimodal"
    
    # Split comma lists
    parts = [p.strip() for p in text.split(",") if p.strip()]

    # Map each part
    mapped = {keyword_match(p, DOMAIN_MAP) for p in parts}
    mapped.discard(None)

    if len(mapped) == 0:
        return pd.NA 
    
    if len(mapped) > 1:
        return "Multimodal"
    
    return next(iter(mapped))

def harmonize_orgs(value):
    if pd.isna(value):
        return pd.NA 
    
    # Split comma and strip
    parts = [p.strip().title() for p in value.split(',') if p.strip()]

    # Remove duplicates
    parts = list(set(parts))

    # Keep valid categories
    parts = [p for p in parts if p in ORG_CATEGORIES]

    if not parts:
        return pd.NA

    # Sort by index in ORG_CATEGORIES
    parts.sort(key=lambda x: ORG_CATEGORIES.index(x))
    
    # Rejoin into string
    return ', '.join(parts)

def harmonize_cloud_vendor(value):
    if pd.isna(value):
        return pd.NA
    
    # Split by comma and strip
    parts = [p.strip() for p in value.split(',') if p.strip()]
    
    # Map to canonical names
    mapped = [REVERSE_CLOUD_MAP.get(p, p) for p in parts]
    
    # Remove duplicates and preserve order
    seen = set()
    unique_parts = []
    for p in mapped:
        if p not in seen:
            seen.add(p)
            unique_parts.append(p)
    
    if not unique_parts:
        return pd.NA
    
    # Join back into a single string
    return ', '.join(unique_parts)

#----MAIN SCRIPT----#
# Fetch data from url
data_url = "https://epoch.ai/data/all_ai_models.csv"
raw_path = os.path.join(RAW_DIR, 'all_models_raw.csv')
clean_path = os.path.join(PROC_DIR, "all_models_clean.csv")

# Load raw data
models_df = pd.read_csv(data_url)

# Save raw data
models_df.to_csv(raw_path, index=False)

# Drop notes and large text columns, as well as columns with significant missing data (>=99%)
cols_to_drop = [
    'Notability criteria notes', 'Parameters notes', 'Training compute notes', 'Dataset size notes', 'Training time notes', 'Post-training compute notes',
    'Abstract', 'Finetune compute notes', 'Archived links', 'Batch size notes', 'Accessibility notes', 'Utilization notes', 'WikiText and Penn Treebank data',
    'Post-training compute (FLOP)', 'Hardware utilization (MFU)', 'Hardware utilization (HFU)', 'Training compute lower bound', 'Training compute upper bound',
    'Hugging Face developer id', 'Training data center', 'Numerical format'
]
models_df = models_df.drop(cols_to_drop, axis=1)

# Rename columns
models_df = models_df.rename(columns={
    'Country (of organization)': 'Country'
})

# Drop rows without publication date - 19 rows
models_df.dropna(subset=['Publication date'], inplace=True)

# Extract year from publication date
models_df["year"] = pd.to_datetime(models_df["Publication date"], errors='coerce').dt.year

# Standardize column names
models_df.columns = models_df.columns.str.lower().str.replace(' ', '_')

# Fill NA values in boolean columns with False
models_df['foundation_model'] = models_df['foundation_model'].fillna('False')
models_df['frontier_model'] = models_df['frontier_model'].fillna('False')
models_df['possibly_over_1e23_flop'] = models_df['possibly_over_1e23_flop'].fillna('False')

# Fill NA values in columns where 'Unknown'
models_df['authors'] = models_df['authors'].fillna('Unknown')
models_df['model_accessibility'] = models_df['model_accessibility'].fillna('Unknown')

# Dtype conversions for standardization
models_df['training_dataset_size_(gradients)'] = pd.to_numeric(models_df['training_dataset_size_(gradients)'], errors='coerce')
models_df['publication_date'] = pd.to_datetime(models_df['publication_date'])

# Create era column
# Where deep learning era is considered years 2010 or later
# And pre deep learning era is years before 2010
models_df['era'] = np.where(models_df['year'] >= 2010, 'Deep learning era', 'Pre deep learning era')

# Create notable_model column
# Where a notable model has notability_criteria 
# And a non-notable model does not have notability_criteria
models_df['notable_model'] = np.where(models_df['notability_criteria'].isna(), 'False', 'True')

# Process countries
models_df = process_countries(models_df)

# Process domains and separate into higher-level domain_group
models_df['domain_group'] = models_df['domain'].apply(extract_domain_group)

# Harmonize organizations
models_df['organization_categorization'] = models_df['organization_categorization'].apply(harmonize_orgs)

# Harmonize cloud vendors
models_df['training_cloud_compute_vendor'] = models_df['training_cloud_compute_vendor'].apply(harmonize_cloud_vendor)

# Save cleaned full dataset
models_df.to_csv(clean_path, index=False)