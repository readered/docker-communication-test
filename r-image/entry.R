library(plumber)
r <- plumb('./r-image/plumber.R')
r$run(host='0.0.0.0', port=8000)
