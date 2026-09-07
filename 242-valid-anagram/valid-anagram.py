class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)): return False

        freq = {}

        
        for i in range(len(t)):
            
            freq[s[i]] = freq.get(s[i], 0) + 1
            print(freq[s[i]])
            freq[t[i]] = freq.get(t[i], 0) - 1
            print(freq[t[i]])

            if(t[i] in freq and freq.get(t[i], 0) == 0):
                del freq[t[i]]

            if(s[i] in freq and freq.get(s[i], 0) == 0):
                del freq[s[i]]                

        if(len(freq) > 0): return False
        return True                    

