# Final Report

View the website here: https://patterns-of-growth.vercel.app/

## Overview

**Audience**

The intended audience includes people with basic familiarity of AI model training and development, who are interested in understanding how different factors have shaped the trajectory of AI progress. We expect the audience to gain insight into how AI development has evolved and its trends of growth over time.

**Dataset**

We use the AI models dataset from Epoch AI, which contains over 3000 machine learning models released from 1950 to present (2025) and documents key factors that have driven progress. Models are collected from a variety of sources including literature reviews, historical accounts, publications, leading industry labs, bibliographies, pre-existing datasets on AI papers, and suggestions from contributors. To be included in the dataset, Epoch AI considered that an ML model must 1) have reliable documentation and relevance to machine learning, 2) include a learning component, i.e. not be a non-learned algorithm, and 3) have actually been trained, not a purely theoretical description.

We merge the AI models dataset with two other datasets as supplementary information: 1) export controls (i.e. restrictions) on semiconductors per country and year from Global Trade Alert, and 2) AI-related academic publications per country and year from OECD.

**General takeaways**

We hope the audience can explore the temporal patterns of how models have scaled over time, geographic patterns of where model development is concentrated at the global level, and cost and efficiency patterns of training as models have advanced.

## Temporal patterns

**Data Wrangling**

View 1: In order to visualize data as hexbins, variables of interest (training compute, parameters, power draw, training time, and training cost) were log-scaled and aggregated by mean per year. 

View 2: Model accessibility levels were mapped to open and closed for the aggregated line chart, where open corresponds to all levels of open weights, API access, and hosted access, and closed refers to unreleased models or unknown access.

View 3: Resource efficiency metrics were computed and log-scaled, namely, cost per compute FLOP, cost per parameter, compute per dollar, and compute per power draw watt. A composite efficiency metric was then computed, considering that a higher cost per FLOP and cost per parameter indicate more efficiency, and a lower compute per dollar and compute per watt indicate more efficiency.

### View 1

**Title**: AI Model Progress Over Time

**Questions and low-level tasks**

This view aims to answer,"How have training compute, parameter count, power draw, training cost, and training time scaled over time, and how do these trends differ across domains, countries, and organization types?".

Tasks
- Characterize distribution: How have model training attributes scaled over time?
- Correlate: How do model training attributes correlate with domain and organization types?
- Find anomalies: Are there significant temporal breakpoints in the scaling of model training?

**View**
*Note: View interactions in website at https://patterns-of-growth.vercel.app/#view1

<img src ="/assets/temporal/view1.png" width="700px">

**Description and characteristics of channels**

Marks: Both charts use points. Chart 1 uses hexbins as shape where individual models are aggregated by log-mean of the selected y-axis metric. Chart 2 uses filled circles as shape, which each represent an individual model.

Channels
- Chart 1 (hexbin) uses x-position for publication year, y-position for selected y-axis metric, and color (saturation) for level of y-axis metric. Discriminability is exploited such that individual points can be easily distinguished via aggregation. Aggregating individual models into hexbins is well-aligned to the analytic task of characterizing the overall distribution of how model training attributes have scaled over time by representing all models across the full range of years, while reducing overplotting. By visualizing the overall distribution, determining if temporal breakpoints exist is also achievable.
- Chart 2 (scatter) uses x-position for publication year, y-position for selected y-axis metric, and color (hue) if a category is selected via radio buttons. Separability is exploited to encourage users to concentrate on each individual point (model) sequentially. Color hue for each category aligns with the task of understanding the relationship between model training attributes and categories such as domain and organization type.

**Interaction**

Indirect manipulations
1. Y-axis dropdown selection: Selects a metric and changes the y-axis of both charts simultaneously. Default is training compute.
2. Categorize models radio buttons (chart 2): Colors model points by domain, country, or organization type. Default is none.
3. Deep learning era checkbox (chart 1): Overlays a box and text to mark the deep learning era (2010-current). Default is empty.
4. Model name regex search input (chart 2): Search for a model name in the brush selected year range. Default is empty.

