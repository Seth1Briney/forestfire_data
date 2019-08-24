# stepwise.R
# author: seth briney
# -\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-
# ###########################################

# "X","Y","month","day","FFMC","DMC","DC","ISI",
# "temp","RH","wind","rain","area" 
forestfire_data = read.csv("forestfires.csv",header=TRUE)
# jpeg(file="plot_forestfire_data.jpeg")
# plot(forestfire_data,col='darkgreen',pc='.')
## Note DC and DMC appear close to linear dep, maybe don't use both in model.
# dev.off()
# converting months to integers
months=as.matrix(forestfire_data['month'])
match(months, tolower(month.abb))
for (n in c(1:length(months))){
    months[n]=match(months[n],tolower(month.abb))
}
months=as.numeric(c(months))
# months are now 1-12 rather than 'jan'-'dec'

# note: data source suggested using log link. Gaussian becaue central convergence theorem.
# model = glm( area+1 ~ temp, family=gaussian(link=log),data=forestfire_data)
# E[log(area+1)] = a*temp + b
# Coefficients:
# (Intercept)         temp  
#     1.06727      0.07798  

# Degrees of Freedom: 516 Total (i.e. Null);  515 Residual
# Null Deviance:      2091000 
# df=1, seth
# Residual Deviance: 2069000  AIC: 5761
# df=2, seth
# The high residual indicates this is a bad fit compared with saturated model.

# model = glm( area+1 ~ temp, family=gaussian(link=log),data=forestfire_data)
# > pchisq(22000,1)
# [1] 1
# with 100% confidence the model is better than nothing (null)

# model = glm( area+1 ~ temp, family=gaussian(link=identity),data=forestfire_data)
# Coefficients:
# (Intercept)         temp  
#      -6.414        1.073  
# Degrees of Freedom: 516 Total (i.e. Null);  515 Residual
# Null Deviance:      2091000 
# Residual Deviance: 2071000  AIC: 5762
# Lower AIC mean more parsimonious fit. AIC=-2log(likelihood)+k num_params
# By AIC this model is slightly worse, as also indicated by the larger residual.

# model = glm( area+1 ~ temp, family=gaussian(link=log),data=forestfire_data)
null_model = glm( area+1 ~ 1, family=gaussian(link=log),data=forestfire_data)
full_model = glm( area+1 ~
    X+Y+months+FFMC+DMC+DC+ISI+temp+RH+wind+rain, family=gaussian(link=log),data=forestfire_data)
# Note months is numerical, and not in forestfire_data.
# Coefficients:
# (Intercept)            X            Y       months         FFMC          DMC  
#  -54.003558     1.774341    -0.727084     1.077763     0.614230     0.087741  
#          DC          ISI         temp           RH         wind         rain  
#   -0.020531    -0.005603    -0.237197    -0.722981     0.997367     3.943085  

# Degrees of Freedom: 516 Total (i.e. Null);  505 Residual
# Null Deviance:      2091000 
# Residual Deviance: 1622000  AIC: 5656
# Warning message:
# glm.fit: algorithm did not converge

backwards=step(full_model,direction='backward')