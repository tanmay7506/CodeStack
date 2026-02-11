'''
Consider a class named Word that is given to you as a part of the prefix code. Your task is to create an object of the class by accepting input from the console.
The first line of input is a word. The second line of input is its part of speech.

(1) Create an object of the class Word and name it word using the values that you have accepted as input.

(2) Call the method print_info using this object.
'''

class Word:
    count = 0
    def __init__(self, word, pos):
        Word.count += 1
        self.word = word
        self.pos = pos

    def print_info(self):
        print(f'The word is "{self.word}" and its part of speech is "{self.pos}".')
