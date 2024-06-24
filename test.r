# install.packages("devtools", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
vct_mean <- mean(vct)
print(maximumVAR(vct_mean, 1, 10, 10))
vct <- c(0, 1)
vct_mean <- mean(vct)
print(maximumVAR(vct_mean, 0, 1, 2))

vct <- c(-10, -9, -8, -7, -6, -5, -4, -3, -2, -1)
vct_mean <- mean(vct)
print(maximumVAR(vct_mean, -10, -1, 10))

vct <- c(-1, 6, 8, -6, -10, 9, 2, 6, 2)
vct_mean <- mean(vct)
print(maximumVAR(vct_mean, -10, 9, 9))