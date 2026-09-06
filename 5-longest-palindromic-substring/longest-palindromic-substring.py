class Solution:
    def longestPalindrome(self, s: str) -> str:

        t = s

        
        s = "#" + "#".join(s) + "#"

        radii = [0] * len(s)
        r = 0
        c = 0

        maxRadius = 0
        maxCenter = 0

        for i in range(len(s)):

            center = i

            if center < r:
                mirror = 2*c - center
                radii[center] = min(r - center, radii[mirror])

            while (radii[center] + center + 1 < len(s)) and ( center - radii[center] -  1 >= 0) and (s[radii[center] + center + 1] == s[ center - radii[center] - 1]):
                radii[center] += 1

            if center + radii[center] > r:
                r = center + radii[center]
                c = center

            if radii[center] > maxRadius:
                maxRadius = radii[center]
                maxCenter = center

            print(c)
            print(r)
        out = s[maxCenter-maxRadius : maxCenter+maxRadius+1] 
        out = out.replace("#","")

        return out

        