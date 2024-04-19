def strStr(haystack: str, needle: str) -> int:
    # Check if needle is not in haystack
    if needle not in haystack:
        return -1
    # Return the index of the first occurrence of needle in haystack
    return haystack.index(needle)

print(strStr("sadbutsad", "sad"))