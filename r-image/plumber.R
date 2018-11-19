# plumber.R

#* Test Entry Point
#* @get /test_entry
function() {
  "Test R server is up and running"
}

#* Soring entry point
#* @post /
function(){
  output <- list(
    model_id = "r_model_1",
    score = 0.8775687
  )

  return (output)
}
