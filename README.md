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

I used a log(x+1) link function, for the gaussian family. I used Gaussian because the 'area burned' variable is continuous, and because Central Convergence Theorem. 
