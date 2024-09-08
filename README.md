# Replication : Principles of Principal Components Analysis (PCA)

In 2000, Salomon Smith Barney published a paper on Principal Compenent Analysis on the yield curve to weight butterfly trades.
The data we use consists of U.S. Treasury yields from 2012 to 2022, with maturities ranging from 1 month to 30 years.

The paper is divided into two parts : 
  - PCA on the yield curve
  - Structuring butterfly trades
## PCA on the Yield Curve

PCA is a dimensionality reduction technique used on large datasets, from a dataset with correlated variables we extract uncorrelated variables: principal components, which are linear combinations of the originals variables. The principal components are chosen such as the first one account for the maximum explained variance.

The main steps to compute PCA are:
  - Centering the data
  - Compute the covariance matrix of the centered data
  - Find the eigenvalues and eigenvectors of the covariance matrix

The eigenvectors are the principal components, we keep the first three higher eigenvalues.

*If we were to not know how many component to keep two main techniques exists, the first is to plot the eigenvalues in descending order and try to find an "elbow", ie a change in the decrease of the eigenvalues. The second one is to keep the eigenvalues superior to 1, because the eigenvalues of the covariance matrix stand for the amount of variance explained by the matching principal component. Thus if the value is superior to 1, the component explain more than one initial variable.*

The kept principal components describe the level shift, the slope and the curvature. 
The level shift is a global change of the yields, the slope is the change between the short term and long term maturities and the curvature is the change of the overall shape of the curve.

The cumulative explained variance of the first three components is 99.7%.

## PCA for butterfly trades

Now we want to use PCA to weight a butterfly trade, we chose the 3 following maturities 2-5-10 and rolling window between 1 to 4 years.
The third PC loadings are used to weight the trade. As the PCs are uncorrelated, the trade is in theory neutral to level shift and slope change.
We perform PCA on the selected maturities, then normalize the weights by the belly (center).
Then we do a dot product weights with yields to get butterfly spread. We plot the result to check if it's stationnary. However, as the paper is pretty old the strategy does not work anymore, the stationnarity is lost.




