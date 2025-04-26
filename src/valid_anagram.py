# Brute Force solution [Time: O(nlogn) | Space: O(n)]

def valid_anagram_brute(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Optimized solution [Time: O(n) | Space: O(1)]

def valid_anagram_optim(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    
    count = {}

    for chr in s:
        count[chr] = count.get(chr, 0) + 1
    
    for chr in t:
        if chr not in count or count[chr] == 0:
            return False
        count[chr] -= 1

    return True