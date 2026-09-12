class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        w =0
        count = 0
        for i in range(len(chars)):
            count += 1

            if(i + 1 == len(chars) or chars[i] != chars[i + 1]):
                chars[w] = chars[i]
                w += 1
                if(count > 1):
                    for digit in str(count):
                        chars[w] = digit
                        w+=1

                count = 0

        return w                
             
        
            

        




        