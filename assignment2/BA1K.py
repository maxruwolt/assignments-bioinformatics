def FrequencyArray(sequence, k):
    fArray = [0] * 4**k                         # 4**k --> 4^k
    for i in range(len(sequence) - k + 1):
        pattern = sequence[i:i+k]
        num = PatternToNumber(pattern)
        fArray[num] = fArray[num]+1
    print(fArray)

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

FrequencyArray('ACGCGGCTCTGAAA',2)

#alternativ: nicht definiert
#sequence = 'ACGCGGCTCTGAAA'
#k = 2
#fArray = [0] * 4**k

#for i in range(len(sequence) - k + 1):
#    pattern = sequence[i:i+k]
#    num = PatternToNumber(pattern)
#    fArray[num] = fArray[num] + 1

#print(fArray)