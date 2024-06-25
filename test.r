# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(1, 2, 3, 4, 5,  10)
res1 <- maximumIPR(-0.0242820291, -0.0242839492
, -0.0242813473
, 2, 0.0000050425, 0.0000050429)
print(res1)
print(-20)