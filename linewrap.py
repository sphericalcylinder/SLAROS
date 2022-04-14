import wordlist

def wrap(sentencelist: list, stringkeylist: str, result: str):
    if len(result) <= 135:
        sentencelist.append(wordlist.Sentence(stringkeylist, 600, True))
        sentencelist.append(wordlist.Sentence(result, 625, False))
    else:
        results = []
        sliceindex = 135
        yval = 600
        for i in range(len(result)//135):
            results.append(result[:sliceindex])
            results.append(result[sliceindex:])
        sentencelist.append(wordlist.Sentence(stringkeylist, yval, True))
        yval -= 25
        for b in reversed(results):
            sentencelist.append(wordlist.Sentence(b, yval, False))
            yval -= 25
