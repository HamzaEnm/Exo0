import nltk
nltk.download('punkt_tab')
a = "Ma vieille tante est en Espagne."
b=nltk.tokenize.word_tokenize(a)
print(b)