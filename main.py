go = input('Would you like to play the maze game: ')
death = "Oops, you took a wrong turn, you died"
cont = 'Good job, keep going'

def Main():
  name = input('What would you like me to call you: ')
  health = 10
  print(name, ' You currently have 10 health, get through the maze without losing all your health to win!')
  print("Let's get started ", name, " !")
  opt1 = input('Would you like to go left or right: ')
  if opt1 == 'left' or 'Left':
    print('Good job, keep going')
  else:
    print(death)
  opt2 = input('Would you like to go left or right: ')
  if opt2 == 'Left' or 'left':
    print(cont)
  else:
    print("Death")


if go == 'yes':
  Main()
elif go == 'no':
  pass
else:
  Main()