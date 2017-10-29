import os
import sys
from collections import namedtuple
#import grader
#import studentSolutionWrapper

#PROGRAM_FILENAME = "studentSolutionWrapper.py"
STUDENT_PROGRAM_FILENAME = "solution.py"
WRAPPED_PROGRAM_FILENAME = "studentSolutionWrapper.py"
SOLUTION_FILENAME = "solution.txt"

TestCase = namedtuple('TestCase', 'initialFilename, goalFilename')

def main(argv):
  
  if(len(argv) != 1):
    print("Usage: python master.py")
    return
  
  #studentProgramFilename = SOLUTION_PROGRAM_FILENAME
  #solutionFilename = SOLUTION_FILENAME
  
  testCases = []
  testCases.append(TestCase("initial1","goal1"))
  testCases.append(TestCase("initial2","goal2"))

  
  solutionFiles = getSolutionFilePaths()
  for solutionFile in solutionFiles :
    command1 = "cp" + " " + solutionFile + " " + "./" + STUDENT_PROGRAM_FILENAME
    print("master.py executing command:")
    print(command1)
    os.system(command1)
    for testCase in testCases :
      command2 = "python" + " " + WRAPPED_PROGRAM_FILENAME + " " + testCase.initialFilename + " " + testCase.goalFilename
      print("master.py executing command:")
      print(command2)
      os.system(command2)
      command3 = "python" + " " + "grader.py" + " " + testCase.initialFilename + " " + testCase.goalFilename + " " + SOLUTION_FILENAME
      print("master.py executing command:")
      print(command3)
      os.system(command3)

def getSolutionFilePaths() :
  paths = []
  for file in os.listdir("./solutions"):
    if file.endswith(".py"):
      path = os.path.join("./solutions", file)
      print(path)
      paths.append(path)
  return paths

if __name__ == "__main__":
    main(sys.argv)

