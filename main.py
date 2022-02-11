Scores=int(input("What is your score? "))
print(f"Your grade is {Scores}")
# grade_A=input("[90-100]")
# for number in {grade_A}:
#   input=("A")
# print(f"{Scores}")
if Scores >=90:
  print("You received an A")
if Scores >=80 and Scores <=89:
  print ("You received a B")
if Scores >=70 and Scores<=79:
  print ("You received a C")
if Scores >=60 and Scores<=69:
  print("You received a D")
if Scores<60:
  print("You received a F")


