# Meta Prisoner

We are going to revisit our prisoner's dilemma classes from the first week.
You may remember that I had you write classes that had the `__init__`, `decide`,
and `sentence` methods. You are to write a metaclass for prisoner classes that
will raise a TypeError if any of these methods are missing. 

Additionally, your metaclass should update a global variable in the `metaprisoner.py` file called `prisoners` which is a `list` of all prisoner 
classes that have been created from your metaclass.

Finally, make it so that calling `str()` on a prisoner class (not a prisoner
instance itself) returns the name of the class.

