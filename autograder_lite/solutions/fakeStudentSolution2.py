import sys
import course_dictionary

def main(argv):
  if(len(argv) != 2):
    print("Usage: python grader.py INITIAL.txt GOALS.txt")
    return

#def course_scheduler(catalog, goalCourses, initialCourses)
def course_scheduler(catalog, goalCourses, initialCourses) :
  solution = {}
  # just add the goals without their prereqs
  for goalCourse in goalCourses :
    courseInfo = catalog[goalCourse]
    # terms should contain a single semester, and year,
    # not a list of possible semesters
    solution[goalCourse] = course_dictionary.CourseInfo(courseInfo.credits, ('Fall','Senior'), courseInfo.prereqs)
    print("***************student solution returning solution:************")
    print(solution)
  return solution
  
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
      lastReadCharNo = left
      right = line.find("'", lastReadCharNo+1)
      lastReadCharNo = right
      token = line[left:right]
      lineTokens.append(token)
    tokens.append(lineTokens)
  return tokens

if __name__ == '__main__':
  main(sys.argv)
