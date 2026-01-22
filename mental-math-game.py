from turtle import *
import random # randomizer module
import time # to record time

# Turtle creation
t = Turtle()
t.shape('turtle')
t.color('red')
t.speed(30)

# Set turtle stage
t.penup()
t.goto(-100,0)
t.forward(300)
t.pendown()
t.fillcolor('green')
t.color('green','green')
t.begin_fill()
for i in range(4):
    t.forward(20)
    t.left(90)
t.end_fill()
t.penup()
t.goto(-100,0)
t.pendown()
t.speed(10)
t.color('red')

# Colour palette selector
COLOURS = ['red','blue','light blue','magenta','orange','yellow','black','gray','purple']
def colour_rand():
    t.color(COLOURS[random.randint(0,8)])
    
# Set target value
def add(a):
    print('Correct answer! Score increased.\n')
    t.forward(25)
    a+=1
    print('Target: 14')
    print(f'Score: {a}\n')
    return a
    
def subtract(b):
    print('Wrong answer! Score reduced by 1.\n')
    t.backward(25)
    b-=1
    print('Target: 14')
    print(f'Score: {b}\n')
    return b

print("+==============================================+")
print("| Welcome to the TestYourMentalMath Challenge! |")
print("+==============================================+")
print("|                                              |")
print("| This is a game where you put your quick witts|")
print("| and skills to the test with this fun game of |")
print("| mental math and turtles! As for each question|")
print("| you get correct, your turtle moves forward to|")
print("| its goal, otherwise backwards! Enjoy!✌️       |")
print("|                                              |")
print("| Your target goal: 14 points                  |")
print("| For every wrong answer: -1 point             |")
print("| For every right answer: +1 point             |")
print("|                                              |")
print("| You lose at: -4 points                       |")
print("| A line is indicated for every correct answer |")
print("|                                              |")
print("| P.S. Only the rock paper scissors match      |")
print("| require some luck factor ^^                  |")
print("+==============================================+\n")

timer_start = time.time() # Start of timer

# Start of game
t.width(3.5)
target = 0
while target != 14:
    try:
        while target != -4:
            print('Provided question/game:')
            print('--------------------')
            r_choice = random.randint(1,5)
            
            if r_choice == 1: # Addition
                rand1 = random.randint(-10000,50000)
                rand2 = random.randint(-5200,90000)
                ans1 = rand1 + rand2
                print(f'{rand1} + {rand2} is?')
                user = int(input('What\'s your answer?: '))
             
                if user == ans1:
                    t.pendown()
                    colour_rand()
                    target=add(target)
                else:
                    t.penup()
                    target=subtract(target)

            elif r_choice == 2: # Subtraction
                rand1 = random.randint(-200,5860)
                rand2 = random.randint(-4000,10000)
                ans2 = rand1 - rand2
                print(f'{rand1} - {rand2} is?')
                user = int(input('What\'s your answer?: '))
           
                if user == ans2:
                    t.pendown()
                    colour_rand()
                    target=add(target)
                else:
                    t.penup()
                    target=subtract(target)
                    
            elif r_choice == 3: # Multiply
                rand1 = random.randint(-100,5000)
                rand2 = random.randint(-400,1990)
                ans3 = rand1 * rand2
                print(f'{rand1} x {rand2} is?')
                user = int(input('What\'s your answer?: '))
           
                if user == ans3:
                    t.pendown()
                    colour_rand()
                    target=add(target)
                else:
                    t.penup()
                    target=subtract(target)
         
            elif r_choice == 4: # Division
                rand1 = random.randint(1,9990)
                rand2 = random.randint(-200,1500)
                if rand1 > rand2:
                    ans4 = rand1 // rand2
                    print(f'{rand1} / {rand2} is?')
                    user = int(input('What\'s your answer? (Give to the nearest whole number only): '))
                    if user == ans4:
                        t.pendown()
                        colour_rand()
                        target=add(target)
                    else:
                        t.penup()
                        target=subtract(target)
                else:
                    continue
                    
            elif r_choice == 5: # Play a game of rock paper scissors

                # Rule documentation for players:
                '''
                Rules for Rock, Paper, and Scissors:
                1 ✊ --> 3 ✌
                3 ✌ --> 2 ✋
                2 ✋ --> 1 ✊
                '''
                
                choices = {1:'✊', 2:'✋', 3:'✌'}

                print("+---------------------------+")
                print("| Rock, Paper, and Scissors |")
                try:
                    status = True
                    while status:
                        print("+---------------------------+")
                        print("|  1. ✊  (Rock)            |")
                        print("|  2. ✋  (Paper)           |")
                        print("|  3. ✌️  (Scissors)        |")
                        print("+---------------------------+")

                        player = int(input("\nPick your number (1 to 3): "))

                        if player not in [1,2,3]:
                            print('Invalid number chosen. Please select 1 to 3: \n')
                            continue

                        computer = random.randint(1,3)
                        print(f'Your choice: {choices[player]}')
                        print(f'Computer\'s choice: {choices[computer]}')

                        if player == computer:
                            print('It\'s a tie! Re-roll your selection.\n')
                        elif (player == 1 and computer == 3) or (player == 2 and computer == 1) and (player == 3 and computer == 2):
                            print('Player has won this match! Computer lost.\n')
                            t.pendown()
                            colour_rand()
                            target=add(target)
                            status = False
                        else:
                            print('Computer has won this match! Player lost.\n')
                            t.penup()
                            target=subtract(target)
                            status = False
                            
                    if status == False:
                        break
                except ValueError:
                    print('Invalid input! Please try again.\n')
                    continue

        else:
            print('You have failed this mental math challenge :(. Better luck next time!') # User lost
            print('Thank you so much for playing!!')
            break
    except ValueError:
        print('Invalid choice. Please enter an integer value.\n')

timer_end = time.time() # End the timer
time_taken = timer_end - timer_start # total time
    
if t.distance == target: # User won
    print('Congratulations! You have reached your final target!')
    t.color('magenta')
    t.width(4)
    t.speed(20)
    t.goto(-250,100)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.forward(-100)
    t.right(90)
    t.forward(-50)
    t.left(90)
    t.forward(100)
    t.forward(-100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.forward(-100)
    t.right(90)
    t.penup()
    t.forward(40)
    t.pendown()
    t.color('blue')
    t.forward(40)
    t.forward(-20)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(20)
    t.forward(-40)
    t.forward(40)
    t.penup()
    t.forward(30)
    t.pendown()
    t.color('magenta')
    t.left(90)
    t.forward(-100)
    t.forward(100)
    t.right(90+55)
    t.forward(120)
    t.left(180)
    t.right(35)
    t.forward(100)
    t.ht()

print(f"Total time taken: {time_taken:.2f} seconds.")

