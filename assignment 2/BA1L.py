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

#noch keine spezifische Reaktion auf unzulaessige Zeichen
    #else print('Invalid character. Please change to A C G T.')

print(PatternToNumber('AGT'))