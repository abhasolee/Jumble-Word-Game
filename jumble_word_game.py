from tkinter import *
import random


# Configuring window
width = 600
height = 400
root = Tk()
root.title("Jumble Word Game")
root.geometry('{}x{}'.format(width, height))


# Function to generate jumble words
def generate():
    jumbled = []
    global generated_word
    generated_word = " "

    # Selecting a random word from list
    global random_word
    random_word = random.choice(words)

    # Creating the hint list
    global hint_list
    hint_list = list(random_word)

    # Sepearing the alphabets in a new list
    for word in random_word:
        jumbled.append(word)

    # Shuffling the new list
    random.shuffle(jumbled)

    # Generating the new jumbled word
    for jumbled_word in jumbled:
        generated_word += jumbled_word.lower()


# Function to check answer
def check_answer():
    if answer_box.get().title() == random_word:
        result_label.config(text="Correct Answer")

        # Call generate function to generate new word
        generate()

        # Displaying the word
        word_label.config(text=generated_word)

        # Deleting the contents of entry box
        answer_box.delete(0, END)

    else:
        result_label.config(text="You are Incorrect")


# Function to generate next word
def next_word():
    # Call generate function generate new word
    generate()

    # Displaying the word
    word_label.config(text=generated_word)


# Function to display hint
def hint():
    for word in hint_list:
        # Get the previous label text and add it to the new letter
        hint_label.config(text=hint_label.cget('text') + word)
        # Remove the letter from the list
        hint_list.remove(word)
        break


# Function to show the game
def play():
    # Deleting widgets of body frame
    for child in body_frame.winfo_children():
        child.destroy()

    # Calling the generate function to generate random word
    generate()

    # Create label to display word
    global word_label
    word_label = Label(body_frame, text=generated_word, font=(
        'Coves', 35, 'bold'), fg="#2d545e")
    word_label.grid(row=0, column=0, columnspan=3, pady=10)

    # Create entry box and label to answer
    answer_label = Label(body_frame, text="Enter Answer",
                         font=('The Hills PERSONAL USE ONLY', 28))
    answer_label.grid(row=1, column=0)

    global answer_box
    answer_box = Entry(body_frame, width=25)
    answer_box.grid(row=1, column=1)

    # Create buttons
    submit_button = Button(body_frame, text="Submit", font=(
        'Kandira PERSONAL', 16, 'bold'), fg="#12343b", command=check_answer)
    submit_button.grid(row=2, column=0, pady=10)

    next_button = Button(body_frame, text="Next Word", font=(
        'Kandira PERSONAL', 16, 'bold'), fg="#12343b", command=next_word)
    next_button.grid(row=2, column=1, pady=10)

    hint_button = Button(body_frame, text="Hint", font=(
        'Kandira PERSONAL', 16, 'bold'), fg="#12343b", command=hint)
    hint_button.grid(row=2, column=2, pady=10)

    exit_button = Button(body_frame, text="Exit", font=(
        'Kandira PERSONAL', 16, 'bold'), fg="#12343b", command=root.quit)
    exit_button.grid(row=3, column=0, columnspan=3, pady=5)

    # Create result label
    global result_label
    result_label = Label(body_frame, font=('Adrenaline', 25), fg="#a0d2eb")
    result_label.grid(row=4, column=0, columnspan=3, pady=10)

    global hint_label
    hint_label = Label(body_frame, font=('Coves', 25, 'bold'), fg="#7d3cff")
    hint_label.grid(row=5, column=0, columnspan=3)



# Creating list of word
words = ['Hashirama', 'Tobirama', 'Hiruzen', 'Minato', 'Sasuke',
         'Nagato', 'Madara', 'Obito', 'Momoshiki', 'Shikamaru']

# Creating a title frame
title_frame = Frame(root, width=600, height=80)
title_frame.grid(row=0, column=0, pady=10)

# Create title label
title_label = Label(title_frame, text="JUMBLEE", font=(
    'Beach Society', 40), fg="#beef00")
title_label.place(x=width / 2, y=25, anchor=CENTER)

# Creating body frame
body_frame = Frame(root, width=600, height=300)
body_frame.grid(row=1, column=0)

# Create welcome label
welcome_label = Label(body_frame, text="Welcome to Jumblee",
                      font=('Beauty Mountains Personal Use', 30), fg="#1400c6")
welcome_label.grid(row=0, column=0)

# Creating play button
play_button = Button(body_frame, text="Play", font=(
    'Kandira PERSONAL', 18, 'bold'), width=2, fg="#657a00", command=play)
play_button.grid(row=1, column=0, pady=10)

root.mainloop()
