def safe_pawns(pawns):
    letters = dict()

    safe = set()

    for p in pawns:
        letters[p] = [int(ord(p[0])),int(p[1])]

    for l in letters:
        for k in letters:
            if l != k:
                if (letters[k][1] == letters[l][1] - 1 ) and ( letters[k][0] == letters[l][0] + 1 or letters[k][0] == letters[l][0] - 1 ):
                    safe.add(l)
                    print l,letters[l], k,letters[k], safe

    return len(safe)
