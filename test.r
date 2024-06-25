# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(1, 2, 3, 4, 5,  10)
res <- relativeSD(vct, 1, 10)
print(res)