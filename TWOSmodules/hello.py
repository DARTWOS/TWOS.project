
from unicodedata import name


def input_name (name:str):
    question = input('What is your name ?\n ')
  
    name =(f' Hello {question}')
    print(name)
input_name(name)