import course_dictionary

#def course_scheduler(catalog, goalCourses, initialCourses)
def course_scheduler(catalog, goalCourses, initialCourses) :
  solution = {}
  # just add the goals without their prereqs
  for goalCourse in goalCourses :
    courseInfo = catalog[goalCourse]
    # terms should contain a single semester, and year,
    # not a list of possible semesters
    #courseInfo[terms]_replace("('Fall','Frosh')")
    #courseInfo.terms = "('Fall','Frosh')"
    #solution[goalCourse] = course_dictionary.CourseInfo(courseInfo.credits, "('Fall','Frosh')", courseInfo.prereqs)
    solution[goalCourse] = course_dictionary.CourseInfo(courseInfo.credits, ('Fall','Frosh'), courseInfo.prereqs)
    print("***************student solution returning solution:************")
    print(solution)
  return solution