Direct manipulations
1. Bidirectional
    a. X-axis (year) brush selection in chart 1 filters chart 2.
    b. Clicking on a point in chart 2 maintains opacity of the associated hexbin and reduces opacity of other points in chart 1.
2. Selecting a category on the legend in chart 2 when models are categorized maintains opacity of points in that category and reduces opacity of other points.

**Insights**
Over time, it is clear that models have scaled across all of the attributes examined, particularly in terms of training compute required, number of trainable parameters, and training time. It is notably more difficult to examine patterns over time for power draw and training cost, as these metrics were generally not recorded until after 2010.

The deep learning era (2010-2025) contains the highest concentration of model releases, as expected, and also shows an increase in usage for the metrics examined. This implies the evident significance of the deep learning era as an inflection point in AI development, likely due to other factors such as the introduction of graphical processing units (GPUs) for general purpose parallel computing.

**Critique**

While this view aimed to reduce overlap and high concentration of model points in the deep learning era, for years 2018 to 2025, points still display non-trivial overlap in the scatterplot (chart 2) given the many models of similar scale (e.g. in compute or parameters) within these years. This leads to low discriminability between points, where users may not be able to perceive a sufficient amount of unique steps. 

Additionally, since certain metrics such as power draw and training cost were not extensively recorded until around 2010, when the x-axis brush selection is before 2010, chart 2 is empty. This may be confusing for users, as it may seem more like an error rather than lack of data. 

Although the many interactions used in this view enable the user to actively engage with the data, this may require significant time and attention even with the imposition of defaults, thereby increasing cognitive load, attentional demand, and perceptual costs.

### View 2

**Title**: Resource Efficiency Over Time

**Questions and low-level tasks**

This view aims to answer,"How has model resource efficiency (i.e. cost per FLOP, cost per parameter, compute per dollar, compute per watt) evolved over time, and do metrics exhibit diminishing returns?".

Tasks
- Compute derived value: What is a model’s cost per FLOP, cost per parameter, compute per dollar, and compute per watt?
- Compute derived value: What is the composite resource efficiency index for each year?
- Characterize distribution: How have efficiency metrics changed over time?

**View**

*Note: View interactions in website at https://patterns-of-growth.vercel.app/#view2

<img src ="/assets/temporal/view3.png" width="700px">

**Description and characteristics of channels**

Marks: Chart 1 uses a line which represents the mean composite resource efficiency index over time. Chart 2 uses lines to indicate the composition of metric values (cost per FLOP, cost per parameter, compute per dollar, and compute per watt) for the brush selected year range. Chart 3 uses points with a filled circle shape for each individual model.

Channels: 

- Chart 1 (line) uses x-position for publication year and y-position for mean composite efficiency. Accuracy is exploited given the common x-position and y-position scales to visualize how overall resource efficiency has changed over time. An overall line is well-aligned to the task of characterizing the distribution of how efficiency metrics have changed over time.
- Chart 2 (line - bars) uses x-position for publication year (ordinal scale), y-position for normalized metric value, and color (hue) for normalized metric category. Grouping is exploited as metrics are grouped by year in order to compare between years and metric differences within each year. Visualizing the composition of metrics is also aligned to the task of understanding how each efficiency metric has changed over time.
- Chart 3 (scatter) uses x-position for composite efficiency index and y-position for training compute in FLOPs. Accuracy is exploited with the common x-position and y-position scales to visualize how a model’s composite resource efficiency compares to its scale in terms of compute.

**Interaction**

Indirect manipulations
1. Yearly percent change checkbox (chart 1): Overlays text above the line to mark the year-to-year percent change in composite efficiency index. Default is empty.

Direct manipulations
1. X-axis (year) brush selection in chart 1 filters chart 2 and chart 3.

