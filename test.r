# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(1, 2, 3, 4, 5,  10)
res <- maximumIPR(5, 0, 10, 8, 0.25, 0.75)
print(res)