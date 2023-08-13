from typing import List
"""
Basic Array Techniques
"""
class String:
    def loop(self, fruit:List[str]) -> List[str]:
        self.fruit = fruit
        for letter in fruit:
            print(letter)
            
    def slidingStr(self, fruit:List[str]) -> List[str]:
        self.fruit = fruit
        # String[from index : upto NOT including index]
        print(fruit[0:5]) # print -> Fresh
        print(fruit[6:12]) # print -> banana
        #Using colon syntax
        print(fruit[:5]) # Get from begining String upto index:  print -> Fresh 
        print(fruit[6:]) # Get from index to end of string:  print -> banana
        print(fruit[:]) # print -> Fresh banana

    def stringMethod(self, fruit:List[str]) -> List[str]:
        self.fruit = fruit
        # Show type and all methods of class string
        print(type(fruit))
        print(dir(fruit)) 
        
        # Print Upper Case
        UpperCase = fruit.upper()
        print(UpperCase)
        
        # find() find the position first occurrence of the substring
        pos = fruit.find("ba") 
        print("print position of b", pos) 
        print("If not found letter z return -1: ",fruit.find("z")) 
        
        # Search and replace
        replace = fruit.replace("banana", "apple")
        print("Replace banana -> apple: ", replace)
        
        #Stripping white space lstrip(), rstrip(), strip()
        stripString = fruit.strip()
        print("Stripping white space", stripString)

        # Check the prefix startswith("value")
        prefix = fruit.startswith("F")
        print('If start with F letter: ', prefix)
        prefix = fruit.startswith("f")
        print('If start with F letter: ', prefix)

        #Parsing and Extracting
        email = "triknigh@gmail.com Sat 8 Jun"
        atpos = email.find("@")
        print("the @ position: ", atpos)
        spacepos = email.find(' ', atpos)
        print('The space postion: ', spacepos)
        host = email[atpos+1: spacepos]
        print("Host value: ", host)


s = "Fresh banana  "
string = String()
string.loop(s)
string.slidingStr(s)
string.stringMethod(s)


