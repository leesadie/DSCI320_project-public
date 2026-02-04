import pandas as pd

def load_export_controls(filepath):
    # Read
    df = pd.read_csv(filepath)

    # Select columns
    df = df[['Implementing Jurisdictions', 'Intervention Type', 'Date Implemented']]

    # Rename
    df = df.rename(columns={
        'Implementing Jurisdictions': 'country_first',
        'Intervention Type': 'intervention_type',
        'Date Implemented': 'date'
    })

    # Get year from date
    df["year"] = pd.to_datetime(df["date"], errors='coerce').dt.year

    # Split comma separated countries and explode into rows
    df = df.assign(country_first=df['country_first'].str.split(',')).explode('country_first')

    # Strip
    df['country_first'] = df['country_first'].str.strip().str.title()

    # Drop exact duplicate rows
    df = df.drop_duplicates() 

    # Count number of export controls per country, per year
    export_counts = (
        df.groupby(['country_first', 'year'])
          .size() 
          .reset_index(name='export_controls_count')
          .sort_values(['country_first', 'year'])
          .reset_index(drop=True)
    )

    # Sum of export controls up to and including year per country
    export_counts['export_controls_sum'] = (
        export_counts.groupby('country_first')['export_controls_count'].cumsum()
    )

    # Keep only sum for merge
    export_counts.drop('export_controls_count', axis=1, inplace=True)

    return export_counts