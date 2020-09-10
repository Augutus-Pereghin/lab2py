# Author: Augustus Perseghin agp5191
# Collaborator: Kieran Murdocca kkm5754@psu.edu
# Collaborator: Reuben Lee wzl128@psu.edu
# Collaborator: Krish Choudhary ksc5496@psu.edu
# Section: 4
# Breakout: 18

def getLetterGrade(grade):
  if grade >= 93:
    return("A")
  elif grade >= 90:
    return("A-")
  elif grade >= 87:
    return("B+")
  elif grade >= 83:
    return("B")
  elif grade >= 80:
    return("B-")
  elif grade >= 77:
    return("C+")
  elif grade >= 70:
    return("C")
  elif grade >= 60:
    return("D")
  else:
    return("F")

def run():
  numGrade = float(input("Enter your CMPSC 131 grade: "))
  letterGrade = getLetterGrade(numGrade)
  print(f"Your letter grade for CMPSC 131 is {letterGrade}.")

if __name__ == "__main__":
  run()