**Insights**
Seeing how overall model scale has grown over time, it is significant to note that the use of these resources required to train AI models has become generally more efficient. In many domains, scaling leads to increased expenses on a per-unit basis. Even in an algorithmic complexity sense, for example, more complex algorithms tend to have worse asymptotic constraints. The fact that larger AI models yield more efficient usage, e.g. lower cost per parameter and cost per FLOP, thus runs counter to traditional intuitions about scaling.

In other words, while most technologies show diminishing returns at high scale, there's no apparent saturation point yet for the large-scale AI models we currently use. This could suggest that improving models by scaling up is a more efficient path.

**Critique**

Since metrics such as power draw were only consistently reported starting around 2010, this chart only displays data from 2010-2025, i.e. the deep learning era. This may not necessarily answer the question of how model resource efficiency has evolved over time, rather, it is more aligned with answering how model resource efficiency has evolved across the deep learning era.

Points in the scatterplot (chart 3) are also highly clustered, making it difficult to determine individual points. Additionally, while the scatterplot explores compute versus the aggregated efficiency index, identifying which models contribute to which specific metric for the year range may have been more beneficial to understanding how metrics have changed over time in relation to model scale.

### View 3

**Title**: Evolution of Model Accessibility

**Questions and low-level tasks**

This view aims to answer, "How have model accessibility levels changed over time, and how does this correlate with training compute?".

Tasks
- Characterize distribution: How has the model accessibility levels changed over time?
- Correlate: How does model accessibility correlate with training compute?

**View**

*Note: View interactions in website at https://patterns-of-growth.vercel.app/#view3

<img src ="/assets/temporal/view2.png" width="700px">

**Description and characteristics of channels**

Marks: Chart 1 uses lines which represent log-mean training compute in FLOPs over time. Chart 2 uses lines (bars) to indicate the specific model accessibility levels for the brush selected year range.

Channels
- Chart 1 (line) uses x-position for publication year, y-position for log-mean training compute in FLOPs, and color (hue) to categorize open versus closed models. Accuracy is exploited in order to visualize differences in compute between open and closed models, with the common x-position and y-position scales.
- Chart 2 (bar) uses x-position for model count, y-position for model accessibility level, and color (saturation) for model accessibility level. Y-position of model accessibility levels are sorted from most open (unrestricted open weights) to least open (unreleased), and unknown. Discriminability is exploited such that the difference in counts for each model accessibility level can be clearly seen based on the x-position of the bar as well as the distinct color saturation for each level.

**Interaction**

Direct manipulations
1. X-axis (year) brush selection in chart 1 filters chart 2.
2. Selecting a category on the legend in chart 2 maintains opacity of points in that category and reduces opacity of other points.
3. Selecting a bar in chart 2 overlays text for the model with the highest amount of training compute in that category, given the year range selected by the brush.

**Insights**
Models have changed in how they can be accessed and used by the public, with more institutions offering open weights, i.e. where a model's trained parameters are publicly shared, yet not having access be a significant factor in the scale of a model's compute. This means that some of the largest-scale models in terms of compute that have been trained to date generally have some level of transparency and accessibility. However, given this large scale, it also means that users would need the necessary computational power to actually use these weights efficiently, which may not be feasible.

**Critique**

While bars in chart 2 are sorted from most open to least open, sorting is not necessarily in numerical order. This may increase cognitive load and be unintuitive to users, especially as the scale of open to closed may not be familiar. 

From 1950 to 1990, all models have an unknown model accessibility level. It may then be difficult to fully understand how model accessibility has changed across the entire year range, and particularly from the pre deep learning era to the deep learning era.

Given the aggregation of models into open versus closed in chart 1, it may be difficult to see how a specific model accessibility level, e.g. unrestricted open weights, is correlated with training compute. Although text overlays on click display the model with the highest compute for that accessibility level within the year range, attempting to identify the correlation over time may require significant attentional demand.

## Geographic patterns

**Data Wrangling**

**View 1**: Country names were standardized to resolve spelling variants and abbreviations, records with missing or ambiguous country or year values were removed, and multinational entries were excluded to ensure clear national attribution. Model releases were then aggregated by country to compute total model counts and identify the global top 10 contributors.

