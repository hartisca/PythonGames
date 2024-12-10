from collections import defaultdict
import re

stop_words = {"de", "en", "y", "la", "el", "los", "las", "un", "una", "que", "a"}

text = input("Añade tu texto a continuación: ")

words = defaultdict(int)

for w in text.lower().split():
    # Eliminar signos de puntuación
    w = re.sub(r'[^\wáéíóúüñ]', '', w)
    if w not in stop_words:
        words[w] += 1

print(dict(words))

