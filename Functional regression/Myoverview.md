## My overview

## 2015 BOOK

comparision of differente sites* (2h)

- **Electricity Consumption Forecasting by Pattern Recognition Using Load Curve Clustering**
  - clustering techniques: K-means and Self-organizing Maps (SOM)
- **Electricity Consumption Forecasting by Signal Decomposition Using Principal Component Analysis **[^1]
  - A multiple linear regression is used in order to find the coefficients for the principal components

adjustment factors ：

- scalar 
- additive

### Performance Indicator

- Mean Absolute Percentage Error (MAPE）

- Mean Squared Error (MSE)

These indicators are adapted to situations where the goal is to optimize the use of production means to meet an electricity demand,or residual demand curves calculation in competitive electricity markets.

- a specific performance criterion： rewarded or penalized economically

  **Gross EnergyDeviation**

### Visualization

![屏幕快照 2018-11-18 下午9.35.30](/Users/bailujia/Desktop/屏幕快照 2018-11-18 下午9.35.30.png)

Conclusion:

Method1>Method2

selection of hour does not influence the performance of different methods(1 2)

[^1]: José Blancarte, Mireille Batton-Hubert, Xavier Bay, Marie-Agnès Girard, and Anne Grau . "Short Term Load Forecasting in the Industryfor Establishing Consumption Baselines:A French Case"

--------



**Curve Linear Regression via Dimension Reduction** 49

(curve to curve)

Based on the vast knowledge on French electricity consumption patterns
accumulated over 20 years, EDF has developed a forecasting model which consists of complex regression models based on past loads, temperature, date and calendar events, coupled with classical time series models such as the seasonal ARIMA (SARIMA) [4].This operational model performs very well, attaining about 1.4 % mean absolute percentage error (see (8)) in forecasting the consumption of EDF customers over one day horizon



Cho et al. [6] 

- Modelling the overall trend and seasonality in the data by fitting a generalised additive model (GAM) to the weekly averages of the load, with meteorological factors (e.g., temperature and nebulosity) as explanatory variables; 
- Modelling the dependence across successive, de-trended daily loads via curve linear regression, where both the response and the regressor are functional (curves), with the load curve on the next day as the response and that on the current day, jointly with the temperature forecast, as the regressor. 



curve linear regression functional y ~ functional x SVD

two classification rules

#### Fully Nonparametric Short Term Forecasting Electricity Consumption

not functional

iterative bias reduction approach

functional nonparametric model

non-linear additive autoregressive approach 

 ##### background:

Such data are available on RTE webpage (www.rte-france.
com). Annual consumption patterns are usually explained by seasonal change in climate (temperature, cloud cover) and daylight duration.

- RTE “corrects” the half hourly load curve by modeling the impact of climate and prices, in order to work on a time series that doesn’t depend on exogenous variables. This first step is done by using a regression model with dependent variables based on climate and tariff. We denote the corrected series by Zt. 

- RTE uses a SARIMA model to forecast Zt at the horizon H:



- RTE adds the forecasts given in Step 2 with the estimation given by the regression model using prices and forecasts for the temperature and cloud cove 


- Addtive models:

  - AR: curse of dimensionality

    $Z_t =f(Z_{t-􏱿1},...,Z_{t_􏱿p})+\epsilon_t$

    $Z_t =f(Z_{t-􏱿1})+,...,+f(Z_{t_􏱿p})+\epsilon_t$

- adaptive nonparametric regression method



####Forecasting Intra Day Load Curves Using Sparse Functional Regression

More precisely,
the prediction box is built using successive learning procedures: elaboration of a
data base of historical scenarios organized on a high dimensional and functional
learning of the intra day load curves, construction of expert forecasters using a
retrieval information task among the scenarios, final aggregation of the experts.

Note that LOLA is an algorithm providing good sparse approximation in very
high dimension (see [17] in the case of the intra day load curve) and very accurateselection properties in medium high dimension (see [16]), which is the case here
(p D 14).

##2014 Book Topics in Nonparametric statistics

#### Chapter 11 Peak-Load Forecasting Using a Functional
Semi-Parametric Approach
flexible semi-parametric approach based on the Projection Pursuit Regression idea

The terms of such decomposition are estimated
with a procedure which combines a spline approximation and the one-dimensional Nadaraya–Watson approach.

![屏幕快照 2018-11-20 下午2.12.50](/Users/bailujia/Desktop/屏幕快照 2018-11-20 下午2.12.50.png)

![屏幕快照 2018-11-20 下午2.12.52](/Users/bailujia/Desktop/屏幕快照 2018-11-20 下午2.12.52.png)