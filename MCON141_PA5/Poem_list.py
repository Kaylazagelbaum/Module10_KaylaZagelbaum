"""
This program will read through a poem, reverse it, change the periods to exclamation points,
change the word woods to house, and add some comments to the bottom.
"""

import os

DOCS_DIR = "docs"


# Reads the code and saves it as a list
def load_poem_list(doc_filename):
    global poem_lines
    poem_lines = []
    # read in the original poem and save it as a list
    try:
        full_path = os.path.join(DOCS_DIR, doc_filename)
        with open(full_path, "r") as f:
            for line in f:
                line = line.strip()
                if line != "":
                    poem_lines.append(line)
                    print(line)  # prints the poem to the screen
    except FileNotFoundError:
        print("File not found")
    return poem_lines


# Reverses the lines and saves a new list
def reverse_poem(poem_lines):
    global reversed_lines
    reversed_lines = poem_lines[::-1]
    # Reverses the list and saves as a new list
    return reversed_lines


# Writes the reversed list into a new file
def write_new_poem(reversed_lines, doc_filename="poem_remix.txt"):
    full_path = os.path.join(DOCS_DIR, doc_filename)
    try:
        with open(full_path, "w") as f:
            for line in reversed_lines:
                f.write(line.replace("woods", "house").replace(".", "!") + "\n")
                print(line)     # prints the new poem to the screen
    except FileNotFoundError:
        print("File not found")
    return reversed_lines


# Appends my comments to the reversed poem
def append_comments(doc_filename="poem_remix.txt"):
    load_poem_list(doc_filename)
    full_path = os.path.join(DOCS_DIR, doc_filename)
    try:
        with open(full_path, "a") as f:
            f.write(" \n I love this poem because of its soothing melody and brilliant rhyme scheme. \n "
                    "Notice how (in the original poem) the third line of each stanza rhymes with the first, second, and fourth of the next stanza. It is a work of genius.")
            f.write("\n Appended by Kayla Zagelbaum.")
            f.write("\n I changed woods to house and the periods to exclamation points.")
    except FileNotFoundError:
        print("File not found")


# Organizes the functions into a main function
def main():
    print("\n" + "Original Poem:" + "\n")
    load_poem_list("Poem.txt")
    reverse_poem(poem_lines)
    print("\n" + "Remixed Poem:" + "\n")
    write_new_poem(reversed_lines)

    append_comments()

# calls main
if __name__ == "__main__":
    main()
