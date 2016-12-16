f = open("enable1.txt", "r")

def longest(s):
    long_string = "i"
    charlen = s.count('?')
    for word in iter(f):
        wlen = len(word.rstrip())
        w = list(word.rstrip())

        for letter in s:
            if letter != '?':
                position = w.index(letter) if letter in w else -1
                if position != -1:
                    del(w[position])
                    wlen -= 1

            else:
                wlen -= 1


            if wlen <= 0:
                if len(word) > len(long_string):
                    long_string = word

    return long_string

s = input("enter the string:")
print(longest(s))
