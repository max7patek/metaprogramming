# Esoteric Print Exploration

Nobody likes talking to someone who says the same thing over and over.
We're going to create a print function that prevents this.

I want to be able to instantiate one of these print functions by calling
`p = Printer(num_repeats_allowed: int)`, and then calling the print function,
like `p("Hello World")`, should print `Hello World`. It should be possible to 
print the same thing `num_repeats_allowed` times in a row, but trying to print
something for the `num_repeats_allowed + 1` times in a row should cause the
print function to print something else. Feel free to be creative with what 
happens when something is printed `num_repeats_allowed + 1` times in row, just
make sure that it prints something other than what is requested and that the
function does not hang. 

Once you have implemented your print functions, change the built-in print function
to `Printer(2)`. While doing this should only be 1 or 2 lines, it may be a little
unintuitive.
Feel free to Google as always.

You can run `runner.py` to test your implementation.

