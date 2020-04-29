import pandas as pd # pandas
from janome.tokenizer import Tokenizer # Janome

t = Tokenizer()
s = 'すもももももももものうち' # 形態素解析を行うテキスト
for token in t.tokenize(s):
    print(token) # 形態素を表示

print('Hello World!') # 「Hello World!」という文を出力。
print('鬼滅の刃は面白い') # 「鬼滅の刃は面白い」という文を出力。