# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(
        -44321.78599591,
        -44321.60904952,
        -44321.81134293,
        -44321.7241855,
        -44321.56522732,
        -44321.80898201,
        -44321.58418848,
        -44315.26797085,
        -44321.82650764,
        -44321.28162627)
res1 <- maximumIPR(mean(vct), min(vct), max(vct), length(vct), 0.01 * length(vct), 0.99 * length(vct))
print(res1)
