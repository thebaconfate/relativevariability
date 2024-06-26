# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(-1.05691532e+08, -1.05657153e+08, -1.05691617e+08, -1.05691616e+08,
 -1.05691615e+08, -1.05691614e+08, -1.05691613e+08, -1.05691607e+08,
 -1.05691606e+08, -1.05639786e+08)
res1 <- maximumIPR(mean(vct), min(vct), max(vct), length(vct), 0.25 * length(vct), 0.75 * length(vct))
print(res1)
