import random

name = "Gwen"
question = "Should I have second breakfast?"
answer = ""

random_number = random.randint(1, 13)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Consult Google, not me."
elif random_number == 11:
  answer = "Please just try therapy."
elif random_number == 12:
  answer = "Whoa now, I'm just RNG, not a therapist."
elif random_number == 13:
  answer = "404"
else:
  answer = "Error"

if name == "":
  print("Question:", question)
else:
  print(name, "asks:", question)

if question == "":
  print("Magic 8-Ball says: I can read the future, not your mind. You must ask enter your question to ask it.")
else:
  print("Magic 8-Ball says:", answer)