**View 2**: Organization categories were consolidated into four main types (Academia, Industry, Government, Multiple), training compute was log-scaled to manage heavy skew, and the dataset was filtered to the top 10 countries. A year-based slider was implemented to support temporal filtering of accessibility and compute patterns.

**View 3**: Model parameters and training compute were log-scaled to enable comparison across orders of magnitude. Publication intensity and export control scores were discretized into Low, Medium, and High bins using quantiles to support categorical visual encoding and country-level filtering.

### View 1

**Title**: Global Leaders in AI Model Releases

**Questions and low-level tasks**

Tasks
- Rank countries by total model count
- Compare contributions across the top producers
- Identify the geographic location of major AI-producing countries

**View**

*Note: View interactions in website at https://patterns-of-growth.vercel.app/#geo_view1

<img src ="/assets/geographic/view1.png" width="700px">

**Description and characteristics of channels**

Marks: Chart 1 uses geoshapes to represent countries on a world map. Chart 2 uses bars to represent aggregated national model counts for the top 10 producing countries.

Channels
- Chart 1 (map) uses geographic position to encode country location and color (saturation) to encode total model count on a logarithmic scale. Color saturation indicates greater model production, allowing dominant contributors to be distinguished from lower-producing countries at a global scale.
- Chart 2 (bar chart) uses x-position to encode total model count and y-position to encode country name, sorted in descending order. Accuracy is achieved through aligned bar lengths, which support precise comparison and ranking of national AI output.

**Interaction**

Direct manipulations
1. Clicking a country in the bar chart highlights the same country on the map and fades all others
2. Clicking a country on the map highlights the corresponding bar in the bar chart.

**Insights**
The United States and China lead global AI development in terms of the total number of AI models released over time. This is expected, given that many of the institutions that are key players in AI development are based in the United States, such as OpenAI, Google, Meta AI, and NVIDIA.

Also expected are the remainder of the countries which make up the top five. Namely, the United Kingdom is home to Google DeepMind, and Canada is home to academic institutions that led key methodological innovations particularly in the earlier stages of AI, such as backpropagation and the ReLU activation function.

**Critique**

This view shows that AI model development is concentrated in a small number of countries, with the United States and China dominating. The combination of a ranked bar chart and a geographic map allows users to see both numerical magnitude and real-world location at the same time. Linked highlighting strengthens the connection between these two representations.

However, the view is aggregated across time, so it does not show how leadership has shifted over the years. Excluding multinational models simplifies attribution but removes cross-border collaborations. Additionally, the logarithmic color scale on the map can make differences between lower and middle-producing countries harder to distinguish.

### View 2

**Title**: Publication Intensity, Export Controls, and Model Scale

**Questions and low-level tasks**
Within a country, how do publication activity and export controls relate to model scale and training compute?

Tasks
- Filter analysis by country
- Compare model parameters and compute
- Compare compute across export-control levels
- Compare model counts across export-control levels

**View**

*Note: View interactions in website at https://patterns-of-growth.vercel.app/#geo_view2

<img src ="/assets/geographic/view2.png" width="700px">

**Description and characteristics of channels**

Marks: Chart 1 uses points (scatter plot). Chart 2 uses a boxplot. Chart 3 uses lines (bars).

Channels
- Chart 1 (scatter) uses x-position for log parameters, y-position for log training compute, color (hue) for organization type, size for publication intensity, and shape for export-control level, enabling multivariate comparison at the model level.
- Chart 2 (boxplot) uses x-position for export-control level and y-position for log training compute to summarize distributional differences in compute across governance categories.
- Chart 3 (bar chart) uses x-position for export-control level and y-position for model counts to compare the volume of models within each regulatory category.

**Interaction**

Indirect manipulations
1. A country dropdown filters all charts to a selected country, where country is limited to the top 5 in terms of model release, enabling focused national-level analysis.

Direct manipulations
1. Selecting an organization in the legend highlights corresponding points in the scatter plot.

