print("Let's try this word counter that counts the number of words in a file. \n")

def word_counter(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            print(words)
            print("\nTotal number of words:", len(words))
    except FileNotFoundError:
        print("Oops!!! File not found.")

word_counter('file.txt')
