import sys
import course_dictionary
from collections import namedtuple
from enum import IntEnum

MAX_CREDITS_PER_NON_SUMMER_TERM = 18
MIN_CREDITS_PER_NON_SUMMER_TERM = 12
MAX_CREDITS_PER_SUMMER_TERM = 6
MIN_CREDITS_PER_SUMMER_TERM = 0

Course = namedtuple('Course', 'program, designation')
CourseInfo = namedtuple('CourseInfo', 'credits, terms, prereqs')

class ScheduledCourse:
  def __init__(self, course, courseInfo, term):
    self.course = course
    self.courseInfo = courseInfo
    self.term = term
  
  def __hash__(self):
    return hash((self.course, self.term))

  def __eq__(self, other):
    return other and self.course == other.course and self.term == other.term

  def __ne__(self, other):
    return not self.__eq__(other)
  
  def __repr__(self):
    #return "<ScheduledCourse course:%s term:%s>" % (self.course, self.term)
    return "(%s, %s)" % (self.course, self.term)

  def __str__(self):
    return "From str method of ScheduledCourse: course is %s, term is %s" % (self.course, self.term)


class Semester(IntEnum):
  Fall = 1
  Spring = 2
  Summer = 3

class Year(IntEnum):
  Frosh = 0
  Sophomore = 1
  Junior = 2
  Senior = 3

class Term:
  def __init__(self, semester, year):
    self.semester = semester
    self.year = year
    semesterNo = Semester(semester)
    yearNo = Year(year)
    self.termNo = int(yearNo)*3 + int(semesterNo)
  
  # Basically a second constructor
  @classmethod
  def initFromTermNo(clazz, termNo):
    # intentional integer division
    yearNo = int(int(termNo-1) / int(3))
    semesterNo = termNo - (3*yearNo)
    semester = Semester(semesterNo)
    year = Year(yearNo)
    return clazz(semester, year)
  
  def __hash__(self):
    return hash((self.termNo))
  
  def __eq__(self, other):
    return other and self.termNo == other.termNo

  def __ne__(self, other):
    return not self.__eq__(other)
  
  def __repr__(self):
    #return "<Term semester:%s year:%s>" % (self.semester, self.year)
    return "(%s, %s)" % (self.semester, self.year)

  def __str__(self):
    #return "From str method of Term: semester is %s, year is %s" % (self.semester, self.year)
    return "(%s, %s)" % (self.semester, self.year)


def getTokensFromFile(filename, numTokensPerLine) :
  with open(filename) as f:
    lines = f.readlines()
  lines = [x.strip() for x in lines]  
  tokens = list()
  for line in lines:
    #print(line)
    lineTokens = list()
    lastReadCharNo = -1
    # get program, designation, semeseter, year, and credits
    for tokenNo in range(0, numTokensPerLine):
      left = line.find("'", lastReadCharNo+1) + 1
      if(left == 0) :
        # didnt find the token we expected, just return what we have
        return tokens
      #print("left = ", left)
      lastReadCharNo = left
      #print("lastReadCharNo = ", lastReadCharNo)
      right = line.find("'", lastReadCharNo+1)
      #print("right = ", right)
      lastReadCharNo = right
      #print("lastReadCharNo = ", lastReadCharNo)
      token = line[left:right]
      #print("token = ", token)
      lineTokens.append(token)
    tokens.append(lineTokens)
  return tokens

