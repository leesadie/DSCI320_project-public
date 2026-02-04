# Python Functions

Data wrangling scripts
- `__init__.py`: empty file to allow for package-like imports when calling `main.py`
- `load_models.py`: loads and processes the main dataset of AI model growth characteristics
- `load_export_controls.py`: function to load and process data for export controls on semiconductors 
- `load_publications.py`: function to load and process data for count of AI-related academic publications
- `main.py`: loads, standardizes, and merges data for models, export controls, and publications
    - Calls functions from `load_export_controls.py` and `load_publications.py`