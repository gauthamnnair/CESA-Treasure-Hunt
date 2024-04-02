import random
import csv


def find_character(season, episode, subtitle_section, word_number, character_number):
    filename = f"S0{season}E0{episode}.txt"  # Assuming subtitle files follow this naming convention

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return 0

    # Find the start index of the subtitle section
    index = 0
    while index < len(lines):
        if lines[index].strip() == str(subtitle_section):
            index += 2  # Move to the line containing the words
            break
        index += 1

    # If subtitle section not found
    if index == len(lines):
        print(f"Subtitle section {subtitle_section} not found in season {season}, episode {episode}.")
        return -1

    # Extract words from the specified lines
    words = []
    while index < len(lines) and lines[index].strip():
        words.extend(lines[index].split())
        index += 1

    print(f"Words in subtitle section {subtitle_section}: {words}")  # Debugging statement

    # Choose a valid word number
    if word_number <= 0 or word_number > len(words):
        print(f"Invalid word number: {word_number}, choosing randomly.")
        word_number = random.randint(1, len(words))  # Pick a random word number within range	

    chosen_word = words[word_number - 1]

    # Choose a valid character number
    if character_number <= 0 or character_number > len(chosen_word):
        print(f"Invalid character number: {character_number}, choosing randomly.")
        character_number = random.randint(1, len(chosen_word))  # Pick a random character number within range
    
    # Return the character at the specified position
    return chosen_word[character_number - 1]

# Example usage:
original_questions = ["314159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664"]
questions = []
passwords = []

for original_question in original_questions:
    password = ""
    question = ""
    for i in range(10):
        block = original_question[i*6 : (i+1)*6]  # Extract the current batch
        season = int(block[0]) % 5
        if season == 0:
            season = random.randint(1, 4)  # Random season between 1 and 4
        episode = int(block[1])
        if (season == 1 or season == 3) and episode == 9:
            episode = random.randint(1,8)        
        subtitle_section = int(block[2:4])
        if subtitle_section < 10:
            subtitle_section = int(block[3])
        word_number = int(block[4])
        character_number = int(block[5])
        character = find_character(season, episode, subtitle_section, word_number, character_number)
        if character != -1:
            password += str(character)
        else:
            # Replace '?' with a blank character
            password += "?"

        question += str(season) + str(episode) + str(subtitle_section) + str(word_number) + str(character_number) 
    questions.append(question)
    passwords.append(password)
    
with open('PDFs Encryption.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Question', 'Password'])
    for i in range(len(questions)):
        writer.writerow([questions[i], passwords[i]])

print("Data written to passwords.csv file.")

