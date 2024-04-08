from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    # Check if the lengths of both words are equal
    if len(word1) != len(word2):
        return False
    
    # Count the frequency of each character in both words
    fr1 = Counter(word1)
    fr2 = Counter(word2)

    # Sort the frequencies of characters in ascending order
    sv1 = sorted(fr1.values())
    sv2 = sorted(fr2.values())

    # Check if the sets of keys (characters) in both words are equal
    check = set(fr1.keys()) == set(fr2.keys())

    # Return True if the sorted frequencies of characters and sets of keys are equal, else False
    return sv1 == sv2 and check

print(closeStrings("cabbba", "abbccc"))