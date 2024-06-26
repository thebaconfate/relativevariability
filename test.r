# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(
        -866609.33460983,
        -1003107.25543884,
        -1003106.25543884,
        -1003105.25543884,
        -1003104.25543884,
        -1003103.25543884,
        -379139.69127295,
        -1087199.8915076,
        -1097723.9591862,
        -1093871.90226563)
res1 <- maximumIPR(mean(vct), min(vct), max(vct), length(vct), 0.25 * length(vct), 0.75 * length(vct))
print(res1)
