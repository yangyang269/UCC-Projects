# To start off, I will declare a loop which will basically determine whether or not the code loops again.
# I ask the user at the end of my code if they want to play again so this wants_to_play_again variable will change depending on their answer
#This variable needs to be True to begin with so I can just redeclare it as False if the user chooses not to play again

wants_to_play_again = True

# Here we see the loop in action

while wants_to_play_again == True:

    # I will introduce and greet the user with a nice text image

    print('''██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ██╗   ██╗ ██████╗ ██╗   ██╗██████╗      ██████╗  █████╗ ███╗   ███╗███████╗██╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██║
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║     ╚████╔╝ ██║   ██║██║   ██║██████╔╝    ██║  ███╗███████║██╔████╔██║█████╗  ██║
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║      ╚██╔╝  ██║   ██║██║   ██║██╔══██╗    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚═╝
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗██╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝
                                                                                                                                                                      ''')

    # Here I will ask the user for their first name and last name.
    # I ask the user for their last name in case they obtain a score high enough to be put on the leaderboard.

    name = str(input("Hello! Welcome to your game. What is your first name?"))

    last_name = str(input("Hello! Welcome to your game. What is your last name?"))

    # Here I just quickly convert the names into capitalized names and save them
    name = name.title()
    last_name = last_name.title()

    print(f"Hello {name.title()}. Welcome to your game.")

    # The valid_knows_how_to_play_answer is the loop variable. It determines when the loop is going to stop.
    # The loop will stop when the user enters a valid input for an answer to the question.
    # If the code does not receive a valid answer, it will repeat the question and instruct the user to give a proper answer.
    valid_knows_how_to_play_answer = False

    while valid_knows_how_to_play_answer == False:
        # I am asking the user if they understand the backstory and storing that answer in a variable.
        knows_how_to_play = input('''\nDo you know how to play this game and understand the backstory of Jabari Jumps?
        Please press 1 if you know how to play.
        Please press 2 if you don't know how to play.''')

        try:
            # I use a try statement to try and convert the knows_how_to_play input into a integer.
            # This will allow me to find out if the user has entered a random string of text into the terminal.

            knows_how_to_play = int(knows_how_to_play)

            #The next line will ensure that the program understands the user input. The user will have to enter 1 or 2 to proceed.
            if knows_how_to_play == 1 or knows_how_to_play == 2:
                # Now the loop variable is set to True so the loop stops.
                # You will see this structure of the try and except statement combined with a while loop in all of my questions in the code
                valid_knows_how_to_play_answer = True
            else:
                # If the answer the user gave is not 1 or 2 which selects an option, I must be able to ask the question again to get a understandable input.
                # For example if the user enters 9 into the terminal, the program will not understand.
                # This is why I have this else statement here, to catch for that specific error, and to ask the question again in case it happens.
                print("\nPlease enter only 1 or 2 to select an option.")

        except ValueError:
            # I am excepting a ValueError, in case the user enters a random string into the terminal that cannot be converted into an integer in the try step above.
            print("\nPlease only type 1 or 2 indicating which option you want to choose.")

    if knows_how_to_play == 1:
        # Once I have the right user input, I can now interpret it. and give the user the right accommodation.
        # If they understand the backstory and how to play, the game will begin right away.
        print("Wonderful! Your game will begin now.")
    else:
        # If the user does not know how to play, I will go over the instructions of the game.

        print("\nWelcome to the game! Instructions will appear on screen now.")
        print('''Here are your instructions:
        \nIn this game, there will be questions popping up on screen which you will need to answer to get points. 
        The end goal is to obviously end with as most points as possible.
        To answer questions, you will be prompted by multiple choice questions. 
        You will answer by eiether typing 1, 2, 3 or 4, each corresponding to an answer. 
        When you want to submit your answer, simply press enter.
        Let's explore this through an example question. 
        \nHow are you feeling today?
            1. Happy
            2. Sad
            3. Excited
            4. Something else.
        To choose an answer, just type the number corresponding to your answer.
        If you are happy, you would type 1 to answer. ''')

        # Now I am going to ask the user if they know the backstory of the book Jabari jumps.
        # The game is based off of the book so the user needs to understand the backstory to play
        # You will see the same while loop, try and except statement structure that was introduced in the first question about the user knowing how to play.

        valid_knows_backstory_answer = False

        while valid_knows_backstory_answer == False:

            knows_backstory = input('''\nDo you know the backstory of the book Jabari Jumps?
            Press 1 if you know the backstory.
            Press 2 if you don't.''')

            try:
                knows_backstory = int(knows_backstory)
                if knows_backstory == 1 or knows_backstory == 2:
                    valid_knows_backstory_answer = True
                else:
                    print("\nPlease enter only 1 or 2 to select an option.")

            except ValueError:
                print("\nPlease only enter 1 or 2 to select an option.")

        if knows_backstory == 1:

            valid_wants_practice_game_answer = False

            # You will see the question structure of the loop with try and except statements everywhere. Sometimes even contained within questions.
            # I am asking the user if they want a practice game here

            while valid_wants_practice_game_answer == False:
                wants_practice_game = input('''\nAmazing! Would you like to try a practice level before we get started with the main game?
                Please press 1 if you want a practice level.
                Please press 2 if you want to head straight to the game.''')

                try:
                    wants_practice_game = int(wants_practice_game)

                    if wants_practice_game == 1 or wants_practice_game == 2:
                        valid_knows_backstory_answer = True
                    else:
                        print("Please enter only 1 or 2 to select an option.")

                except ValueError:
                    print("Please only enter 1 or 2 to select an option.")

            if wants_practice_game == 1:

                # If the user wants a practice game, I will give them a simple game where they can practice the commands.
                print('''\nGreat! Let's get started with the practice game.''')

                valid_answer = False

                print("Here comes the first question.")

                # The question structure appears again, this time to actually ask the game questions
                # The loop variable in this case is named valid_answer

                while valid_answer == False:
                    answer = input('''\nWhat is the answer to 2 + 2??
                        1. 4
                        2. 5
                        3. 3
                        4. 1
                    Please enter the number corresponding to your answer.''')

                    try:
                        answer = int(answer)
                        if 4 >= int(answer) and int(answer) >= 0:
                            valid_answer = True
                        else:
                            print("\nPlease enter only 1, 2, 3, or 4 to select an option.")

                    except ValueError:
                        print("\nPlease only enter 1, 2, 3, or 4 to select an option.")

                if answer == 1:
                    print('''\nCorrect! That question was correct. When we play, you can choose whether or not you want to play with points.
                    If you chose to play with points, you would have 3 points because you answered that question correctly. 
                    For the practice level,we won't keep track of points.''')

                else:
                    print("\nSorry but that is not quite the answer. The correct answer was 4.")

                # Notice how I do not use a different loop variable for each of the questions. I just recycle one variable.
                # To recycle this variable, I make sure to redeclare it False at the beginning of every question.
                valid_answer = False

                print("Alright. It's time for the second question.")

                while valid_answer == False:
                    answer = input('''\nWhat is 3 x 4?
                        1. 4
                        2. 3
                        3. 12
                        4. 76
                    Please enter the number corresponding to your answer.''')

                    try:
                        answer = int(answer)
                        if 4 >= int(answer) and int(answer) >= 0:
                            valid_answer = True
                        else:
                            print("\nPlease enter only 1, 2, 3, or 4 to select an option.")

                    except ValueError:
                        print("\nPlease only enter 1, 2, 3, or 4 to select an option.")

                if answer == 3:
                    print("\nCorrect! I think that you are now ready to play the game. Let's get on with that!")

                else:
                    print("\nSorry but that is not quite the answer. The correct answer was 12")

            else:

                # There is a lot of if and else statements in this introduction piece of the code.
                # This is actually the else from the would you like a practice game question.
                # If the user would not like a practice game, the game begins.

                print("\nLet's get started with the main game!")
        else:

            # This else statement is from the do you know the backstory question.
            # If the user does not know the backstory, I will link them a YouTube read aloud where can listen to the book.

            print('''\nAlright! Let's cover the backstory quickly.
            If you go to this link: https://www.youtube.com/watch?v=hwXKM7cyYGM&ab_channel=RooftopKid, you will find a read aloud.
            Listen to the read aloud and come back to the game when you are done. It's a quick video I promise.''')

            # The same question structure that we all know and love appears again

            valid_answer = False

            while valid_answer == False:

                # This is me offering the user a practice level if the user did not understand the backstory of the game.
                # The practice level is identical to the one we just explored above.
                # The practice level above was offered to users who understood the backstory.
                # Note how even though the user could choose differnt answers to the question do you understand the backstory,
                # they can both lead to the practice level if the user chooses.

                wants_practice_game = input('''\nAnswer this question when you are done the readaloud but would you like to play a practice level?
                Please press 1 if you want a practice level.
                Please press 2 if you want to head straight to the the game.''')

                try:
                    wants_practice_game = int(wants_practice_game)
                    if wants_practice_game == 1 or wants_practice_game == 2:
                        valid_answer = True
                    else:
                        print("\nPlease enter only 1 or 2 to select an option.")

                except ValueError:
                    print("\nPlease only enter 1 or 2 to select an option.")

            if wants_practice_game == 1:

                print('''\nGreat! Let's get started with the practice game.''')

                valid_answer = False

                while valid_answer == False:
                    answer = input('''\nWhat is the answer to 2 + 2??
                    1. 4
                    2. 5
                    3. 3
                    4. 1
                    Please enter the number corresponding to your answer. To submit your answer, simply press enter after your number.''')

                    try:
                        answer = int(answer)
                        if 4 >= int(answer) and int(answer) >= 0:
                            valid_answer = True
                        else:
                            print("\nPlease enter only 1, 2, 3, or 4 to select an option.")

                    except ValueError:
                        print("\nPlease only enter 1, 2, 3, or 4 to select an option.")

                if answer == 1:
                    print('''\nCorrect! That question was correct. When we play, you can choose whether or not you want to play with points.
If you chose to play with points, you would have 3 points because you answered that question correctly. 
For the practice level,we won't keep track of points.''')

                else:
                    print("\nSorry but that is not quite the answer. The correct answer was 4.")

                print("\nAlright time for your second question!")

                valid_answer = False

                while valid_answer == False:
                    answer = input('''\nWhat is 3 x 4?
                    1. 4
                    2. 3
                    3. 12
                    4. 76
                    Please enter the number corresponding to your answer.''')

                    try:
                        answer = int(answer)
                        if 4 >= int(answer) and int(answer) >= 0:
                            valid_answer = True
                        else:
                            print("\nPlease enter only 1, 2, 3, or 4 to select an option.")

                    except ValueError:
                        print("\nPlease only enter 1, 2, 3, or 4 to select an option.")

                if answer == 3:
                    print('''\nCorrect! I think that you are now ready to play the game. Let's get on with that!''')
                else:
                    print("\nSorry but that is not quite the answer. The correct answer was 12")

    # After the practice level, it is not time to play the actual game.

    print("\nNow let's get started with the game!")

    # Here I lay out 3 of the most important variables I have in my game.
    # The user will have a choice whether or not to count points in their game to have a competitive and non-competitive experience
    # As you can guess, total_points calculates the total amount of points the user has.
    # transfer_points if a transfer variable so I can get the number of points the user has at the end of each question into the next.
    # Because each question is in its each respective definition, I need a transfer variable to get the point amount from one definition
    # to the next.
    # Finally, wants_to_count_points is a boolean which basically equals True or False depending if the user wants to play with points or not.

    total_points = int
    transfer_points = int
    wants_to_count_points = bool

    # We will now begin with the first question
    # Let's take a closer look at the first quetsion

    def question1():
        # Right off the bat, I will globalize all of my variables, so they can be accessed in the following definitions oft the other questions.

        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        # You will see here that I initialize all of my variables. want_to_count_points is defined False to begin with.

        total_points = 0
        transfer_points = 0
        wants_to_count_points = False

        # Firstly I will ask the user if they would like to count points using the question structure we are very familiar with now.

        valid_wants_to_count_points_answer = False

        while valid_wants_to_count_points_answer == False:
            want_to_count_points_integer = input('''\nWould you like to keep track of points while we play?
                Please type 1 if you would like to play with points
                Please type 2 if you would not like to play with points''')

            try:
                want_to_count_points_integer = int(want_to_count_points_integer)
                if want_to_count_points_integer == 1 or want_to_count_points_integer == 2:
                    valid_wants_to_count_points_answer = True
                else:
                    print("Please only enter 1 or 2 to select an option.")
            except ValueError:
                print("Please only enter 1 or 2 to select an option.")

        if want_to_count_points_integer == 1:
            want_to_count_points = True
        else:
            want_to_count_points = False

        # After asking the user if they would like to play with points, I ask the user if they would like to play in easy, medium, or hard mode
        # All the difficulty options are False, so they can be turned to be True later on

        valid_difficulty_level_answer = False
        wants_easy_mode = False
        wants_medium_mode = False
        wants_hard_mode = False

        while valid_difficulty_level_answer == False:
            difficulty_level = input('''Would you like to play easy, medium, or hard mode?
                Please type 1 if you would like to play on easy mode.
                Please type 2 if you would like to play on medium mode.
                Please type 3 if you would like to play on hard mode.''')

            try:
                difficulty_level = int(difficulty_level)
                if int(difficulty_level) == 1 or int(difficulty_level) == 2 or int(difficulty_level) == 3:
                    valid_difficulty_level_answer = True
                else:
                    print("Please only enter 1, 2, or 3 to select an option.")
            except ValueError:
                print("Please only enter 1, 2, or 3 to select an option.")

        if difficulty_level == 1:
            print("The game will proceed in easy mode.")
            wants_easy_mode = True
            wants_medium_mode = False
            wants_hard_mode = False
        elif difficulty_level == 2:
            print("The game will proceed in medium mode.")
            wants_medium_mode = True
            wants_easy_mode = False
            wants_hard_mode = False
        else:
            print("The game will proceed in hard mode.")
            wants_hard_mode = True
            wants_medium_mode = False
            wants_easy_mode = False

        # Now that I have the difficulty mode and know if the user wants to play with points, the fun can begin.

        print("\nYour first question will appear on screen now")

        # I start off each question with some more text art to keep the terminal interesting.

        print('''   ___                  _   _                 _  _   _ 
          / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_/ |
         | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _| |
         | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _| |
          \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_| |_|
                                                               ''')
        # All of my game questions use the standard question structure

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #1: Who is the main character of the book?
                    Answer 1: Jabari
                    Answer 2: Jabari's sister
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #1: Who is the main character of the book?
                    Answer 1: The Dad
                    Answer 2: Jabari
                    Answer 3: Jabari's sister
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #1: Who is the main character of the book?
                    Answer 1: The Dad
                    Answer 2: The Mom
                    Answer 3: Jabari
                    Answer 4: Jabari's sister
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            # The only thing that will be noticeably different about the following snipet of code and the regular
            # question strucutre is that I am accounting for all the answer responding to each of the modes.
            # It is nothing too special

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
    please just type 2 and then press enter. Please type a valid answer into the terminal this time.
    ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
    please just type 2 and then press enter. Please type a valid answer into the terminal this time.
    ''')

        # This next part basically accounts and calculates the answer to the question based off the difficulty the user selected

        if wants_easy_mode == True and int(answer1) == 1:

            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_medium_mode == True and int(answer1) == 2:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_hard_mode == True and int(answer1) == 3:
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")

    # From now on, I basically just follow the stucture outlined in question 1 without asking the user for the difficulty level and if they want to play with points


    def question2():

        # I globalize my important variables again, I do so at the beginning of every question

        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        # You will notice that everything is layed out just like the last question

        print("Now on to question 1.")

        print('''   ___                  _   _                 _  _  ____  
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || ||___ \ 
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _|__) |
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _/ __/ 
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_||_____|
                                                                      ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #2: Where is Jabari and his family?
                    Answer 1: The Swimming Pool
                    Answer 2: His house
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #2: Where is Jabari and his family?
                    Answer 1: The Swimming Pool
                    Answer 2: The Gym
                    Answer 3: His house
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #2: Where is Jabari and his family?
                    Answer 1: The Swimming Pool
                    Answer 2: The Gym
                    Answer 3: His house
                    Answer 4: His friend's house
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        if wants_easy_mode == True and int(answer1) == 1:

            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_medium_mode == True and int(answer1) == 1:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_hard_mode == True and int(answer1) == 1:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")


    def question3():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Now for question 3!")

        print('''   ___                  _   _                 _  _  _____ 
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || ||___ / 
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _||_ \ 
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _|__) |
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_||____/ 
                                                                      ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #3: What is Jabari going to attempt in this story?
                    Answer 1: To shoot a basketball
                    Answer 2: To jump off jumping board
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #3: What is Jabari going to attempt in this story?
                    Answer 1: To shoot a basketball
                    Answer 2: To jump off jumping board
                    Answer 3: To ride a bike
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #3: What is Jabari going to attempt in this story?
                    Answer 1: To shoot a basketball
                    Answer 2: To jump off jumping board
                    Answer 3: To ride a bike
                    Answer 4: To swing a bat
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        if wants_easy_mode == True and int(answer1) == 2:

            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_medium_mode == True and int(answer1) == 2:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_hard_mode == True and int(answer1) == 2:
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")


    def question4():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Time for question 4!")

        print('''   ___                  _   _                 _  _   _  _   
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_| || |  
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _| || |_ 
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _|__   _|
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_|    |_|  
                                                                        ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #4: How does Jabari feel about jumping off the diving board?
                    Answer 1: Happy
                    Answer 2: Excited
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #4: How does Jabari feel about jumping off the diving board?
                    Answer 1: Tired
                    Answer 2: Happy
                    Answer 3: Excited
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #4: How does Jabari feel about jumping off the diving board?
                    Answer 1: Tired
                    Answer 2: Happy
                    Answer 3: Excited
                    Answer 4: Nervous
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        if wants_easy_mode == True and int(answer1) == 2:

            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_medium_mode == True and int(answer1) == 3:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_hard_mode == True and int(answer1) == 3:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")

# Question 5 is the first True or False question

    def question5():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Now time for question 5!")

        print('''   ___                  _   _                 _  _   ____  
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_| ___| 
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _|___ \ 
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _|___) |
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_| |____/ 
                                                                       ''')

        # The only thing differnt with this question is that it is a True or False question, meaning that all of
        # the difficulty modes will be answering the same question with the same amount of answer options

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #5: Does Jabari come back down after he climbs the ladder to the diving board the first time?
                    Answer 1: True
                    Answer 2: False
    
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #5: Does Jabari come back down after he climbs the ladder to the diving board the first time?
                    Answer 1: True
                    Answer 2: False
    
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #5: Does Jabari come back down after he climbs the ladder to the diving board the first time?
                    Answer 1: True
                    Answer 2: False
    
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        if wants_easy_mode == True and int(answer1) == 1:

            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_medium_mode == True and int(answer1) == 1:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_hard_mode == True and int(answer1) == 1:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")


    def question6():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Time for question 6!")

        print('''   ___                  _   _                 _  _    __   
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_ / /_  
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _| '_ \ 
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _| (_) |
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_|  \___/ 
                                                                       ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #6: Why doest Jabari climb back down the ladder?
                    Answer 1: Because he was tired
                    Answer 2: Because he wanted to leave
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #6: Why doest Jabari climb back down the ladder?
                    Answer 1: Because he wanted to swim instead
                    Answer 2: Because he was tired
                    Answer 3: Because he wanted to leave
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #6: Why doest Jabari climb back down the ladder?
                    Answer 1: Because he wanted to swim instead
                    Answer 2: Because he was excited
                    Answer 3: Because he was tired
                    Answer 4: Because he wanted to leave
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        if wants_easy_mode == True and int(answer1) == 1:

            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_medium_mode == True and int(answer1) == 2:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_hard_mode == True and int(answer1) == 3:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")


    def question7():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Let's move on to question 7!")

        print('''   ___                  _   _                 _  _  _____ 
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || ||___  |
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _| / / 
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _|/ /  
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_| /_/   
                                                                      ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #7: What does Jabari do after climbing down tha ladder?
                    Answer 1: He waits
                    Answer 2: He remembers that he needs to stretch
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #7: What does Jabari do after climbing down tha ladder?
                    Answer 1: He remembers that he needs to stretch
                    Answer 2: He goes for a swim in the pool
                    Answer 3: He waits
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #7: What does Jabari do after climbing down tha ladder?
                    Answer 1: He waits
                    Answer 2: He leaves with his family
                    Answer 3: He goes for a swim in the pool
                    Answer 4: He remembers that he needs to stretch
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        if wants_easy_mode == True and int(answer1) == 2:

            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_medium_mode == True and int(answer1) == 1:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        elif wants_hard_mode == True and int(answer1) == 4:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")

# I decided to have some fun here so I made Question 8 a special question.
# Question 8 is basically a question where all the options are correct, meaning the user
# is guaranteed to earn points if they decided to play with points. Sort of like a Kahoot powerup or something

    def question8():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Time for question 8!")

        print('''   ___                  _   _                 _  _    ___  
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_ ( _ ) 
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _|/ _ \ 
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _| (_) |
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_|  \___/ 
                                                                       ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #8: After Jabari climbs down, he talks with his dad.
                    What advice does his did offer?
                    Answer 1: Facing your fears gives you suprises.
                    Answer 2: That feeling scared is normal.
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #8: After Jabari climbs down, he talks with his dad.
                    What advice does his did offer?
                    Answer 1: Facing your fears gives you suprises.
                    Answer 2: That feeling scared is normal.
                    Answer 3: Trying new things are hard.
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #8: After Jabari climbs down, he talks with his dad.
                    What advice does his did offer?
                    Answer 1: Facing your fears gives you suprises.
                    Answer 2: That feeling scared is normal.
                    Answer 3: That it's okay to be a little scared. Taking a deep breath helps sometimes.
                    Answer 4: Trying new things are hard.
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        if wants_easy_mode == True:
            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_medium_mode == True:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_hard_mode == True:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")


    def question9():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Now time for question 9!")

        print('''   ___                  _   _                 _  _    ___  
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_ / _ \ 
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _| (_) |
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _|\__, |
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_|    /_/ 
                                                                       ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #9: What does Jabari do after talking with his dad?
                    Answer 1: Make his way up the ladder and to the edge of the diving board.
                    Answer 2: Decide to try the diving board again another day
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #9: What does Jabari do after talking with his dad?
                    Answer 1: Make his way up the ladder and to the edge of the diving board.
                    Answer 2: Decide that it is still to scary and give up.
                    Answer 3: Decide to try the diving board again another day
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #9: What does Jabari do after talking with his dad?
                    Answer 1: Decide to try the diving board another day.
                    Answer 2: Decide that it is still to scary and give up.
                    Answer 3: Make his way up the ladder and to the edge of the diving board.
                    Answer 4: Go swimming instead.
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        if wants_easy_mode == True and answer1 == 1:
            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_medium_mode == True and answer1 == 1:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_hard_mode == True and answer1 == 3:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")


    def question10():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Are you ready for quetion 10? Let's go!")

        print('''   ___                  _   _                 _  _   _  ___  
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_/ |/ _ \ 
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _| | | | |
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _| | |_| |
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_| |_|\___/ 
                                                                         ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #10: What does Jabari say before jumping off the board?
                    Answer 1: I'm scared
                    Answer 2: I love surprises.
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #10: What does Jabari say before jumping off the board?
                    Answer 1: I'm scared
                    Answer 2: Oh no!
                    Answer 3: I love surprises.
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #10: What does Jabari say before jumping off the board?
                    Answer 1: I love surprises.
                    Answer 2: I'm scared
                    Answer 3: Oh no!
                    Answer 4: Hi!
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        if wants_easy_mode == True and answer1 == 2:
            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_medium_mode == True and answer1 == 3:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_hard_mode == True and answer1 == 1:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")

# Question 11 is the second True or False question

    def question11():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Get ready for question 11!")

        print('''   ___                  _   _                 _  _   _ _ 
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_/ / |
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _| | |
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _| | |
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_| |_|_|
                                                                     ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #11: Does Jabari jump off of the board?
                    Answer 1: Yes
                    Answer 2: No
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #11: Does Jabari jump off of the board?
                    Answer 1: Yes
                    Answer 2: No
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #11: Does Jabari jump off of the board?
                    Answer 1: Yes
                    Answer 2: No
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        if wants_easy_mode == True and answer1 == 1:
            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_medium_mode == True and answer1 == 1:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_hard_mode == True and answer1 == 1:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")


    def question12():
        global total_points
        global transfer_points
        global want_to_count_points
        global wants_easy_mode
        global wants_medium_mode
        global wants_hard_mode

        print("Let's finish off strong! Here comes your last question.")

        print('''   ___                  _   _                 _  _   _ ____  
              / _ \ _   _  ___  ___| |_(_) ___  _ __    _| || |_/ |___ \ 
             | | | | | | |/ _ \/ __| __| |/ _ \| '_ \  |_  ..  _| | __) |
             | |_| | |_| |  __/\__ \ |_| | (_) | | | | |_      _| |/ __/ 
              \__\_\\__,_|\___||___/\__|_|\___/|_| |_|   |_||_| |_|_____|
                                                                         ''')

        valid_answer = False

        while valid_answer == False:
            if wants_easy_mode == True:
                answer1 = input('''Question #12: How does Jabari feel after he has jumped off the board?
                    Answer 1: Sad
                    Answer 2: Amazing
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            elif wants_medium_mode == True:
                answer1 = input('''Question #12: How does Jabari feel after he has jumped off the board?
                    Answer 1: He doesn't feel anything.
                    Answer 2: Amazing
                    Answer 3: Sad
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            else:
                answer1 = input('''Question #12: How does Jabari feel after he has jumped off the board?
                    Answer 1: He doesn't feel anything.
                    Answer 2: Sad
                    Answer 3: Unhappy
                    Answer 4: Amazing
                    Please type the number coressponding to the answer you want to select.
                    For example, if you want to answer question 1, simply type 1 and press enter.''')

            try:
                answer1 = int(answer1)
                if wants_easy_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2:
                        valid_answer = True
                elif wants_medium_mode == True:
                    if int(answer1) == 1 or int(answer1) == 2 or int(answer1) == 3:
                        valid_answer = True
                elif wants_hard_mode == True:
                    if 4 >= int(answer1) and int(answer1) >= 0:
                        valid_answer = True
                else:
                    print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2,
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

            except ValueError:
                print('''\nPlease only enter a number corresponding to answer you want to select. For example, if you want to choose answer 2, 
        please just type 2 and then press enter. Please type a valid answer into the terminal this time.
        ''')

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        if wants_easy_mode == True and answer1 == 2:
            print("\nThat was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_medium_mode == True and answer1 == 2:

            print("That was correct! Congrajulations!")
            if want_to_count_points == True:
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        # I do not need to check if the user input is correct or not because this question is intended to have all
        # the answers to be correct. I already filter out all responses that are not 1, 2, 3, or 4 from the try and
        # except statements
        elif wants_hard_mode == True and answer1 == 4:
            if want_to_count_points == True:
                print("That was correct! Congrajulations!")
                total_points += 3
                print(f"\nYou have {total_points} points!")
                transfer_points = total_points

        else:
            print("\nSorry! That question was incorrect. Don't worry, there will be many other questions.")
            if want_to_count_points == True:
                total_points = 0
                transfer_points = total_points
                print(f"\nYou have {total_points} points!")


    # Here I will just call all the questions one by one in order
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    question7()
    question8()
    question9()
    question10()
    question11()
    question12()

    # This is where my outro will begin to kick in

    # You can see me declaring the important variables for the outro of the game
    # final_points will basically collect the amount of points the user ends with
    # display_score is a boolean variable, it turns True or False based off of the fact if the user wanted to play
    # with points or not.

    final_points = total_points
    display_score = wants_to_count_points

    print('''Congratulations! You've sucessfully completed the game!''')
    if display_score == True:
        print(f"You ended the game with {final_points} points.")
        print('''Here is where you rank among all the players that have played this game.''')

    # Here I create 3 dictionaries.
    # The following players did not play the game, but they were just created so the user has something to compare
    # their accomplishments to

    leaderboard_number_1 = {"first_name" : "George", "last_name" : "Wei", "score" : 20}
    leaderboard_number_2 = {"first_name" : "George", "last_name" : "Wei", "score" : 17}
    leaderboard_number_3 = {"first_name" : "Andy", "last_name" : "Yu", "score" : 16}

    # I then print the current leaderboard so the user knows if they achieved a socre high enough to be placed on the leaderbaodr.
    # THe leaderboard scores are not intended to be unbeatable, they are designed, so they are not hard to beat.
    # I want the user to feel accomplished after playing my game so hopefully if they understood the book well,
    # they will have landed on the leaderboard.

    print(f'''Current Leaderboard:
    1. {leaderboard_number_1["first_name"]} {leaderboard_number_1["last_name"]}: {leaderboard_number_1["score"]} points
    2. {leaderboard_number_2["first_name"]} {leaderboard_number_2["last_name"]}: {leaderboard_number_2["score"]} points
    3. {leaderboard_number_3["first_name"]} {leaderboard_number_3["last_name"]}: {leaderboard_number_3["score"]} points''')

    print(f"Your final score is {final_points}.")

    # I declare the 3 variables that will power the leaderboard which are basically booleans that turn on and if
    # depending on the place the user got compared to the 3 other scores

    got_first_place = False
    got_second_place = False
    got_third_place = False

    # I then compare the user's score to the score of each of the 3 users that I set.
    # I access the user's score by using a dictionary key
    # Being able to use a dictionary key is the reason that I used dictionaries to set the values for the leaderbaord

    if final_points > leaderboard_number_3["score"]:
        print('''This means...
        That since your score was higher than some of the scores on the leaderboard...
        You will now be on placed on the leaderboard!!!
        Amazing job! Well done!''')

        # I then turn on or off the booleans depending on which place they got

        if final_points > leaderboard_number_1["score"]:

            got_first_place = True
            got_second_place = False
            got_third_place = False

        if final_points > leaderboard_number_2["score"] and final_points < leaderboard_number_1["score"]:

            got_first_place = False
            got_second_place = True
            got_third_place = False

        if final_points > leaderboard_number_3["score"] and final_points < leaderboard_number_2["score"]:

            got_first_place = False
            got_second_place = False
            got_third_place = True

    # Next you will just see me printing the new leaderboards, depending on how well the user did

    if got_first_place == True:

        print(f'''Leaderboard:
        1. {name.title()} {last_name.title()}: {final_points} points
        2. {leaderboard_number_1["first_name"]} {leaderboard_number_1["last_name"]}: {leaderboard_number_1["score"]} points
        3. {leaderboard_number_2["first_name"]} {leaderboard_number_2["last_name"]}: {leaderboard_number_2["score"]} points''')

        print(f"Great job on your accomplishments {name}!")

    if got_second_place == True:

        print(f'''Leaderboard:
        1. {leaderboard_number_1["first_name"]} {leaderboard_number_1["last_name"]}: {leaderboard_number_1["score"]} points
        2. {name.title()} {last_name.title()}: {final_points} points
        3. {leaderboard_number_2["first_name"]} {leaderboard_number_2["last_name"]}: {leaderboard_number_2["score"]} points''')

        print(f"Great job on your accomplishments {name}!")

    if got_third_place == True:

        print(f'''Leaderboard:
        1. {leaderboard_number_1["first_name"]} {leaderboard_number_1["last_name"]}: {leaderboard_number_1["score"]} points
        2. {leaderboard_number_2["first_name"]} {leaderboard_number_2["last_name"]}: {leaderboard_number_2["score"]} points
        3. {name.title()} {last_name.title()}: {final_points} points''')

        print(f"Great job on your accomplishments {name}!")

    # The next part of my oiutro composes of a survey.
    # I ask the user to take a survey, so I as the game creator can receive some feedback
    # The survey is of course optional

    valid_wants_to_do_survey_answer = False

    # I use the standard question structure to get the answer to the survey question

    while valid_wants_to_do_survey_answer == False:
        wants_to_do_survey = input('''Amazing job on completing the game! Would you mind if you took a quick momment to do a survey for me?
        Please press 1 if you would love to help
        Please press 2 if you would rather do it another time''')

        try:
            wants_to_do_survey = int(wants_to_do_survey)
            if wants_to_do_survey == 1 or wants_to_do_survey == 2:
                valid_wants_to_do_survey_answer = True
            else:
                print("Please only enter 1 or 2 to select an option.")
        except ValueError:
            print("Please only enter 1 or 2 to select an option.")

    if wants_to_do_survey == 1:
        print('''Amazing! I'll give you the survey right now!
        Here is the link to the survey: https://docs.google.com/forms/d/1R4VzQmX_e1gFSBgIcX6NNqFL8TqXmxBuBoOJujBc5Ws/edit. 
        Please click on the link and answer the survey, when you are done, just come back to the game so we can finish up together.''')

    else:
        print('''Alright, you can do it another time.''')

    # Finally to end everything off, I ask the user if they would like to play again.
    # This is why all of my code is contained within a while loop which was set right away at the top of the code

    valid_wants_to_play_again_input_answer = False

    while valid_wants_to_play_again_input_answer == False:
        wants_to_play_again = input('''Thanks for playing! Would you like to play again?
        If you would like to play again, please type 1
        If you wouldn't like to play again, please type 2''')

        try:
            wants_to_play_again = int(wants_to_play_again)
            if wants_to_play_again == 1 or wants_to_play_again == 2:
                valid_wants_to_play_again_input_answer = True
            else:
                print("Please only enter 1 or 2 to select an option.")
        except ValueError:
            print("Please only enter 1 or 2 to select an option.")

    # If the user wants to play again, all I have to do is set the wants_to_play_again variable to True which
    # we set at the beginning of the code

    if wants_to_play_again == 1:
        wants_to_play_again = True
        print("That's amazing to hear! The game will restart now so you can play it again.")

    # If the user does not want to play again, I will just display a goodbye message

    else:
        wants_to_play_again = False
        print('''Ok. I hope that you will play this game again someday. Thank you for playing and I hope to see you later on.
        Goodbye for now, thanks again for playing.''')
        print(''' ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗███████╗██╗
██╔════╝ ██╔═══██╗██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║
██║  ███╗██║   ██║██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  ██║
██║   ██║██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗
 ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝
                                                               ''')