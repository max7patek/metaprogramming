# Meta Prisoner

We are going to revisit our prisoner's dilemma classes from the first week.
You may remember that I had you write classes that had the `__init__`, `decide`,
and `sentence` methods. You are to write a metaclass for prisoner classes that
will raise a TypeError if any of these methods are missing. Additionally, your
metaclass should have a static/class attribute (see `_instances` from the
singleton example for an example of a static/class attribute) called
`prisoner_types` which is a `list` of all prisoner classes that have been
instantiated from your metaclass.
