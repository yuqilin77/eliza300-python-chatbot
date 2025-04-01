'''
Intent: Get complaint_types and key_words from local ElizaData.txt
Precondition =========

ElizaData.txt is a local file consisting of paragraphs of the form
On first line: 'Key Words for '<phrase describing a complaint category>
On second line: <words, separated by blanks, that may occur within a
description of the corresponding category>

Example of ElizaData.txt:

Key Words for Depression
depress sad

Key Words for Human Relations
conflict argument mistreat

Postconditions =========

(1) complaint_types = list of the phrases in ElizaData.txt describing all
complaint categories
{2) key_words = list of lists of words in ElizaData.txt that may occur
within phrases that describe the corresponding complaint category
'''

from eliza300_5_runtime_data import read_complaint_data
from eliza300_5_functions import get_complaint_type

read_complaint_data()
print("Thank you for using Eliza300, a fun therapy program.\n\
Please state your complaint:")
a_user_complaint = input()
observed_complaint_type1 = get_complaint_type(a_user_complaint)

advice_per_type = [
['Get out more.', 'Take up a hobby that you love.'],
["Don't expect too much of people.", "Don't take offence easily."],
['Get counseling.', "Don't delay action on counseling."]]
for element in observed_complaint_type1:
        for element1 in advice_per_type[element]:
                print(element1)




    
