"""
This program will:
1) read in a poem
2) reverse it
3) change the periods to exclamation points
4) change the word woods to house
5) add some comments to the bottom
6) print both the original and edited poems to the screen
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
    except FileNotFoundError:
        print("File not found")
    return poem_lines

# Prints the poem to the scree.
# It is used twice: once for the original and once for the remix
def print_poem(doc_filename):
    full_path = os.path.join(DOCS_DIR, doc_filename)
    with open(full_path, "r") as f:
        for line in f:
            print(line)

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
    load_poem_list("Poem.txt")
    print("\n" + "------------Original Poem:-------------" + "\n")
    print_poem("Poem.txt")
    reverse_poem(poem_lines)
    write_new_poem(reversed_lines)
    print("\n" + "-------------Remixed Poem:--------------" + "\n")
    print_poem( "poem_remix.txt")

    append_comments()

# calls main
if __name__ == "__main__":
    main()