**Insights**
Reflecting the top countries in terms of number of AI models released, it's interesting to note that while both the United States and China produce large models, the United States has greater variation in its export controls on semiconductors and intensity of AI-related publications. Whereas, China tends to have low export controls and a high intensity of AI-related publications.

Further, for the United States, the distribution of training compute is fairly comparable across all levels of export controls, indicating that export controls have not significantly limited available training compute.

**Critique**

This view supports detailed analysis of how governance constraints and research intensity relate to model scale within individual countries. It highlights how export controls interact with compute investment and how highly published models tend to cluster at the upper end of scale. However, the use of multiple simultaneous encodings and log-scaled axes increases perceptual complexity. Additionally, forcing single-country selection limits the ability to directly compare regulatory regimes across nations.

Further, the overlap of points leads to low discriminability and decrease perception of unique steps.

### View 3

**Title**: Model Accessibility and Compute by Organization and Country

**Questions and low-level tasks**

How does model accessibility vary across organization types, and how does training compute differ across organization–country combinations?

Tasks
- Compare accessibility composition across organization types
- Compare training compute across organization and country
- Observe changes over time using the year slider

**View**

*Note: View interactions in website at https://patterns-of-growth.vercel.app/#geo_view3

<img src ="/assets/geographic/view3.png" width="700px">

**Description and characteristics of channels**

Marks: Chart 1 uses bars (normalized stacked) to show accessibility composition. Chart 2 uses rectangles (heatmap) with overlaid text labels

Channels
- Chart 1 (stacked bar) uses x-position for organization type, y-position for normalized model share, and color (hue) for model accessibility level. Discriminability is exploited so differences in openness across organizations can be easily compared.
- Chart 2 (heatmap) uses x-position for organization type, y-position for country, and color (saturation) for mean log training compute. Text labels provide numeric summaries to improve readability of color differences.

**Interaction**

Indirect manipulations
1. A year slider filters both charts to models released up to the selected year, enabling exploration of historical versus recent trends.

**Insights**

At both a country-level and organization-level, compute is not significantly related to model accessibility, reflecting the earlier temporal findings.

**Critique**

This view clearly shows how openness differs by organization type and how compute varies by country and institution. Normalized stacked bars emphasize proportional differences rather than volume, while the heatmap provides a compact overview of compute intensity. However, using mean log compute may hide within-group variation, and the year slider only supports one-sided temporal filtering.

Gaps in the heatmap may also be disorienting to users; while they indicate lack of data for that organization type and country, this may be unintuitive to understand.

## Cost, Scale, and Efficiency Patterns

**Data Wrangling**

All Views: In order to best visualize efficiency, cost, and scale data, all views generated the variables of interest explored throughout my EDA. Additionally, data points with empty values were dropped and appropriate names were mapped to the neccessary variables.

View 1: In order to visualize data as lines over time, median FLOPs per $ and per watt values were calculated grouped by year and frontier model type. The data frame was also reshaped to longform.

View 2: Minimal additional data wrangling was used for this visualization.

View 3: Correlations were calculated for every possible combination of focus columns for all unique years with complete data. This data was then converted to long form and mapped with appropriate titles. When mapping correlations to the yearly breakdown, same variable values (i.e Corr = 1) are filtered out.

### View 1

**Title**: Efficiency metrcis have increase over the deep learning era

**Questions and low-level tasks**

This view aims to answer, "How has model efficiency changed in the deep learning era, and how do different organizations frontier models compare against each other?".

Tasks
- Characterize growth: How has model efficiency changed over time?
- Find anomalies: Have any organizations exceeded in their metrics?

**View**

*Note: View interactions in website at https://patterns-of-growth.vercel.app/#efficiency_view1

<img src ="/assets/resources/view1.png" width="700px">

**Description and characteristics of channels**

Marks: Charts 1 uses lines which represent log-median efficiency metrics including flops per dollar, flops per hour and flops per watt. Chart 2 uses bars to show the release pattern of frontier and non frontier models in the deep learning era. Chart 3 uses points to create a scatter plot of individual organization efficiency metrics.

