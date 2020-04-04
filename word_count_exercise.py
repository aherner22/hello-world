def count_words(filename):
    """Count the approximate words in a file."""

    try:
        with open(filename, encoding='utf-8') as f_obj:
          contents = f_obj.read()              #contents is a single string to start
    except FileNotFoundError:
        msg = f"Sorry, the file {filename} does not exist."
        print(msg)
        #pass
    else:                                   #count the number of words in the file        
        words = contents.split()            #split the string into a list of words
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

count_words("word_count_exercise.txt")