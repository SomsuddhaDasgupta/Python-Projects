print("Welcome to the Sam quiz 2024")
print("The questions will be from Indian Polity")

playing = input("Do you want to play? ")

if playing != "yes":
	quit()

print("Awesome! Let's start :)")
score = 0


answer = input("Who is the head of the Indian Republic? ")
if answer.lower() == "the president of india":
	print('Correct! ')
	score += 1
else:
	print('Incorrect :(')


answer = input("What is the maximum term of the Lok Sabha? ")
if answer.lower() == "5 years":
	print('Correct! ')
	score += 1
else:
	print('Incorrect :(')


answer = input("Who is the current Chief Justice of India? ")
if answer.lower() == "d.y. chandrachud":
	print('Correct! ')
	score += 1
else:
	print('Incorrect :(')


answer = input("Who was the chairman of the drafting committee of the Indian Constitution? ")
if answer.lower() == "dr. b.r. ambedkar":
	print('Correct! ')
	score += 1
else:
	print('Incorrect :(')
	

answer = input("Who is the current President of India? ")
if answer.lower() == "draupadi murmu":
	print('Correct! ')
	score += 1
else:
	print('Incorrect :(')

print("You got " + str(score) + " points")
print("You got " + str(score /5 * 100) + "%")
print("Thank you for participating! ")
