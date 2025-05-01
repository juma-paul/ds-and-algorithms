from typing import List
from collections import defaultdict

# Brute force solution [Time: O(n^2 * mlogm) | Space: O(n * m)]

def group_anagrams_brute(strs: List[str]) -> List[List[str]]:
    visited = [False] * len(strs)
    group_anagrams = []

    for i in range(len(strs)):
        if visited[i]:
            continue
        group = [strs[i]]
        visited[i] = True

        for j in range(i + 1, len(strs)):
            if not visited[j] and sorted(strs[i]) == sorted(strs[j]):
                group.append(strs[j])
                visited[j] = True
        group_anagrams.append(group)
    
    return group_anagrams
                

# Optimized solution [Time: O(n * m) | Space: O(n * m)]
def group_anagrams_optim(strs: List[str]) -> List[List[str]]:
    hash_map = {}

    for string in strs:
        char_freq = [0] * 26
        for char in string:
            char_freq[ord(char) - ord('a')] += 1
        
        key = tuple(char_freq)

        if key in hash_map:
            hash_map[key].append(string)
        else:
            hash_map[key] = [string]
    
    return list(hash_map.values())