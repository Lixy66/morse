morse = {"a": ".-",
         "b": "-...",
         "c": "-.-.",
         "d": "-..",
         "e": ".",
         "f": "..-.",
         "g": "--.",
         "h": "....",
         "i": "..",
         "j": ".---",
         "k": "-.-",
         "l": ".-..",
         "m": "--",
         "n": "-.",
         "o": "---",
         "p": ".--.",
         "q": "--.-",
         "r": ".-.",
         "s": "...",
         "t": "-",
         "u": "..-",
         "v": "...-",
         "w": ".--",
         "x": "-..-",
         "y": "-.--",
         "z": "--.."}


def encode_to_morse(text):
    for i in input().lower().split():
        print(*[morse[j] for j in i])


