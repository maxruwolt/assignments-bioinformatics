def PatternToNumber(pattern):
    allowed_chars = set('ACGT')
    if set(pattern).issubset(allowed_chars):    #check for invalid characters
        if len(pattern) == 0:
            return 0
        symbol = pattern[-1:]
        prefix = pattern[0:-1]
        return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)
    else: print('Invalid Characters. Please only use A C G T.')

def SymbolToNumber(symbol):
    if symbol == 'A':
        return 0
    if symbol == 'C':
        return 1
    if symbol == 'G':
        return 2
    if symbol == 'T':
        return 3

if PatternToNumber('AGT') is not None:
    print (PatternToNumber('AGT'))
else: print('')

#alternativ: print(PatternToNumber('AGTE'))
#verhindert Code muss zwar zweimal bei pattern veraendert werden
#aber die Ausgabe erfolgt ohne 'None'
#derzeit optisch ansprechender