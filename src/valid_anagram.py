# Brute Force solution [Time: O(nlogn) | Space: O(n)]

def valid_anagram_brute(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Optimized solution [Time: O(n) | Space: O(n)]

def valid_anagram_optim(s: str, t: str) -> bool:
    if len(t) != len(s):
        return False
    
    count_s, count_t = {}, {}

    for i in range(len(t)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    
    return count_s == count_t