class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = defaultdict(list)

        for i in range(len(strs)):
            count = [0] * 26

            for c in strs[i]:
                count[ord(c) - ord('a')] += 1

            groups[tuple(count)].append(strs[i])

        return list(groups.values())
