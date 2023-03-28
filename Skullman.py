skull_art = [
'███████████████████████████',
'███████▀▀▀░░░░░░░▀▀▀███████',
'████▀░░░░░░░░░░░░░░░░░▀████',
'███│░░░░░░░░░░░░░░░░░░░│███',
'██▌│░░░░░░░░░░░░░░░░░░░│▐██',
'██░└┐░░░░░░░░░░░░░░░░░┌┘░██',
'██░░└┐░░░░░░░░░░░░░░░┌┘░░██',
'██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██',
'██▌░│██████▌░░░▐██████│░▐██',
'███░│▐███▀▀░░▄░░▀▀███▌│░███',
'██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██',
'██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██',
'████▄─┘██▌░░░░░░░▐██└─▄████',
'█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████',
'████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████',
'█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████',
'███████▄░░░░░░░░░░░▄███████',
'''██████████▄▄▄▄▄▄▄██████████
████████▄     ▄████████    ▄████████     ███        ▄█    █▄         
███   ▀███   ███    ███   ███    ███ ▀█████████▄   ███    ███        
███    ███   ███    █▀    ███    ███    ▀███▀▀██   ███    ███        
███    ███  ▄███▄▄▄       ███    ███     ███   ▀  ▄███▄▄▄▄███▄▄      
███    ███ ▀▀███▀▀▀     ▀███████████     ███     ▀▀███▀▀▀▀███▀       
███    ███   ███    █▄    ███    ███     ███       ███    ███        
███   ▄███   ███    ███   ███    ███     ███       ███    ███        
████████▀    ██████████   ███    █▀     ▄████▀     ███    █▀    
''']

lose='''
__  __               __
\ \/ /___  __  __   / /   ____  ________
 \  / __ \/ / / /  / /   / __ \/ ___/ _ \\ 
 / / /_/ / /_/ /  / /___/ /_/ (__  )  __/
/_/\____/\__,_/  /_____/\____/____/\___/
'''

win='''
░░░░░░░░░░░░░░░░░░░░░░█████████
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░████████████░░░█████████████████
'''

import random  
import json
dictionary=open('dictionary.json')
dictionary=dictionary.read()
dictionary=json.loads(dictionary)

print('''
The game is called Skullman. It is inspired by the game hangman.

Instructions:
You only 6 lives. If you have 6 wrong attempts, you lose.
The player wins when they completed the secret word. If the players get every letter of the word before the program shows the complete form of the skull then they win.
''')

while True:
    entered_letter=[]
    current_answer=[]
    death_count=0
    while True:
        try:
            life=int(input('Choose how many lives you want.[6/9]\n~~~~> '))
            if life == 6:
                life_times=3
                break
            elif life == 9:
                life_times=2
                break
            else: print('CHOOSE AVAILABLE OPTIONS!')
        except: print('CHOOSE AVAILABLE OPTIONS!')
        
    while True:
        difficulty=input("Enter difficulty.\n[S-short words(3-5 letters)]\n[M-between short and long words(6-9 letters)]\n[L-long words(10+ letters)]\n~~~~> ").upper().strip()
        if difficulty == 'S' or difficulty == 'L' or difficulty == 'M':break
        else: print('CHOOSE AVAILABLE OPTIONS!')
        
    while True:
        chosen_word=random.choice(list(dictionary.keys()))
        if difficulty == 'S' and len(chosen_word) >= 3 and len(chosen_word) <= 5:break
        elif difficulty == 'M' and len(chosen_word) >= 6 and len(chosen_word) <= 9:break
        elif difficulty == 'L' and len(chosen_word) >= 10:break
        else: pass       

    chosen_word_list=list(chosen_word)
    
    for i in range(len(chosen_word)):
        if chosen_word_list[i] == '-':
            print('-', end=' ')
            current_answer.append('-')
            continue
        print('_', end=' ')
        current_answer.append('_')

    while True:
        
        answer=input('\nEnter a letter: ').lower().strip()
        
        if answer in entered_letter:
            entered_letter.append(answer)
            print("You have already entered that letter!")
            print(*skull_art[0:death_count*life_times],sep='\n')
                
        elif answer in chosen_word_list:
            index=0
            entered_letter.append(answer)
            print(*skull_art[0:death_count*life_times],sep='\n')
            for i in chosen_word_list:            
                if i == answer: current_answer[index]=answer
                index+=1

        elif len(answer) > 1:
            print("Please enter one letter!")
            print(*skull_art[0:death_count*life_times],sep='\n')
        
        else:
            entered_letter.append(answer)
            death_count+=1
            print(*skull_art[0:death_count*life_times],sep='\n')

        print(*current_answer)
            
        if current_answer == chosen_word_list:
            print(win)
            break

        elif death_count == life:
            print(lose)
            break

    print(chosen_word)
    print(dictionary[chosen_word])
    yes_no=input('\nDo you wanna go again?[Y/N]\n').upper().strip()
    if yes_no == 'Y':pass
    elif yes_no == 'N':break
    else:
        print('\nERROR! SHUTTING DOWN')
        break






