Channels
- Chart 1 (line) uses x-position for publication year, y-position for log-median efficiency measures, and color (hue) is used to differentiate between the three efficiency metrics observed. We use accuracy as a consistent reference point to reveal efficiency differences across years.
- Chart 2 (bar) uses x-position for publication year, y-poisition for publication count, and color to encode the frontier status. We exploit discriminability to clearly visualize yearly counts and differences in frontier status of the models released
- Chart 3 (scatter) uses x-position for publication year, y-position for log-median effiency measure, and color (hue) is again used to differentiate between metrics. Discriminability is exploited to clearly visualize and contextualize year-to-year and organization-organization differences that the aggregated line chart cannot convey.

**Interaction**

Direct manipulations
1. Selecting a color group on the scatter plot maintans opacity for the selected metrics points while reducing the opacity for the other two.
2. Selecting a line on the line graph maintains opacity for the selected line while reducing the opacity for the other two.

Indirect manipulations
1. Organization dropdown in chart 3 allows the user to filter the plotted points to all leading organizations or any individual one.

BiDirectional manipulations
1. Selection in either the scatter or the line graphs direct manipulations will retain the selection for the other graph, regardless of organization filter.

**Insights**
Across the deep learning era, efficiency metrics have generally increased, also reflecting the earlier temporal findings. As expected, the models with the highest levels of training compute are frontier models, given that Epoch AI defines a frontier model in the dataset as models in the top 10 by training compute at the time of their release, a threshold that has increased over time as larger models are developed.

At the organization level, the data records xAI's 2025 Grok model as having the greatest efficiency in training compute FLOPs per training hour.

**Critique**

I would have liked to include the same efficiency variables for non-frontier models in the line chart to better contextualize the size and persistence of the performance gap, because seeing both trajectories side by side would clarify whether frontier advantages are widening, narrowing, or simply stable over time. 

The bar chart, while somewhat informative, feels comparatively static and slightly misaligned with the broader analytical goals; it shows a basic release order without offering the same dynamic or temporal perspective as the other visuals. 

Additionally, the scatter plots are hampered by the fact that several organizations contribute only a few data points, which creates visually unappealing and uninsightful visualizations that do not hold meaningful statistical weight.

### View 2

**Title**: Trends in AI Training Compute and Cost Over Time

**Questions and low-level tasks**

This view aims to answer, "How have model compute and cost levels changed over time, and how do they vary across model types?".

Tasks
- Characterize growth: How have model computes and costs changed over time?
- Correlate: How do model types change compute and cost values?

**View**

*Note: View interactions in website at https://patterns-of-growth.vercel.app/#efficiency_view2

<img src ="/assets/resources/view2.png" width="700px">

**Description and characteristics of channels**

Marks: Charts 1 and 2 uses lines which represent log-mean training compute in FLOPs over time and log-mean training costs in USD over time for boths model types. Charts 3 and 4 uses box plots to visualize the specific years compute and cost spread by model type.

Channels
- Chart 1 (line) uses x-position for publication year, y-position for log-mean training compute in FLOPs, and color (hue) to categorize frontier and non-frontier models. Chart 2 (line) uses x-position for publication year, y-position for log-mean training cost in USD, and color (hue) to categorize frontier and non-frontier models. We use accuracy as a consistent reference point to reveal compute differences between open and closed models through aligned x- and y-position scales.
- Chart 3 (box) uses x-position and color for model type, y-position for log-mean training compute in Flops for the selected year. Chart 4 (box) uses x-position and color for model type, y-position for log-mean training cost in USD for the selected year. Discriminability is exploited to clearly visualize and contextualize year-to-year differences that the line chart alone cannot convey. The box plot further enhances this by revealing not only changes in central tendency but also the full distribution of values across models.

**Interaction**

Direct manipulations
1. Selecting a type on the legend in either chart 1 or chart 2 maintains opacity of the lines in that category and reduces opacity of the other lines.

