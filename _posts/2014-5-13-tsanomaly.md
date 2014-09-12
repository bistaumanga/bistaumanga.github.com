---
layout: post
title: Robust Statistic based Streaming Anomaly Detection Scheme for Time-Series Data
meta: Robust Statistic based Streaming Anomaly Detection Scheme for Time-Series Data
comments: true
category: anomaly-detection
tags: robust-statistic, anomaly-detection, time-series, streaming-algorithm
---

Identifying the anomalous observations in time series data can be very important for [SIEM][siem] solutions. An example is a system that tracks the records of number of user-logins per minute. The anomalous entries in this case can be when the count becomes unexpecteadly higher or lower than normal trend.

This can be detected by simpler approach such as standard deviation method, i.e. an entry in time-series is anomaly when its not in range **$ [\mu - k * \sigma, \mu + k * \sigma] $**. The typical value of **$ k $** is **3, 3.5, 4**, which has to be set manually. There are three problems with this approach. The problems and the possible solutions are enumerated below:

<div class="alert alert-danger" role="alert">the statistics $ \mu $ and $ \sigma $ both are not robust, outliers have huge affect on them.</div>

> We have to use roubust statistics such as **$ M_d $**:[Median], **$ IQR $** :[Inter Quartile Range], in favour of **$ \mu $** and **$ \sigma $**. The time series should be smoothened by **[causal][causal]** version of **Moving Median** or **Causal 1-D Moving Median Filter**.

<div class="alert alert-danger" role="alert">It does not captures the trend, i.e. What if the distribution of the time-series data is  multimodal.</div>

> We have to capture the trend. One way to do this is smooth the time series signal, and model the residual for anomaly detection. The residual will have $ \mu = 0 $ and some standard deviation.

![center](/images/tsanomaly/residual_plot.png)

<div class="alert alert-danger" role="alert">Anomalous time-series entries have to be identified in real-time, so we cannot use batch algorithms that calculates the parameters *$ \mu, \sigma $* in first pass and filters out the anomalous data in second pass. But this can be solved by streaming algorithm for $ \mu, \sigma $ {% cite knuth2 -l 232 %}.</div>

> But since we are using robust statistics *$ [M_d, IQR] $*, we have to use streaming version of that. Luckily, there exist an awesome algorithms for this : **QDigest** {% cite qdigest %} and **TDigest** {% cite tdigest %}.

Using these concepts to decide whether a data from real-time is an anomaly or not, we first predict
the value using Causal Moving Median algorithm. Then the residual, which is a difference between predicted and observed value is used to compute the Streaming $ M_d,  IQR $. These Robust statistics are used to estimate the robust $ \mu , \sigma $ using Equations [[wiki : Robust Scale Estimation][wikiRobustStddev]]:

$$
\mu = M_d \\
\sigma = 0.74 * IQR
$$

With these estimates for robust mean and standard deviation, we will calculate the two-tailed $p-value$ as :

$$ p_{value} = 1 - Erf \frac{\mid residual - \mu  \mid}{\sqrt{2\sigma^2}} $$

and we can give the score to anomalous entries as {% cite pvalprelert %}:

$$ anomaly\_score = - \log{p_{value}} $$

<!--- So, Let us use overall Discussion to sketch an algorithm for real time Anomaly Detection in time-series data.
![png](/files/tsanomaly/algorithm.png) -->

Results
--------
Here are the results of algorithm for time series datasets with

#### Trend
![center](/images/tsanomaly/trend.png)

#### Seasonality
![center](/images/tsanomaly/sin.png)

#### Trend and Seasonality
![center](/images/tsanomaly/sintrend.png)

#### Level Shift
![center](/images/tsanomaly/shift.png)

The results shows that the algorithm was able to detect the anomalous entries in a time series with trend or seasonality or both or Level shifts.


References
--------------
{% bibliography --cited %}
{: style="font-size:12pt; text-align:left;"}

[siem]: http://en.wikipedia.org/wiki/Siem
[causal]: http://en.wikipedia.org/wiki/Causal_system
[wikiRobustStddev]: http://en.wikipedia.org/wiki/Robust_measures_of_scale#Estimation