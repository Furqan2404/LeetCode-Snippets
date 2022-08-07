##python code to reverse list  using recursion
from typing import List

def reverse(s:List[str])->None:
    if len(s)==0:
        return []
    else :
        return [s[-1]] + reverse(s[:-1])

s=['w','E','R','4','5']
print(reverse(s))