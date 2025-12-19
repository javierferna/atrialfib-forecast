# Atrial Fibrillation Forecast

This repository contains the source code and analysis for the final project **“Forecasting Intracardiac Electrograms to Identify Arrhythmic Activity in Atrial Fibrillation”**, developed as part of the **Machine Learning in Healthcare** course at **Universidad Carlos III de Madrid (UC3M)**, in collaboration with Gonzalo Ríos (Department of Bioengineering).

The project applies machine learning forecasting techniques to predict the temporal evolution of intracardiac electrogram (EGM) signals. The core hypothesis is that signals with high prediction error correspond to active arrhythmic drivers or complex fractionated atrial electrograms (CFAEs), while more predictable signals indicate healthy, passively activated tissue.

## Dataset
The analysis uses discrete-time EGM recordings from multiple patients undergoing ablation procedures.

- **Sampling frequency:** 500 Hz.
- **Duration:** 2.5 seconds per recording (1250 samples).
- **Observation window:** 2.0 seconds (model input).  
- **Prediction horizon:** 0.5 seconds (model target).

## Methodology

Signals are centered by subtracting the mean of the observation window to enforce weak stationarity. Principal Component Analysis (PCA) was explored for dimensionality reduction.

### Modeling Approaches
Both deep learning and classical time-series models are evaluated:

1. **Deep Learning Baselines**
   - GRU and LSTM networks. 
   - Sequence-to-Sequence models with attention.  

2. **Autoregressive Models**
   - **AR(p):** Estimated using Yule-Walker and Least Squares.  
   - **ARIMA(p, d, q):** Handles non-stationarity via differencing and moving average terms.  
   - **TVAR:** Time-Varying AR model using Recursive Least Squares with Kalman filtering. 

### Anomaly Detection
Normalized Mean Squared Error (NMSE) is proposed as a biomarker of tissue complexity:

- **NMSE < 1:** Organized, predictable tissue.  
- **NMSE > 1:** Chaotic, unpredictable activity and potential ablation targets.  

## Results
- **Forecasting:** Both deep learning and AR-based models struggle with long-horizon spike prediction (0.5 s), often reverting to the mean after ~100 ms.  
- **Biomarker validation:** NMSE effectively differentiates organized signals from fractionated ones.  
- **Clinical relevance:** Electrodes in the top 10% by prediction error emerge as candidate ablation sites, corresponding to regions of high signal complexity.
