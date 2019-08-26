# stepwise.R
# author: seth briney
# -\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-
# ###########################################
# The purpose of this script is to perform generalized
# linear regression on forestfire data
# Using glm step functions does not appear to be of much use
# either moving forward from null model, or steping
# backward from full model (all homogenous first terms)

# https://www.rdocumentation.org/packages/stats/versions/3.6.1/topics/glm
# glm.fit is the workhorse function: it is not normally called directly but can be more efficient where the response vector, design matrix and family have already been calculated.
# "X","Y","month","day","FFMC","DMC","DC","ISI",
# "temp","RH","wind","rain","area" 
forestfire_data = read.csv("forestfires.csv",header=TRUE)
# jpeg(file="plot_forestfire_data.jpeg")
# plot(forestfire_data,col='darkgreen',pc='.')
## Note DC and DMC appear close to linear dep, maybe don't use both in model.
# dev.off()
# converting months to integers

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
    X+Y+month+FFMC+DMC+DC+ISI+temp+RH+wind+rain, family=gaussian(link=log),data=forestfire_data)
# Coefficients:
# (Intercept)            X            Y     monthaug     monthdec     monthfeb  
#     42.2766       1.0777       1.1956      50.4205      34.9012      10.7710  
#    monthjan     monthjul     monthjun     monthmar     monthmay     monthnov  
#     47.8388      16.7824      16.1480     -12.6351      22.8416      14.1294  
#    monthoct     monthsep         FFMC          DMC           DC          ISI  
#     93.5486      68.6529      -0.4986       0.2866      -0.1572      -0.4137  
#        temp           RH         wind         rain  
#      0.2071      -0.8250       2.8181       5.6578  

# backwards=step(full_model,direction='backward')
# Start:  AIC=5662.48
# area + 1 ~ X + Y + month + FFMC + DMC + DC + ISI + temp + RH + 
#     wind + rain

#         Df Deviance    AIC
# - DMC    1   954547 5399.5
# - wind   1   954835 5399.7
# - RH     1   979521 5412.9
# - month 11  1628037 5655.5
# - X      1  1575923 5658.7
# - temp   1  1581050 5660.4
# - rain   1  1581440 5660.5
# - FFMC   1  1581820 5660.6
# - ISI    1  1582130 5660.7
# <none>      1581306 5662.5
# - DC     1  1590190 5663.4
# - Y      1  1835635 5737.6

# Step:  AIC=5399.51
# area + 1 ~ X + Y + month + FFMC + DC + ISI + temp + RH + wind + 
#     rain

#         Df   Deviance     AIC
# - rain   1 9.5453e+05  5397.5
# - temp   1 9.5455e+05  5397.5
# - X      1 9.5467e+05  5397.6
# - wind   1 9.5491e+05  5397.7
# - FFMC   1 9.5523e+05  5397.9
# <none>     9.5455e+05  5399.5
# - RH     1 9.7519e+05  5408.6
# - ISI    1 1.6180e+06  5670.3
# - DC     1 1.9445e+06  5765.4
# - month 11 3.3591e+07  7218.4
# - Y      1 2.4410e+17 18977.7

# Step:  AIC=5397.5
# area + 1 ~ X + Y + month + FFMC + DC + ISI + temp + RH + wind

#         Df   Deviance     AIC
# - temp   1 9.5469e+05  5395.6
# - X      1 9.5480e+05  5395.7
# - wind   1 9.5505e+05  5395.8
# - FFMC   1 9.5538e+05  5396.0
# <none>     9.5453e+05  5397.5
# - RH     1 9.7533e+05  5406.6
# - month 11 1.6279e+06  5651.5
# - ISI    1 1.6182e+06  5668.4
# - DC     1 1.9444e+06  5763.4
# - Y      1 2.6193e+14 15440.9

# Step:  AIC=5395.59
# area + 1 ~ X + Y + month + FFMC + DC + ISI + RH + wind

#         Df Deviance    AIC
# - wind   1   955180 5393.9
# - X      1   955389 5394.0
# - FFMC   1   955398 5394.0
# <none>       954690 5395.6
# - Y      1   964608 5398.9
# - month 11  1627903 5649.5
# - ISI    1  1620586 5667.2
# - DC     1  1972213 5768.7
# - RH     1  2045874 5787.6

# Step:  AIC=5393.86
# area + 1 ~ X + Y + month + FFMC + DC + ISI + RH

#         Df Deviance    AIC
# - FFMC   1   955492 5392.0
# <none>       955180 5393.9
# - Y      1   965936 5397.6
# - X      1  1537023 5637.8
# - month 11  1630042 5648.2
# - DC     1  2005533 5775.3
# - ISI    1  2012900 5777.2
# - RH     1  2052127 5787.2

# Step:  AIC=5392.02
# area + 1 ~ X + Y + month + DC + ISI + RH

#         Df Deviance    AIC
# <none>       955492 5392.0
# - X      1  1654449 5673.9
# - month 11  2037756 5761.6
# - DC     1  2012432 5775.1
# - ISI    1  2013446 5775.4
# - Y      1  2025682 5778.5
# - RH     1  2061212 5787.5
# There were 31 warnings (use warnings() to see them)
# > backwards

# Call:  glm(formula = area + 1 ~ X + Y + month + DC + ISI + RH, family = gaussian(link = log), 
#     data = forestfire_data)

# Coefficients:
# (Intercept)            X            Y     monthaug     monthdec     monthfeb  
#    -20.9047       1.8900      17.8590      65.8302      79.1038     -85.0384  
#    monthjan     monthjul     monthjun     monthmar     monthmay     monthnov  
#     29.8956       6.7313      48.7607     -26.1632      44.7588      26.1792  
#    monthoct     monthsep           DC          ISI           RH  
#    177.3435     221.0480      -0.3582      -3.1911      -0.9182  

# Degrees of Freedom: 516 Total (i.e. Null);  500 Residual
# Null Deviance:      2091000 
# Residual Deviance: 955500   AIC: 5392

# forward=step(null_model,direction='forward')
# > source('stepwise.R')
# Start:  AIC=5764.89
# area + 1 ~ 1

# Warning message:
# glm.fit: algorithm did not converge 
