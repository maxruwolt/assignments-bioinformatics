def hammingDistance(m, n):
    ham = 0
    for x, y in zip(m, n):
        if x != y:
            ham += 1
    return ham


def distanceBetweenPatternAndString(pattern, dna):
    k = len(pattern)
    distance = 0
    for x in dna:
        hammingD = k+1
        for i in range(len(x) - k + 1):
            if hammingD > hammingDistance(pattern, x[i:i+k]):
                hammingD = hammingDistance(pattern, x[i:i+k])
        distance += hammingD
    return distance

dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]
pattern = "AAA"
print(distanceBetweenPatternAndString(pattern, dna))