# print("hello world")
path_to_file = "books/frankenstein.txt"
def spitOutText(path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)

def word_count(path):
    with open(path) as f:
        words = f.read().split()
        # print(words) # This makes chaos of "words" variables
        return len(words)

def count_char(path):
    with open(path) as f:
        chars = f.read()
        return len(chars)
    
def countLetters(path):
    # Dictionary to hold the count of each letter
    letter_count = {}

    # Open and read the file
    with open(path) as f:
        file_contents = f.read().lower()  # Convert to lowercase for uniformity

    # Count each letter
    for char in file_contents:
        if char.isalpha():  # Check if the character is a letter
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Print the report
    for letter, count in sorted(letter_count.items()):
        print(f"Letter '{letter}' is counted {count} times")

    
if __name__ == "__main__":
    # spitOutText("books/frankenstein.txt")
    print(word_count(path_to_file))
    print(count_char(path_to_file))
    print(countLetters(path_to_file))
    # print("I LOVE YOU ANNI")