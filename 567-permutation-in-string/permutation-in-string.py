class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        n1 = len(s1)

        for s in s1:
            freq[s] = freq.get(s, 0) + 1

        for i in range(len(s2)):
            freq[s2[i]] = freq.get(s2[i], 0) - 1

            if(i >= n1):
                freq[s2[i - n1]] += 1


            if(i+1 >= n1 and all(val <= 0 for val in freq.values())):
                return True

        return False                    
