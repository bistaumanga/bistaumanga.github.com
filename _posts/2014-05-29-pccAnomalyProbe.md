---
layout: post
title: Principal Component Analysis Based Unsupervised Anomaly Detection
meta: Principal Component Analysis Based Anomaly Detection
comments: true
categories: anomaly-detection
tags: anomaly principal-component-classifier PCA unsupervised
published: true
---

Unsupervised anomaly detection has its importance in the cases where we need to detect novilities from the unlabeled dataset of iids (independent and identically distributed). There has been different approaches to this problem such as Statistical Outlier Detection approaches e.g regression, gaussian density estimation, density based outlier detection e.g. [Local Outlier Factor](/blog/lof/), Kernel density estimation etc.. {% cite charuoutlier %}.

## PCA
[Principal Component Analysis](http://en.wikipedia.org/wiki/Principal_component_analysis) is a technique that transforms observations ($X \in \mathbb{R}^{n \ast d}$) of correlated variables in a higher dimensional space to the orthonormal space of uncorrelated variables. The new axis in the uncorrelated space of variables is given by **eigenvactors** and the amount of variance/energy retained along each eigenvector is given by **eigenvalues** in case of eigenvalue decomposition of **covariance matrix** of dataset. PCA can also be performed based on SVD and other decompositions.

$$
\mu_i = \frac{1}{n}\sum_{j=1}^{n}X_{ji} \ ,\ for\ each\ i = 1\ to\ d \\
C_x = Cov(X) = (X-\mu)^T(X-mu) \\
C_x = V \Lambda V^{-1}
$$

where, $n$ is number of datapoints, and $d$ is dimensionality of observations.

$V \in \mathbb{R}^{d \ast d}$ is matrix of Eigen-Vectors of $C_x \in \mathbb{R}^{d \ast d}$, and $\Lambda \in \mathbb{R}^{d \ast d}$ is a diagonal matrix of Eigen-Values of $C_x$.

$$\Lambda = \begin{pmatrix}
\lambda_1 &0  &. &. &. &0\\
0 &\lambda_2  &. &. &. &0\\
 .&  .&  .& & &.\\
 .&  .&  & .& &.\\
 .&  .&  & & .&.\\
 .&  .&  .& .& .&\lambda_n\\
\end{pmatrix} $$

and eigenvalues are sorted and maximum information are retained along earlier eigen-vectors that the later ones, i.e.

$$\lambda_1 > \lambda_2 > ... > \lambda_n $$

The percentage of energy retained in $r$ principal components after PCA transformation is given by:

$$ \%\ energy\ retained = \frac{\sum_{i=1}^{r} \lambda_i^2}{\sum_{i=1}^{d} \lambda_i^2} $$

### Dimensionality Reduction
If we pick the $r$ principal components that maintain $p\%$ variance of data, the truncated matrix of eigen-vectors is $V_L \in \mathbb{R}^{d \ast r}$, matrix of eigenvalues is $\Lambda_L \in \mathbb{R}^{r \ast r}$.

To reduce the dimensionality means to transform the data from $\mathbb{R}^{d}$ space to $\mathbb{R}^{r}$ space or to project the data into the axes given by eigen-vectors, which can be accomplished by following equation:

$$X_L = X.V_L $$

After this transform, the data will be transformed to a ortho-normal space where there is no correlation between variables.

Practically, this method often shows that dimensionality can often be reduced without much loss of information(typical choices are $1\%$, $5\%$).

I will use the concepts and try to demonstrate how they can be used to detect the **portsweep** attack in [KDD 1999]() datasets.

#### Loading the datasets

I have only selected few columns which were significant for the portsweep. These can be identified with Decision trees. ( rpart  function) or by manual inspection of ditribution of each variables for portsweep and normal data instances (boxlot(V13~V42, data = kdd)).


{% highlight r %}
type = "portsweep."
cols = c(30, 27, 33, 34, 35, 36, 5, 6, 12, 40, 23, 1)
# type = "ipsweep."
# cols = c(37, 5, 6, 32, 8, 12, 24, 31, 34, 35)
kdd <- read.csv('~/scripts/kddcup.data_10_percent', header = FALSE)
kdd.probe <- subset(kdd,V42 ==  type | V42=='normal.',
                    select=cols)
{% endhighlight %}

#### PCA with FactoMineR

I will use PCA function of package [FactoMineR]().


{% highlight r %}
require('FactoMineR')
nnn = ncol(kdd.probe) ### number of variables
pca_result <- PCA(kdd.probe,graph = F, ncp = nnn, scale.unit = T)
pca.var <- pca_result$eig[['cumulative percentage of variance']]/100
lambda <- pca_result$eig[, 'eigenvalue']

require(ggplot2)
qplot(1:length(pca.var), pca.var, ylab = "Cumulative % variance retained", xlab = "No. of Principal Components") + theme_bw() + geom_line(col = "blue") + ylim(0, 1)
{% endhighlight %}

![plot of chunk pca](/images/pcc_anomaly/pca.png)

The plot of cumulative variance retained showed we can retain the must of the infomation among the first few axes.

## Outlier Detection

PCA can not only be used as dimensionality reduction technique, but also for outlier detection. The idea behind this is, that the anomalies will not conform with the reduced sub-space pattern of most of the normal-data, i.e. the loss for the outlier will be much more larger than the most of the normal instances in the dataset when first $r$ components are picked.

### 1. $\chi^2$ Test

Charu Aggarwal [Charu pp 59] has given a more accurate way of scoring the outlierness without picking the $r$ components, but rather using eigenvectors and eigenvalues to score the outlierness as normalized distance of datapoint to the centroid along the direction of each principal components.

$$Score(X_i) = \sum_{i=1}^{d}\frac{|(X_i - \mu).V_i|^2}{\lambda_i}$$

In above relationship, the contribution of outlierness is backed by deviations from less significant principal components(with small $\lambda_i$).This value is $\chi^2$ distributed with $d$ degree of freedom.

So, an observation $X_i$ is an outlier if: $$ Score(X_i) > \chi_d^2(\alpha)$$

for $d$ degree of freedom, and $1 - \alpha$ significance level.

For giving the outlier score,we can use above equation.

{% highlight r %}
#anomaly_score <- apply(pca_result$ind$coord, 1, function(x) sum(x ^ 2/lambda))
anomaly_score = (as.matrix(pca_result$ind$coord) ^ 2) %*% (1 / as.matrix(lambda, ncol = 1))
{% endhighlight %}

KDD dataset is labeled, so let me evaluate the performance of algorithm. For that we need threshold for decision of whether an observation is outlier. Since we know that this utlier score is $\chi^2$ distributed with $d$ degree of freedom, i will perform the $\chi^2$ test with various level of significance.

{% highlight r %}
significance <- c (0.9, 0.925, 0.95, 0.96, 0.97, 0.975, 0.98, 0.985, 0.9899, 0.99, 0.991, 0.992, 0.995, 0.999)
result <- data.frame(matrix(nrow = length(significance), ncol = 4))
colnames(result) <- c('significance', 'precision', 'recall', 'F_measure')

result_expected <- subset(subset(kdd, V42 ==  type| V42=='normal.'), select=c(V42))
result_expected <- result_expected != "normal."

for(i in 1 : length(significance)){
  sig = significance[i]
  thresh = qchisq(sig, nnn)
  anomaly <- anomaly_score > thresh
  result_obtained = as.factor(anomaly)
  crosstable <- table(result_obtained, result_expected)

  tp <- crosstable[2, 2] # true_positive
  fp <- crosstable[2, 1] # false positive
  fn <- crosstable[1, 2] # false negative

  precision <- tp/(tp+fp)
  recall <- tp/(tp+fn)
  f_measure = 2 * precision * recall /(precision + recall)
  result[i, ] = c(sig, precision, recall, f_measure)
}
{% endhighlight %}

Now, i will plot the evaluation measures against the level of significance in $\chi^2$ test.

{% highlight r %}
p = ggplot(result, aes(x = significance)) +
  geom_line(aes(y = recall, col = "recall", fill = "recall"),
            lwd = 1, lty = 'longdash') +
  geom_point(aes(y = recall, col = "recall", shape = "recall"), size = 3)+
  geom_line(aes(y = F_measure, col = "F-measure", fill = "F-measure"),
            lwd = 1, lty = 'dotdash') +
  geom_point(aes(y = F_measure, col = "F-measure", shape = "F-measure"), size = 3)+
  geom_line(aes(y = precision, col = "Precision", fill = "Precision"),
            lwd = 1, lty = 'solid') +
  geom_point(aes(y = precision, col = "Precision", shape = "Precision"), size = 3)+
  theme_bw()+
  xlab("Significance $1 - \alpha$") + ylab("") +
  scale_colour_manual(name="", values = c(2, 3, 4))+
  scale_shape_manual(name="", values = c(15, 17, 18))
print(p)
{% endhighlight %}

![plot of chunk results](/images/pcc_anomaly/results.png)

We can see the algorithm performs poorly, especially in terms of Precision, which means a lot of False alarm are generated. We would like to improve on this, for this we will explore the **Principal component Classifier method**.

### 2. Principal Component Classifier (PCC)

PCC was first introduced by Shyu et. al.{% cite pcc-anomaly%}. They divided the principal components into two categories: **Major Components** which account for first $q\%$ of variance, and minor components, which accountfor the last $r\%$ of variance of the data.

To Be continued...


References
--------------
{% bibliography --cited %}
{: style="font-size:12pt; text-align:left;"}
