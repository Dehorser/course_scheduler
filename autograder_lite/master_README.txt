--------------------------------------------------
Before using:
--------------------------------------------------
	Install virtualenv
	Use a terminal (i.e. command line interface) to navigate to this directory
	Type "source venv/bin/activate"
	The above command makes it so that from here on out you are using the python installation that is included with the autograder.

---------------------------------------------------
Usage: python master.py
---------------------------------------------------
newcatalog.xlsx must be in the same directory, and must have the name newcatalog.xlsx .
GOAL and INITIAL files listed in master.py source code must exist and be in the same directory.
student solutions to be tested should be placed in the solutions folder.
If a student solution is a project with more than one .py file (likely),
then ensure that only the main .py file is in the solutions folder, and the other files are in subfolders that can still be found when the main file is renamed and moved up to the autograder directory (up and out of the solutions folder).  Possibly simply copy all non-main .py files into the autograder directory, or some subdirectory therein like "lib".
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
studentSolutionWrapper.py makes it so you have to define the function solution.course_scheduler(course_dict, goalCourses, initialCourses), rather than outputting to a file yourself.

