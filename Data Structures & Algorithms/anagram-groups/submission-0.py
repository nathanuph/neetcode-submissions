class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) # mapping character count to list of anagrams

        for s in strs:
            sortedS = ''.join(sorted(s))
            result[sortedS].append(s)

        return list(result.values())