# Dictionaries is no order, we index the thing in the dictionary with a lookup tag
bag = {} # or bag =dict()
bag['money'] = 12
bag['candy'] =10
bag['tissues'] =3
print('Print all method of the dictionary',dir(bag))
# Print all value in the dict
print("Dictionary of bag:", bag)
#Get value by the lookup tag
print('Print value in the money: ', bag['money'])
# Can add the value 
print('Print value + 2 in the money: ', bag['money']+2)

