The premise of this project is analyzing forest fire related data provided by the UC Irvine Machine Learning Repository 
http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv'

Citation:
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

A description of the dataset can be found at:
https://archive.ics.uci.edu/ml/datasets/Forest+Fires

Source:
Paulo Cortez, pcortez '@' dsi.uminho.pt, Department of Information Systems, University of Minho, Portugal.
Aníbal Morais, araimorais '@' gmail.com, Department of Information Systems, University of Minho, Portugal. 

Citation:
[Cortez and Morais, 2007] P. Cortez and A. Morais. A Data Mining Approach to Predict Forest Fires using Meteorological Data. In J. Neves, M. F. Santos and J. Machado Eds., New Trends in Artificial Intelligence, Proceedings of the 13th EPIA 2007 - Portuguese Conference on Artificial Intelligence, December, Guimarães, Portugal, pp. 512-523, 2007. APPIA, ISBN-13 978-989-95618-0-9. Available at: [Web Link]

So far I am using the glm() function in the R programming language. Starting with a null model with no predictors and stepping forward, algorithm does not converge. Starting with model with all non-mixed first order terms doesn't converge. Interestingly stepping backward, algorithm removes rain and wind from model. Perhaps the various indeces take rain and wind into consideration, so I will look into those.

I used a log(x+1) link function, for the gaussian family. I used Gaussian because the 'area burned' variable is continuous, and because Central Convergence Theorem. Using log is suggested in the dataset description site, and it is mentioned that log(x+1) was used "In [Cortez and Morais, 2007], the output 'area' was first transformed with a ln(x+1) function.". When I say log() I mean the natural log, ln().

Removed various indeces from full model in stepwise.R (I still haven't looked into their meanings). This resulted in convergence (to the same thing) in 'backward' and 'both' directions. The reported model is approximately:
E[log(area+1)] = -0.95 + 0.18 X + 0.10 temp + 0.15 wind,
where E[x] is the expected value for x.

The reported test statistics are:
Null Deviance:	    2091000 
Residual Deviance: 2040000 	AIC: 5758

pchisq(2091000-2040000,3) gives 1, meaning with 100% confidence the model is better than null. 
pchisq(2091000,4) gives 1, meaning with 100% confidence the saturated model (descriptor for each data point) is better than our model.

For now I'm done using R, I will switch to Python. Ideas: try doing the same linear regression, but with Python; try using sci-kit learn, pytorch, and tensorflow.
