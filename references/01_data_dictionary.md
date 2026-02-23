# Data Dictionary

Data source: [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)

| Variable       | Description                              | Type    |
| :---           | :---                                     | :---    |
| `Time`         | Seconds elapsed since the first transaction | integer |
| `Vx`           | PCA result of original variables         | float   |
| `Amount`       | Transaction amount                       | float   |
| `Class`        | Target variable (1 for fraud, 0 otherwise) | integer |

In the Kaggle data description, some explanations are provided:
- for confidentiality reasons, the identifications of a good part of the original variables are not available;
- those represented as V1, V2,... V28 are the result of a principal component analysis - PCA transformation, a technique used to condense the information contained in several original variables into a smaller set of statistical variables (components) with minimal loss of information. In this work, we will see some consequences of this transformation in our analysis;
