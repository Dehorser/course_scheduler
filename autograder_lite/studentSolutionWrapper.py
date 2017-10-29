import os
import sys
from collections import namedtuple
import pprint
from multiprocessing.pool import ThreadPool
import course_dictionary
import solution

PROGRAM_FILENAME = "solution.py"
SOLUTION_FILENAME = "solution.txt"

Course = namedtuple('Course', 'program, designation')
CourseInfo = namedtuple('CourseInfo', 'credits, terms, prereqs')

def main(argv):
  
  if(len(argv) != 3):
    print("Usage: python studentSolutionWrapper.py INITIAL.txt GOALS.txt")
    return
  
  print("Loading courses from newcatalog.xlst...")
  course_dict = course_dictionary.create_course_dict()

  print("Wrapper using this file as the INITIAL file:\n", argv[1])
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

  print("Wrapper using this file as the GOAL file:\n", argv[2])
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

  args = (course_dict, goalCourses, initialCourses)
  
  pool = ThreadPool(processes=1)
  async_result = pool.apply_async(solution.course_scheduler, args)
  return_val = async_result.get()
  solution_dict = return_val
  solution_str = pprint.pformat(solution_dict)
  f = open(SOLUTION_FILENAME, "w")
  f.write(solution_str)
  f.close()
  
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
      lastReadCharNo = left
      right = line.find("'", lastReadCharNo+1)
      lastReadCharNo = right
      token = line[left:right]
      lineTokens.append(token)
    tokens.append(lineTokens)
  return tokens


if __name__ == "__main__":
    main(sys.argv)