def main(argv):
  
  if(len(argv) != 4):
    print("Usage: python grader.py INITIAL.txt GOALS.txt MY_SOLUTION.txt")
    print("Any filenames works for INITIAL, GOALS, and MY_SOLUTION).")
    print("newcatalog.xlsx must be in the same directory, and must have the name newcatalog.xlsx")
    print("see README.txt for file formatting requirements")
    return
  
  print("Loading courses from newcatalog.xlst...")  
  course_dict = course_dictionary.create_course_dict()
  
  print("Autograder using this file as the INITIAL file:\n", argv[1])
  numTokensPerLine = 2
  tokens = getTokensFromFile(argv[1], numTokensPerLine)
  initialCourses = list()
  for lineTokens in tokens:
    course = Course(lineTokens[0], lineTokens[1])
    if(course in course_dict) :
      initialCourses.append(course)
    else:
      print("Fatal Error: Course in INITIAL file:\n", key, "\nWas not found in newcatalog.xlst")
      return
  print("Loaded from INITIAL file:\n", initialCourses)
  
  print("Autograder using this file as the GOAL file:\n", argv[2])
  numTokensPerLine = 2
  tokens = getTokensFromFile(argv[2], numTokensPerLine)
  goalCourses = list()
  for lineTokens in tokens:
    key = Course(lineTokens[0], lineTokens[1])
    if(key in course_dict) :
      goalCourses.append(key)
    else:
      print("Fatal Error: Course in GOAL file:\n", key, "\nWas not found in newcatalog.xlst")
      return
  print("Loaded from GOAL file:\n", goalCourses)
  
  print("Autograder using this file as the SOLUTION file:\n", argv[3])
  numTokensPerLine = 5
  courseInfoErrorCount = 0
  tokens = getTokensFromFile(argv[3], numTokensPerLine)
  scheduledCourses = list()
  isEmptySolution = False
  if len(tokens) == 0 :
    isEmptySolution = True
  if len(tokens) == 1 and len(tokens[0]) < 5:
    isEmptySolution = True
  if not isEmptySolution :
    for lineTokens in tokens:
      if lineTokens[3] not in Semester.__members__ :
        print("Fatal Error: Unrecognized Semester '", lineTokens[3], "'")
        return
      if lineTokens[4] not in Year.__members__ :
        print("Fatal Error: Unrecognized Year '", lineTokens[4], "'")
        return
      term = Term(Semester[lineTokens[3]], Year[lineTokens[4]]);
      course = Course(lineTokens[0], lineTokens[1])
      if(course not in course_dict) :
        print("Fatal Error: Course in SOLUTION file:\n", course, "\nWas not found in newcatalog.xlst")
        return
      courseInfo = course_dict[course]
      if int(courseInfo.credits) != int(lineTokens[2]) :
        print("Error in your solution:") 
        print("\tIncorrect number of credits for course ", course)
        print("\t\tnewcatalog.xlst: ", int(lineTokens[2]))
        print("\t\tnewcatalog.xlst: ", int(courseInfo.credits))
        courseInfoErrorCount += 1
      scheduledCourse = ScheduledCourse(course, courseInfo, term)
      scheduledCourses.append(scheduledCourse)

  print("Loaded from SOLUTION file:\n", scheduledCourses)
  if isEmptySolution :
    print("FIXME: check whether an empty solution is correct (i.e. there is no solution)")
    print("**********Ending grader.py early...**********")
    return
  
  scheduledCourses.sort(key=lambda x: x.term.termNo)
  print("Loaded courses in your solution:\n", scheduledCourses)
  
  # 3 semesters * 4 years
  numTerms = 12
  creditsByTerm = {}
  scheduledCoursesByTerm = {}
  # initialize the lists in the dictionaries
  for termNo in range(1, numTerms+1) :
    term = Term.initFromTermNo(termNo)
    creditsByTerm[term] = 0
    scheduledCoursesByTerm[term] = []
  # add up credits for each semester
  for scheduledCourse in scheduledCourses :
    term = scheduledCourse.term
    credits = int(scheduledCourse.courseInfo.credits)
    creditsByTerm[term] += credits
    scheduledCoursesByTerm[term].append(scheduledCourse)

  print("Checking number of credit hours in each term...")
  print(creditsByTerm)

  finishedByTermNo = 0;
  for termNo in range(1, numTerms+1) :
    term = Term.initFromTermNo(termNo)
    if creditsByTerm[term] > 0 :
      finishedByTermNo = termNo

  creditErrorCount = 0
  for termNo in range(1, finishedByTermNo+1) :
    term = Term.initFromTermNo(termNo)
    isSummer = False
    if termNo%3 == 0 :
      isSummer = True
    if isSummer:
      if creditsByTerm[term] > MAX_CREDITS_PER_SUMMER_TERM :
        print("Error in your solution:") 
        print("\tToo many credits taken in term #", term)
        creditErrorCount += 1
      elif creditsByTerm[term] < MIN_CREDITS_PER_SUMMER_TERM :
        print("Error in your solution:") 
        print("\tToo few credits taken in term #", term)
        creditErrorCount += 1
    else:
      if creditsByTerm[term] > MAX_CREDITS_PER_NON_SUMMER_TERM :
        print("Error in your solution:") 
        print("\tToo many credits taken in term #", term)
        creditErrorCount += 1
      elif creditsByTerm[term] < MIN_CREDITS_PER_NON_SUMMER_TERM :
        print("Error in your solution:") 
        print("\tToo few credits taken in term #", term)
        creditErrorCount += 1
    
  print("Checking that each course's credits and available terms match solution...")
  for scheduledCourse in scheduledCourses :
    courseInfo = scheduledCourse.courseInfo
    scheduledSemester = scheduledCourse.term.semester
    scheduledSemesterName = Semester(scheduledSemester).name
    #print("semesterName: ", semesterName)
    if scheduledSemesterName not in courseInfo.terms :
      print("Error in your solution:") 
      print("\tTried to take course ", scheduledCourse.course, " during a semester that it is not offered.")
      print("\t\tSolution: ", scheduledSemesterName)
      print("\t\tnewcatalog.xlst: ", courseInfo.terms)
      courseInfoErrorCount += 1
  

  print("Checking that each course's prerequisites are taken before that course...")
  prerequisiteErrorCount = 0

  # Take 'normal', not e.g. ('CS', 'major'), courses 
  coursesTakenSoFar = initialCourses
  for termNo in range(1, finishedByTermNo+1) :
    term = Term.initFromTermNo(termNo)
    coursesToTakeThisTerm = scheduledCoursesByTerm[term]
    coursesTakenThisTerm = []
    for scheduledCourse in coursesToTakeThisTerm :
      # check if 'normal' course
      if(int(scheduledCourse.courseInfo.credits) != 0) :
        course = scheduledCourse.course
        prereqs = scheduledCourse.courseInfo.prereqs
        print("Taking course: ", course, "...")
        print("Prereqs are: ", prereqs)

        has_prereqs = len(prereqs) > 0
        did_satisfy_prereqs = False
        if not has_prereqs :
          did_satisfy_prereqs = True
        else:
          for prereq_or_element in prereqs :
            prereq_and_term = prereq_or_element
            did_satisfy_and_term = True
            for prereq_and_element in prereq_and_term :
              if prereq_and_element not in coursesTakenSoFar :
                did_satisfy_and_term = False
              if prereq_and_element not in coursesTakenSoFar :
                did_satisfy_and_term = False
            if did_satisfy_and_term :
              did_satisfy_prereqs = True
        if not did_satisfy_prereqs :
          print("Error in your solution:") 
          print("\tTried to take course ", course, " before (or without) its prerequisites.")
          prerequisiteErrorCount += 1
        else:
          coursesTakenThisTerm.append(course);
          print("Successfully took course: ", course)
    # take all courses for a semester after checking all prereqs for them
    for course in coursesTakenThisTerm :
      coursesTakenSoFar.append(course)
    
    # take any 0-credit (not really a course) requirements
    # these CAN be satisfied by things taken the same semester
    tookRequirement = True
    while tookRequirement :
      tookRequirement = False
      for scheduledCourse in coursesToTakeThisTerm :
        course = scheduledCourse.course
        courseInfo = scheduledCourse.courseInfo
        # check if non-course requirement
        if(int(courseInfo.credits) == 0) :
          # need this check because we are in a while loop
          if course not in coursesTakenSoFar :
            prereqs = courseInfo.prereqs
            print("Checking higher-level requirement: ", course, "...")
            print("Prereqs are: ", prereqs)
            has_prereqs = len(prereqs) > 0
            did_satisfy_prereqs = False
            if not has_prereqs :
              did_satisfy_prereqs = True
            else:
              for prereq_or_element in prereqs :
                prereq_and_term = prereq_or_element
                did_satisfy_and_term = True
                for prereq_and_element in prereq_and_term :
                  if prereq_and_element not in coursesTakenSoFar :
                    did_satisfy_and_term = False
                  if prereq_and_element not in coursesTakenSoFar :
                    did_satisfy_and_term = False
                if did_satisfy_and_term :
                  did_satisfy_prereqs = True
            if did_satisfy_prereqs :
              print("Satisfied higher-level requirement: ", course)
              coursesTakenSoFar.append(course)
              tookRequirement = True
          

  # Indicate that we are in the final state, and are now checking goals
  coursesTaken = coursesTakenSoFar

  print("Checking that all courses in the goal state are taken...")
  goalErrorCount = 0
  for goalCourse in goalCourses :
    if goalCourse not in coursesTaken :
      print("Error in your solution:") 
      print("\tDid not satisfy requirement/goal ", goalCourse)
      goalErrorCount += 1
  
  totalErrorCount = courseInfoErrorCount + creditErrorCount + prerequisiteErrorCount + goalErrorCount
  print("********** Autograder finished **********")
  print("There are ", totalErrorCount, " errors in your solution.")
  finishedByTerm = Term.initFromTermNo(finishedByTermNo)
  print("Your solution finished by ", finishedByTerm.semester.name, " ", finishedByTerm.year.name, ".")
  
if __name__ == "__main__":
    main(sys.argv)

