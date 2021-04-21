#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

fizzBuzz <- function(n) {
  # This seemed like a silly way to print results to the console, but
  # was the only way I could get Hacker Rank to accept my solution.
  for (i in 1:n) {
    
    if ( (i %% 5 == 0) & (i %% 3 == 0) ) {
      cat("FizzBuzz\n")
    } 
    
    else if ( (i %% 5 != 0) & (i %% 3 == 0) ) {
      cat("Fizz\n")
    }
    
    else if ( (i %% 5 == 0) & (i %% 3 != 0) ) {
      cat("Buzz\n")
    }
    
    else {
      cat(paste0(i), "\n")
    }
  }
  
}