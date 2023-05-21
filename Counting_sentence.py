# A python program that counts the number of lettters in  a sentence and displays the result
#using .isalpha and .isdigit funtions

def count_this_sentence(sentence):
    no_of_letter= 0
    no_of_digits= 0
     
    for c in sentence:
        if c.isalpha():
            no_of_letter += 1
        elif c.isdigit():
            no_of_digits += 1
             
    return no_of_digits, no_of_letter

sentence = input("Insert any statement that includes a number: ")

letters, digits = count_this_sentence(sentence)

print("LETTERS", letters)
print("DIGITS", digits)
