# install.packages("devtools", repos = "http://cran.us.r-project.org")
library(devtools)
# install_github("seanchrismurphy/relativeVariability")
library(relativeVariability)

xParts <- c(c(1, 2, 3, 4), c(5, 6, 7, 8), c(9, 10, 11, 12))

n <- 0
output <- 0
for (i in (1:(length(xParts)))) {
  print("first:")
  print(xParts[[i]])
  if (length(xParts[[i]]) > 1) {
    for (j in (1:(length(xParts[[i]]) - 1))) {
      print("second:")
      print(xParts[[i]][j])
      output <- output + (xParts[[i]][j + 1] - xParts[[i]][j])^2
      n <- n + 1
    }
  }
}

x <- c(1, 2, 3, 4, NA, 6, 7, 8, 9, 10, 11, 12)
add_temp <- 0
n_part_add <- 1
n_parts <- c()
print("nParts:")
print(n_parts)
for (i in (1:(length(x)))) {
  if (is.nan(x[i]) == 0)  {
    add_temp <- add_temp + 1
  } else if (add_temp > 0) {
    n_parts[nPartAdd] <- add_temp
    n_part_add <- nPartAdd + 1
    add_temp <- 0
  }
}

print("nParts:")
print(n_parts)


# print(sum(!is.na(c(1, 2, 3, 4, NA, 6, 7, 8, 9, 10, 11, 12))))


r <- c(1, 2, 3, 4, 5, NA, 10, 8)

MSSD <- function(X) {
  differences <- diff(X)
  differences <- differences[!is.na(differences)]
  differences <- differences ^ 2
  MSSD <- mean(differences)
  return(MSSD)
}

print(MSSD(r))