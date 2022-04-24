import wordlist

def wrap(sentencelist: list, stringkeylist: str, input: str, colors: tuple):
    if len(input) <= 135:
        sentencelist.append(wordlist.Sentence(stringkeylist, 600, True, colors))
        sentencelist.append(wordlist.Sentence(input, 625, False, colors))
    else:
        inputs = []
        sliceindex = 135
        y = 650
        for i in range(len(input)//135):
            inputs.append(input[:sliceindex])
            inputs.append(input[sliceindex:])
        y -= len(inputs) * 25
        sentencelist.append(wordlist.Sentence(stringkeylist, y, True, colors))
        for b in inputs:
            y += 25
            sentencelist.append(wordlist.Sentence(b, y, False, colors))
