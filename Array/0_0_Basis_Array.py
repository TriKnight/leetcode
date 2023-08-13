from typing import List
"""
Basic Array Techniques
"""
class Array:
    def slidingWindow(self, string:List[str]) -> List[str]:
        self.string = string
        print(string)
        

s = "abcabcbb"
array = Array()
print(array.slidingWindow(s))