from typing import List
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
                

# Optimized solution [Time:  | Space: ]
def group_anagrams_brute(strs: List[str]) -> List[List[str]]:
    pass