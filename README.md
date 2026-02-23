# Yes Bank Stock Price Prediction ML Project

## 📈 Project Overview

This project analyzes Yes Bank's historical stock price data from **2005 to 2020** and implements machine learning models for stock price prediction. The analysis includes comprehensive Exploratory Data Analysis (EDA) with 11 professional visualizations and statistical insights.

## 📊 Dataset Information

- **Time Period**: July 2005 - November 2020 (185 monthly observations)
- **Features**: Open, High, Low, Close prices + engineered Price_Spread
- **Data Quality**: Perfect dataset with no missing values or duplicates
- **Price Range**: ₹5.55 (crisis low in 2020) to ₹404.00 (peak in 2018)

## 🔍 Key Findings

### Statistical Analysis
- **Exceptionally Strong Correlations**: All features show >97% correlation with Close price
- **Right Skewed Distributions**: All price metrics are positively skewed (>1.2)
- **High Volatility Periods**: 2018-2020 banking crisis with 8x normal volatility

### Time Series Insights  
- **Growth Period**: Steady rise from ₹13 (2005) to ₹404 (2018)
- **Banking Crisis**: Dramatic collapse from ₹404 to ₹5.55 (2018-2020)
- **Recovery Signals**: Gradual price recovery visible in late 2020

## 📁 Project Structure

```
yes_bank_project/
├── data/
│   └── data_YesBank_StockPrices.csv    # Historical stock price data
├── notebooks/
│   ├── 1_EDA.ipynb                     # Complete exploratory data analysis
│   └── 2_ML_Model.ipynb                # Machine learning model development
├── outputs/
│   ├── boxplot_outliers.png            # Outlier analysis
│   ├── correlation_heatmap.png         # Feature correlation matrix
│   ├── monthly_returns.png             # Monthly return patterns
│   ├── pairplot.png                    # Pairwise relationships
│   ├── price_spread.png                # Volatility over time
│   ├── rolling_averages.png            # Trend smoothing
│   ├── scatter_vs_close.png            # Feature vs target relationships
│   ├── skewness_chart.png              # Distribution skewness
│   ├── time_series_full.png            # Complete price history
│   ├── univariate_boxplots.png         # Individual feature distributions
│   └── univariate_distributions.png    # Histogram + KDE analysis
├── requirements.txt                     # Python dependencies
├── test_imports.py                      # Library verification script
└── README.md                           # Project documentation
```

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/avidada35/YesBank_Internship.git
cd YesBank_Internship
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
python test_imports.py
```

## 📚 Dependencies

- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly, missingno
- **Machine Learning**: scikit-learn, xgboost, lightgbm, catboost
- **Statistical Analysis**: scipy, statsmodels
- **Technical Analysis**: ta (financial indicators)
- **Model Tools**: shap, lime, optuna, joblib
- **Jupyter Environment**: jupyter, ipython, ipywidgets

## 🔬 Analysis Highlights

### Correlation Analysis
- **Low vs Close**: 0.9954 (strongest predictor)
- **High vs Close**: 0.9851
- **Open vs Close**: 0.9780
- **Conclusion**: Perfect linear relationships for regression modeling

### Volatility Analysis
- **Average Spread**: ₹21.16 monthly
- **Maximum Volatility**: ₹183.85 (Sep-2018)
- **Crisis Impact**: 2018-2020 period shows extreme price swings

### Distribution Patterns
- **All features are right-skewed** indicating concentration at lower prices
- **Outliers present** during high-price periods (2017-2018)
- **Non-normal distributions** suggest potential for data transformation

## 📈 Visualizations Created

1. **Outlier Detection** - IQR method boxplots
2. **Distribution Analysis** - Histograms with KDE overlays  
3. **Correlation Matrix** - Feature relationship heatmap
4. **Pairplot Analysis** - All feature relationships
5. **Scatter Plots** - Feature vs target with regression lines
6. **Time Series** - Complete price history with crisis annotations
7. **Volatility Analysis** - Monthly price spread over time
8. **Returns Analysis** - Monthly percentage changes
9. **Trend Analysis** - Rolling averages (3-month, 12-month)
10. **Skewness Analysis** - Distribution shape analysis
11. **Individual Boxplots** - Feature-wise outlier analysis

## 🎯 Model Readiness

### Why Linear Regression is Ideal:
- **Exceptional correlations** (>97% with target)
- **Clear linear relationships** in scatter plots
- **Strong predictive power** from all features
- **Clean dataset** with no missing values
- **Sufficient historical data** (185+ observations)

### Potential Improvements:
- **Log transformation** for skewed distributions
- **Feature engineering** with technical indicators
- **Time series models** for temporal patterns
- **Ensemble methods** for robustness

## 👨‍💼 Business Impact

### Investment Insights:
- **Long-term growth potential** despite crisis periods
- **High volatility** creates both risk and opportunity  
- **Recovery patterns** visible in recent data
- **Technical analysis** supports trend predictions

### Risk Assessment:
- **Banking sector sensitivity** to regulatory changes
- **Market volatility** during crisis periods
- **External factors** significantly impact price movements

## 📧 Contact

**Author**: Aviraj Umesh Virape  
**Project**: Yes Bank Stock Price Prediction  
**Date**: February 2026  

---

## 📄 License

This project is for educational and internship purposes. Dataset and analysis are for learning machine learning applications in financial markets.

## 🙏 Acknowledgments

- Yes Bank for publicly available historical data
- Python data science community for excellent libraries
- Financial analysis techniques from quantitative finance literature