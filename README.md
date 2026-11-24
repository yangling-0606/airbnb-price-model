# Airbnb business case: price drivers and a price model

Data analytics business case for Siemens Advanta. The data is 51,707 Airbnb listings from 10 European cities.

## Guiding questions
1. **Correlation analysis:** which attributes go together, and how strongly?
2. **Predictive modelling:** what drives the price, and how can Airbnb use a price model in its operations and strategy?

## Files
| File | Content |
|---|---|
| `code/01_eda_correlation.ipynb` | Data checks, price distribution, Spearman correlations, by city, quality vs price |
| `code/02_price_model.ipynb` | Price model (linear regression, random forest), cross-validation, tuning, test score, importance, fair-price check |
| `code/common.py` | Loading and cleaning of the data, chart style and colours |
| `data/` | The two files from Siemens: the data and the data catalogue |
| `outputs/figures/` | The charts, saved by the notebooks |

## Run it
Python 3.11 or newer.

```bash
pip install -r requirements.txt
```

The two files from Siemens are in the `data/` folder:
- `Case 1 - Airbnb Dataset.csv`
- `Data Catalogue - Case 1 Airbnb Dataset.xlsx`

Then open the notebooks in the `code` folder and run them from top to bottom, 01 first.

## Main results
- The city, the room type and size, and the neighbourhood attraction index carry most of the price.
- Guest ratings hardly relate to price.
- The tuned random forest has a typical error of about 12% on listings it has never seen. A straight-line model is off by about 21%.
