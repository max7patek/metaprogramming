# Problem Generator

This is a group assignment with groups no larger than 5.
Comment the computing IDs of your group members at the top of your .java file.
Only one team member has to sumbit.

You should use the JavaPoet library to complete this assignment.
You can download the .jar [here](https://mvnrepository.com/artifact/com.squareup/javapoet/1.11.1).
You can see the documentation [here](https://github.com/square/javapoet).
Also, see the example solutions under [examples](examples).

For this Java program you will write, the user is an exam-maker.
The exam maker wants to be able to automatically generate exam problems in the
form "What is printed by the following code? <insert code here> ".

Your program should accept user input for what should be printed (ie what the
answer to the problem should be). The program should then output some Java code
that prints that String (the problem). The harder the problem is, the better.
The problem should still be solvable by hand in a reasonable amount of time.

If your problem takes in a specific type of answer (for example, if your type
of problems only print ints), then you should throw an IllegalArgumentException
if the input is not in that form.

Make sure to comment your code with an explanation for what your problems test.