Indirect manipulations
1. X-axis (year) scale selection in chart 1 and 2 filters chart 3 and 4.

**Insights**
As training compute has grown, so have training costs. This is expected, and further seen where frontier models, i.e models leading in training compute, generally exhibit higher training costs than non-frontier models.

**Critique**

Although the use of a log scale is necessary to fit the full range of compute and cost values, it also makes the cost data far less interpretable to the average viewer. Differences that are meaningful in absolute terms become visually compressed, which may limit a reader’s ability to intuitively assess how training costs evolve across model types.

While the box plots effectively contextualize the patterns suggested by the line charts,particularly by revealing distributional spread rather than only central tendencies,they introduce some redundancy. These plots reinforce the same general message rather than adding substantially new information, and could potentially have been replaced or merged into a visualization that contributes additional insight.

Finally, given the relatively short time span available in the dataset, it is difficult to extract meaningful differences in long-term trends between model categories beyond the broad, expected separation in compute. The narrow temporal window limits the ability to observe shifts, inflection points, or structural changes, reducing the strength of conclusions one can draw from the trends.


### View 3

**Title**: Correlation Patterns Among Key AI Training Metrics

**Questions and low-level tasks**

This view aims to answer, "How have model compute, cost, efficiency, and scale correlate, and how have they changed over time?".

Tasks
- Compute Derived Value: How have key metrics correlated to each other over time?
- Characterize Distributions: How do these metrics relate to each other, how have relationships changed as models improve?

**View**

*Note: View interactions in website at https://patterns-of-growth.vercel.app/#efficiency_view3

<img src ="/assets/resources/view3.png" width="700px">

**Description and characteristics of channels**

Marks: Chart 1 uses a heatmap to represent correlation values of key cost, scale, and efficiency metrics over time. Chart 2 uses bar plots to order correlations by strength for each variable.

Channels
- Chart 1 (heatmap) uses x-position and y-position for correlation match and color (hue) to display correlation strength. We use x- and y-position scales to visually segregate correlation pairs and color hue to clearly convey differences in correlation strength.
- Chart 2 (bar) uses x-position and color to indicate correlation strength, x-position is also used to order variables by correlation strength. y-position is used to indicate variable of reference. Discriminability is exploited to clearly visualize and contextualize how correlation strength varies across each variable.

**Interaction**

Indirect manipulations
1. Year scale selection filters data for both chart 1 and 2.

**Insights**
Several training metrics are highly correlated, particularly, power draw and compute, and power draw and cost. This is also expected given the nature of the data, as some of the values for these variables were derived directly from each other by Epoch AI, when values were not reported by the model's organization.

**Critique**

Although the heatmap offers a clear visual summary of yearly correlations, the limited number of data points underpinning each estimate makes many of the correlations statistically weak or unreliable. Patterns that appear visually distinct may not meaningfully reflect underlying relationships, leading to an interpretation that is more aesthetic than substantive.

The accompanying bar chart largely reiterates the same correlation values, adding ordering but not introducing new insight. Together, the two visualizations become repetitive, and the scarcity of data prevents either from revealing meaningful differences across variables or trends over time. This limits the analytical value of the correlations and constrains the conclusions one can confidently draw.

## Summary

These themes and views enable a comprehensive understanding of how AI development has progressed across time, geography, and resource usage. 

AI development has progressed rapidly over training resources such as compute, trainable parameters, and time in hours, particularly in the deep learning era. Over time, models have been increasingly developed for multimodal tasks compared to earlier models that were task-specific, pointing to the movement towards more generalized models.

The United States has emerged as the globally dominant country in terms of model releases in the deep learning era, with China following. Notably, China produces large models in terms of compute and parameters, with low export controls on semiconductors and high AI-related academic publications.

Resource and efficiency patterns indicate that while models have become increasingly resource-intensive, they have also become more resource-efficient. Frontier models, in particular, tend to have a high level of training compute FLOPs per hour.