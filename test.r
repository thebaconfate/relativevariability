# install.packages("devtools", repos = "http://cran.us.r-project.org")
# install.packages("httpgd", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

vct <- c(-1174559.36404975, -1173890.54863387, -1173042.80477426, -1174782.2274112,
 -1175053.33452611, -1174971.7337945,  -1174968.8788993,  -1168536.42858289,
 -1165737.48082844, -1175053.3337175)
res1 <- maximumIPR(mean(vct), min(vct), max(vct), length(vct), 0.25, 0.75)
print(res1)
