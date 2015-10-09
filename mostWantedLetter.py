from collections import defaultdict
def checkio(text):
    text = text.lower()
    freq = defaultdict(int)
    prevCount = -1
    letters = []

    for i in  text:
        if i.isalpha():
            freq[i] += 1
            if freq[i] > prevCount: prevCount = freq[i]

    for f in freq:
        if freq[f] == prevCount:
            letters.append(f)

    letters.sort()
    return letters[0]
