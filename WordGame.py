import random 
     
# Function to assign random words from the given list.
def choose(): 
    # list of moviesName 
    moviesName = ['unplanned',
                    'thekid',
                    'escaperoom',
                    'howtotrainyourdragon',
                    'glass',
                    'theupside',
                    'coldpursuit',
                    'captainmarvel',
                    'fivefeetapart',
                    'thewind',
                    'avengersendgame',
                    'longshot',
                    'brightburn',
                    'aladdin',
                    'theperfection',
                    'johnwick',
                    'godzilla',
                    'thesecretlifeofpets',
                    'murdermystery',
                    'annabellecomeshome',
                    'crawl',
                    'iammother',
                    'lightofmylife',
                    'theinformer',
                    'downtonabbey',
                    'joker',
                    'zombieland',
                    'sweetheart',
                    'terminator',
                    'thefarewell',
                    'doctorsleep',
                    'frozen',
                    'hustlers',
                    'knivesout',
                    'darkwaters',
                    'jumanji',
                    'starwars',
                    'parasite',
                    'waves',
                    'thefinalwish'] 
  
    # choice() method calls for randomly choosing the movies name
    pickMovie = random.choice(moviesName) 
  
    return pickMovie 
  
  
# Function for shuffling characters of the chosen word. 
def jumble(word): 
    # sample() method to shuffle the characters of the word 
    random_word = random.sample(word, len(word)) 
  
    # join() method join the elements of the iterator with particular character
    jumbled = ''.join(random_word) 
    return jumbled 
    
  
# Function for declaring winner. 
def check_win(player1, player2, p1score, p2score): 
    if p1score > p2score: 
        print("The winner is :", player1) 
    elif p2score > p1score: 
        print("The winner is :", player2) 
    else: 
        print("Game was Drawn! Good Luck Guys.") 
  

# Function for final score. 
def thank(p1n, p2n, p1, p2): 
    print(p1n, 'Your score is :', p1) 
    print(p2n, 'Your score is :', p2) 
  
    # check_win() function calling 
    check_win(p1n, p2n, p1, p2) 
  
    print('Thanks for playing...') 
    
      
# Function for playing the game. 
def play(): 
    # enter player1 and player2 name 
    p1name = input("Player 1, Please enter your name: ") 
    p2name = input("Player 2 , Please enter your name: ") 
  
    # variable for counting score. 
    pp1 = 0
    pp2 = 0
  
    # variable for counting turn 
    turn = 0
  
    while True: 
  
        # calling choose() function
        picked_word = choose() 
  
        # calling jumble() function 
        jumbled_name = jumble(picked_word) 
        print("jumbled movie name is :", jumbled_name) 
  
        # checking turn is odd or even 
        if turn % 2 == 0: 
  
            # player1 turn if the trun is even
            print(p1name, 'Your Turn.') 
  
            ans = input("Guess the correct movie name? ") 
  
            # checking ans is equal to picked_word or not 
            if ans == picked_word: 
                
                # The score for player 1 increases based on correct guess
                pp1 += 1
  
                print('Your score is :', pp1) 
                turn += 1
  
            else: 
                print("Wrong guess, better luck next time...") 
  
                # player 2 turn 
                print(p2name, 'Your turn.') 
  
                ans = input("Guess the correct movie name? ") 
  
                # The score for player 2 increases based on correct guess
                if ans == picked_word: 
                    pp2 += 1
                    print("Your Score is :", pp2) 
  
                else: 
                    print("Better luck next time...correct word is :", picked_word) 
  
                c = int(input("press 1 to continue and 0 to quit :")) 
  
                # checking the c is equal to 0 or not 
                # if c is equal to 0 then break out 
                # of the while loop otherwise keep looping.
                
                if c == 0: 
                    # calling thank() function 
                    thank(p1name, p2name, pp1, pp2) 
                    break
  
        else: 
  
            # player2 turn if the trun is odd 
            print(p2name, 'Your turn.') 
            ans = input("Guess the correct movie name? ") 
  
            if ans == picked_word: 
                pp2 += 1
                print("Your Score is :", pp2) 
                turn += 1
  
            else: 
                print("Wrong guess, better luck next time...") 
                
                # player 1 turn 
                print(p1name, 'Your turn.') 
                ans = input("Guess the correct movie name? ") 
  
                if ans == picked_word: 
                    pp1 += 1
                    print("Your Score is :", pp1) 
  
                else: 
                    print("Better luck next time...correct word is :", picked_word) 
  
                    c = int(input("press 1 to continue and 0 to quit :")) 
  
                    if c == 0: 
                        # calling thank() function 
                        thank(p1name, p2name, pp1, pp2) 
                        break
  
            c = int(input("press 1 to continue and 0 to quit :")) 
            if c == 0: 
                # calling thank() function 
                thank(p1name, p2name, pp1, pp2) 
                break


# calling main() function  
if __name__ == "__main__":
    play()

