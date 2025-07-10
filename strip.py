l = ["Parth", "Shubham", "Harry"]
def rem (l,word):
    n = []
    for item in l:
        if not(item.strip == word):
            n.append(item.strip(word))
    return n
print(rem(l,"am"))