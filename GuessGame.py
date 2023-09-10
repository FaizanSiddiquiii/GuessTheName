secretName = "Faizan"
guess = ""
guessLimit = 3
guessCount = 0
outofguesses = False
while guess != secretName and not (outofguesses):
  if guessCount < guessLimit:
    guess = input("Enter guess: ")
    guessCount += 1
  else:
    outofguesses = True

if outofguesses:
  print("Out of Guesses, You Lose! :(")
else:
  print("You Win, Congrats! :)")
    
