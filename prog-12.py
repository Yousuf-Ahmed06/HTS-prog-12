import pyperclip
line = input("input: ")
prime = [2, 3, 5, 7]
pr_sm, cm_sm = 0, 0
text = ""
for letter in line:
    if letter.isdecimal():
        letter = int(letter)
        if letter in prime:
            pr_sm += letter
        elif letter > 1:
            cm_sm += letter
    elif len(text) < 25:
        ind = ord(letter) + 1
        if ind >= 127: ind -= 94
        text += chr(ind)
text = text.strip() + str(pr_sm * cm_sm)
print(text)
pyperclip.copy(text)

# asci = "!\"#$%&'()*+,-./:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
# text += asci[(asci.index(letter) + 1) % len(asci)]
