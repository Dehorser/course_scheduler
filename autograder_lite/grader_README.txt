--------------------------------------------------
Before using:
--------------------------------------------------
	Install virtualenv
	Use a terminal (i.e. command line interface) to navigate to this directory
	Type "source venv/bin/activate"
	The above command makes it so that from here on out you are using the python installation that is included with the autograder.

---------------------------------------------------
Usage: python grader.py INITIAL.txt GOALS.txt MY_SOLUTION.txt
---------------------------------------------------
Any filenames works for INITIAL, GOALS, and MY_SOLUTION.
newcatalog.xlsx must be in the same directory, and must have the name newcatalog.xlsx

---------------------------------------------------
Goals file formatting requirements:
---------------------------------------------------
        The order the requirements are listed in does not matter.
        A requirement is either a real course or a higher-level requirement.
        In either case, a requirement must match an entry in newcatalog.xlsx
        One requirement per line in the goals file
        There should 2 fields per requirement, surrounded by single quotes (').
        Those fields should be in this order:
                program (e.g. CS), designation (e.g. 5260)
You should be able to meet all of the above requirements if you print a list of objects of type 'Course' (defined in course_dictionary.py) to a file
Anything outside of single-quotes is ignored and should not interfere with the autograder's parsing.

---------------------------------------------------
Initial file formatting requirements:
---------------------------------------------------
The same requirements as for GOAL file.

---------------------------------------------------
Solution file formatting requirements:
---------------------------------------------------
        The order the courses are listed in does not matter.
        There should be one course per line in your solution file.
        There should 5 fields per course, surrounded by single quotes (').
        Those fields should be in this order:
                program (e.g. CS), designation (e.g. 5260),
                credits (e.g. 3), semester (e.g. Spring), and year (e.g. Frosh)
You should meet all of the above requirements if you use the python function 'pprint' to print out a 'dict' object whose keys are 'Course' and whose values are 'CourseInfo' to a file.
'Course' and 'CourseInfo' are namedtuples (basically lightweight classes) which are defined in course_dictionary.py

