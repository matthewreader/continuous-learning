# Chapter 2

This chapter briefly introduces handling exceptions with `try` , `except`, and `finally`.  However the main focus of the chapter is optimizing Python code once a workable solution to a problem has been found.  

The chapter uses two tasks as an example, finding palindromes and finding palingrams in a list of dictionary words.  We are introduced to profiling Python code using `cProfile` and using the `time.time()` function of Python to time specific sections of code.  The original solutions to finding palingrams relies on iterating through a Python list of words and takes approximately 300 seconds to complete.  However, converting the list to a set reduces runtime down to approximately one second to complete.  

As a challenge, `palindrome.py` is re-written to find palindromes recursively.  A discussion of recursion to find palindromes is given at [Khan Academy]( https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/using-recursion-to-determine-whether-a-word-is-a-palindrome/ )



