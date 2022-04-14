import wordlist

def wrap(sentencelist: list, stringkeylist: str, result: str, colors: tuple):
    if len(result) <= 135:
        sentencelist.append(wordlist.Sentence(stringkeylist, 600, True, colors))
        sentencelist.append(wordlist.Sentence(result, 625, False, colors))
    else:
        results = []
        sliceindex = 135
        y = 650
        for i in range(len(result)//135):
            results.append(result[:sliceindex])
            results.append(result[sliceindex:])
        y -= len(results) * 25
        sentencelist.append(wordlist.Sentence(stringkeylist, y, True, colors))
        for b in results:
            y += 25
            sentencelist.append(wordlist.Sentence(b, y, False, colors))
