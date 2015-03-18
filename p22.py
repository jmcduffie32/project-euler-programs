myList = sorted(open('p022_names.txt').read().replace('"','').split(","))

def word_score(word):
    score = 0
    for c in word:
        score += ord(c) - 64
    return score

scores = 0
for n, word in enumerate(myList):
    score = (n + 1) * word_score(word)
    scores += score

print scores
