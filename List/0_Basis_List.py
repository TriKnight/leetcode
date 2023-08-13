# List is the kind of collection ["A", "B", "C"]
# List can include another List [ 1, [2, 3], 4]
from typing import List

# 1. List can mutable
fruit = ['Banana'] # -> Example List can mutable
fruit[0]='b'
print('1. print the value of fruit ',fruit) #-> print: ['b']

fruit = 'Banana' # -> Example List can mutable
#fruit[0]='b'
#print('print: ',fruit) #-> TypeError: 'str' object does not support item assignment

# range() function returns the List of numbers from 0 to less than the parameter

# 2. Append function to add more value
stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')
print("2. Print the stuff list after append(): ", stuff)

# 3. Check elements in the list
nums = [ 1, 2 , 3, 4, 5]
print('3.1 Check number 1 in the List: ', 1 in nums ) #-> True
print('3.2 Check number 9 in the List: ', 9 in nums ) #-> False
print('3.3 Check number 9 in NOT the List: ', 9 not in nums ) #-> True

# 4. Change order by using sort() method
nums = [3, 2, 4, 5, 8, 1, 6]
text = ['Banana', 'Apple', 'Carrot', 'Strawberry', 'BlueBerry']
text.sort()
print("4. The text order after sort: ", text)

# 5. Min max function in List
print('Len of list', len(nums))
print('Max value in list', max(nums))
print('Min value in list', min(nums))
print('Sum all values in list', sum(nums))

# 6. Convert from String to List
abc = 'Apple is good for health'
list_abc = abc.split()
print('Convert from String to List:' , list_abc)

abc_comma = 'Apple, is, good,for,health'
list_abc = abc_comma.split(',')
print('Convert from String to List with comma:' , list_abc)