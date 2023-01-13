"""
Chapter 6 project
12/22/2022 Program: doctor2.py
Application that asks the user for input and responds by redirecting the input into a new question. Program will also randomly choose hedge statements to keep the conversation moving.
"""
import random
# Global variables (data pool)
hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue", "Go on, go on...", "You don't say...")
qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")
replacements = {"I":"you", "me":"you", "my":"your", "we":"you", "us":"you", "mine":"yours", "am":"are", "was":"were", "you":"I"}
history = []
# Definition of the reply() function
def reply(sentence):
	"""Builds and returns a reply to the input the user provides."""
	print(history)
	probability = random.randint(1, 4)
	if probability == 1:
		response = random.choice(hedges)
	elif probability == 2 and len(history) > 3:
		response = "Earlier you said that " + random.choice(history)
	else:
		response = random.choice(qualifiers) + changePerson(sentence)
	history.append(sentence)
	return response
# Definition of the changePerson() function
def changePerson(sentence):
	"""Replaces first-person pronouns with second person pronouns."""
	words = sentence.split()
	replyWords = []
	for word in words:
		replyWords.append(replacements.get(word, word))
	return " ".join(replyWords)
# Definition of the main() function for program entry
def main():
	"""Handles the interaction between patient and doctor."""
	print("Greetings, I hope you are well today!")
	print("What can I do for you?")
	# Keep this app running until the user decides to QUIT
	while True:
		sentence = input("Type a response, or type QUIT to exit >>")
		# check if the user typed QUIT, if they did exit the program
		if sentence.upper() == "QUIT":
			print("Have a nice day!")
			break
		# If we are here, the user must not have typed quit
		print(reply(sentence))
# Global call to the main() function for program execution
main()