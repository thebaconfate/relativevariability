# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(-1204988.6026813,
        -1204988.60313556,
        -1204988.6037683,
        -1204988.60367774,
        -1204988.60367732,
        -1204988.60376828,
        -1204988.60362847,
        -1204988.60356019,
        -1204988.60338437,
        -1204988.60340467)
res1 <- maximumIPR(mean(vct), min(vct), max(vct), length(vct), 0.25, 0.75)
print(res1)
