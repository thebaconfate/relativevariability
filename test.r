# install.packages("devtools", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
res <- maximumVAR(mean(vct), 1, 10, length(vct))
print(res)