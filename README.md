# Patterns of Growth - Mapping the Trajectory of AI Model Development

View the website here: https://patterns-of-growth.vercel.app/

## Project description

We aim to explore how AI models have progressed over time from the following lenses: 
1. Temporal patterns: Scaling of key training attributes over time, temporal regime changes in model growth, changes in model accessibility, evolution of model resource efficiency
2. Geographic patterns: Geographic distributions of AI models and their training resources, evolution of geographic clusters for frontier models, large-scale model correlations with a country's research output and export controls on semiconductors 
3. Cost, scale, and efficiency patterns: How has cost, scale, and efficiency of models changed over time, how does it differ between frontier and non frontier models.

## Dataset

The AI models dataset from Epoch AI contains over 3000 machine learning models released from 1950 to 2025, documented over a broad range of domains and organization types. Key development and release characteristics include training compute in floating point operations (FLOPs), power draw, parameter count, and model accessibility level. This dataset is useful in examining historical trends in the growth of artificial intelligence.

We merge the AI models dataset with two other datasets for supplementary information: 1) export controls (i.e. restrictions) on semiconductors per country and year from Global Trade Alert, and 2) AI-related academic publications per country and year from OECD. We use export controls on semiconductors to consider relationships between regulations on the hardware needed to develop AI models and overall model growth, e.g. in training compute. Considering AI-related academic publications enables observations regarding translation from research to model release.

Source information (see [References](#references) for citations):
1. Epoch AI: https://epoch.ai/data/ai-models
    - License: Creative Commons Attribution
2. Global Trade Alert: https://globaltradealert.org/threads/export-controls-on-semiconductors
    - License: Creative Commons
3. OECD: https://oecd.ai/en/data?visualizationFiltersHash=eyJkYXRlIjpbIjE5OTkiLCIyMDI0Il19
    - License: Creative Commons

## Package requirements

View package verisons in `requirements.txt`. Install with the following:
```
pip install -r requirements.txt
```

## File structure

```
.
├── analysis
│   ├── geographic              
│   ├── resources  
│   ├── temporal                 
├── data                    
│   ├── raw              
│   ├── processed              
├── assets
├── scripts
├── .gitignore
├── final_report.md
├── LICENSE
├── README.md
└── requirements.txt
```

## References

1. Epoch AI, ‘Data on AI Models’. Published online at epoch.ai. Retrieved from ‘https://epoch.ai/data/ai-models’ [online resource]. Accessed 24 Oct 2025.
2. OECD.AI (2025), data from OpenAlex, last updated 2025-09-30, accessed on 2025-10-24, https://oecd.ai/
3. Global Trade Alert. 'Export controls on semiconductors'. Global Trade Alert. Retreived from https://globaltradealert.org/threads/export-controls-on-semiconductors. Accessed 24 Oct 2025.