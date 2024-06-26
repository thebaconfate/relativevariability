# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(
        -8.99558082e07,
        -1.04134412e08,
        -1.04134411e08,
        -1.04134410e08,
        -1.04134409e08,
        -1.04134408e08,
        -3.93571899e07,
        -1.12862539e08,
        -1.13954509e08,
        -1.13548355e08)
res1 <- maximumIPR(mean(vct), min(vct), max(vct), length(vct), 0.25 * length(vct), 0.75 * length(vct))
print(res1)
