print("Welcome To The Quiz Game!!")

player = input("Do You Want To Play The Game? ")

if player.lower() != "yes":
    quit()
print("okay!! let's play...")
score = 0

question = input("what does CSE stands for? ")
if question.lower() == "computer science engineering":
    print("correct!!")
    score += 1
else:
    print("incorrect!!")
    
question = input("what does RAM stands for? ")
if question.lower() == "random memory access":
    print("correct!!")
    score += 1
else:
    print("incorrect!!")
    
question = input("what does MAC in apple mac stands for? ")
if question.lower() == "macintosh":
    print("correct!!")
    score += 1
else:
    print("incorrect!!")
    
question = input("what does WHO stands for? ")
if question.lower() == "world health organisation":
    print("correct!!")
    score += 1
else:
    print("incorrect!!")
    
question = input("what does IOS stands for? ")
if question.lower() == "iphone operating system":
    print("correct!!")
    score += 1
else:
    print("incorrect!!")
    
print("you got " + str(score) + " correct answers")
print("you got " + str((score/5) * 100) + " %")

print("THANKS FOR PLAYING :) ")