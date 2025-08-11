import os 

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def countIt(a):
  if a == "exit":
     return True
  word = len(a.split(" "))
  emt = []

  for i in a:
      emt.append(i)
  if ' ' in emt:   
    emt.remove(' ')
  char = len(emt)
  print(f"There are {word} word in Pharase\nThere are {char} characters in Pharase!!")

def mainLoop():
  clear_screen()
  print("Welcome to word counter!! ")
  while True:
    ask = input("Write phares here: ").lower()
    if countIt(ask) == True:
       break

if __name__ == "__main__":
    mainLoop()