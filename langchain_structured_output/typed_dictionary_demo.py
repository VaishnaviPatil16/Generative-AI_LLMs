from os import name
from typing import TypedDict

class Person(TypedDict):
    name = str
    age  = int

new_perosn: Person = {'name':'Vaishnavi','age':28}
print(new_perosn)