import pandas as pd
from janome.tokenizer import Tokenizer

t = Tokenizer()

s = 'すもももももももものうち'
for token in t.tokenize(s):
    print(token)

print('Hello World!')
print('鬼滅の刃は面白い')