#Intro
print("Welcome to Quiz Game")
print("-by Adesh")
print("")

#Points
points = 0

#Q1
print("Q1) Who is the current Captain of Indian Cricket Team?")
Q1 = input("Ans: ")
if Q1.lower() == "rohit sharma":
    print("Correct")
    points = points + 1
else:
    print("Wrong")
print("")

#Q2
print("Q2) What does 'WHO' stand for?")
Q2 = input("Ans: ")
if Q2.lower() == "world health organisation":
    print("Correct")
    points = points + 1
else:
    print("Wrong")
print("")

#Q3
print("Q3) Which year did India get Independence?")
Q3 = input("Ans: ")
if Q3.lower() == "1947":
    print("Correct")
    points = points + 1
else:
    print("Wrong")
print("")

#Q4
print("Q4) What is the full form of RBI?")
Q4 = input("Ans: ")
if Q4.lower() == "reserve bank of india":
    print("Correct")
    points = points + 1
else:
    print("Wrong")
print("")

#Q5
print("Q5) how many players are there in a Cricket Team?")
Q5 = input("Ans: ")
if Q5.lower() == "11":
    print("Correct")
    points = points + 1
else:
    print("Wrong")
print("")

#score
print("Your score is " + str(points))
print(str(points) + "/5")




