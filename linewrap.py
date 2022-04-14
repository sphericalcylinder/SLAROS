import wordlist

def wrap(sentencelist: list, stringkeylist: str, result: str):
    if len(result) <= 135:
        sentencelist.append(wordlist.Sentence(stringkeylist, 600, True))
        sentencelist.append(wordlist.Sentence(result, 625, False))
    else:
        results = []
        sliceindex = 135
        y = 650
        for i in range(len(result)//135):
            results.append(result[:sliceindex])
            results.append(result[sliceindex:])
        y -= len(results) * 25
        sentencelist.append(wordlist.Sentence(stringkeylist, y, True))
        for b in results:
            y += 25
            sentencelist.append(wordlist.Sentence(b, y, False))
