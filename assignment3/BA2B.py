def hammingDis(m, n):
    ham = 0
    for x, y in zip(m, n):
        if x != y:               # "!=" bedeuted "ungleich"
            ham += 1
    return ham

def distanceBetweenPatternAndDna(pattern, dna):
    k = len(pattern)
    distance = 0
    for x in dna:
        hamming = k+1
        for i in range(len(x) - k+1):
            z = hammingDis(pattern, x[i:i+k])
            if hamming > z:
                hamming = z
        distance += hamming
    return distance


def NumberToPattern(x,k):
    if k == 1:
        return NumberToSymbol(x)
    return NumberToPattern(x // 4, k - 1) + NumberToSymbol(x % 4)


def NumberToSymbol(x):
    if x == 0:
        return 'A'
    if x == 1:
        return 'C'
    if x == 2:
        return 'G'
    if x == 3:
        return 'T'


def medianString(dna, k):
    distance = (k+1) * len(dna)
    median = ""
    for i in range(4**k):
        pattern = NumberToPattern(i,k)
        z = distanceBetweenPatternAndDna(pattern,dna)
        if distance > z:
            distance = z
            median = pattern
    return median


#parameters:
dna = \
["TGATGATAACGTGACGGGACTCAGCGGCGATGAAGGATGAGT",
"CAGCGACAGACAATTTCAATAATATCCGCGGTAAGCGGCGTA",
"TGCAGAGGTTGGTAACGCCGGCGACTCGGAGAGCTTTTCGCT",
"TTTGTCATGAACTCAGATACCATAGAGCACCGGCGAGACTCA",
"ACTGGGACTTCACATTAGGTTGAACCGCGAGCCAGGTGGGTG",
"TTGCGGACGGGATACTCAATAACTAAGGTAGTTCAGCTGCGA",
"TGGGAGGACACACATTTTCTTACCTCTTCCCAGCGAGATGGC",
"GAAAAAACCTATAAAGTCCACTCTTTGCGGCGGCGAGCCATA",
"CCACGTCCGTTACTCCGTCGCCGTCAGCGATAATGGGATGAG",
"CCAAAGCTGCGAAATAACCATACTCTGCTCAGGAGCCCGATG"] #uebersichtlicher und offener fuer bearbeitungen
k = 6

print(medianString(dna,k))