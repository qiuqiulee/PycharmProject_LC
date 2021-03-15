def getKseq(seq,A):
    def checkfreq(seq,word):
        if len(word)> len(seq):
            return 0
        i = 0
        lofStr = len(word)
        maxrepeat = 0
        currmatch   = 0
        while i+lofStr < len(seq)+1:
            if seq[i:i+lofStr] == word:
                currmatch +=1
                i=i+lofStr
                maxrepeat = max(maxrepeat,currmatch)
            else:
                i+=1
                currmatch = 0

        return maxrepeat
    res= []
    for word in A:
        res.append(checkfreq(seq,word))
    return res




sequence = 'cababcabc'
A = ['ab', 'a', 'abc', 'ba']
print(getKseq(sequence,A))



