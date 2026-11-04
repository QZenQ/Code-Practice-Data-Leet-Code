class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if(len(s) != len(t)): return False
        count = {}
      
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1

            if(count[s[i]] == 0):del count[s[i]]
            if(t[i] in count and count[t[i]] == 0):del count[t[i]]
            

        
        print(len(count))
        if len(count) == 0: return True
        return False