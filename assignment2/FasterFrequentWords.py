def FasterFrequentWords(sequence,k):
    frequentPatterns = []
    fArray = FrequencyArray(sequence,k)
    maxCount = max(fArray)
    for i in range(4**k):
        if fArray[i] == maxCount:
            pattern = NumberToPattern(i,k)
            frequentPatterns.append(pattern)
    return frequentPatterns


def FrequencyArray(sequence, k):
    fArray = [0] * 4**k
    for i in range(len(sequence) - k + 1):
        pattern = sequence[i:i+k]
        num = PatternToNumber(pattern)
        fArray[num] = fArray[num]+1
    return fArray


def PatternToNumber(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[-1:]
    prefix = pattern[0:-1]
    return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)


def SymbolToNumber(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3


def NumberToPattern(index,k):
    if k == 1:
        return NumberToSymbol(index)
    return NumberToPattern(index // 4, k - 1) + NumberToSymbol(index % 4)


def NumberToSymbol(index):
    if index == 0:
        return 'A'
    if index == 1:
        return 'C'
    if index == 2:
        return 'G'
    if index == 3:
        return 'T'


print(FasterFrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT",4))


