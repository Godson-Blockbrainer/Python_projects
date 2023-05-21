# A python program that counts the number of lettters in  a sentence and displays the result
#using .isalpha and .isdigit funtions

def count_this_sentence(sentence): # set the function for the enitre program action which is to count digits and letters in a sentence
    # initialze the agents that will do the counting 
    no_of_letter= 0. 
    no_of_digits= 0
     # using for loops to iterate every character in ther sentence
    for c in sentence:   
        if c.isalpha(): 
            no_of_letter += 1
        elif c.isdigit():
            no_of_digits += 1
             
    return no_of_digits, no_of_letter # we are returning the values that this agents holds. 

sentence = input("Insert any statement that includes a number: ") # lets ask our user to input a sentence we a number character in it 

letters, digits = count_this_sentence(sentence) # calling the function to take action on the value in the sentence variable and assiged its results to letters and digits 

# printing the value 
print("LETTERS", letters)
print("DIGITS", digits)
