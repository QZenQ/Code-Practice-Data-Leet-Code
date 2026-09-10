class Solution:
    def compress(self, chars: List[str]) -> int:

        data = [] * 2000
        buffer = None
        cii = -1
        cc = 1 
        for i in range(len(chars)):
            print(cc)
            if(chars[i] != buffer or i == len(chars) - 1):

                if(i == len(chars) - 1 and chars[i] == buffer):
                    cc +=1

                if cii != -1 and cc > 1:
                    stack = []
                    while(cc>0):                                         
                        stack.append(str(cc % 10))
                        cc = cc//10
                    while(stack):
                        cii +=1
                        data.insert(cii, stack.pop())
                     
                    
                if(i == len(chars) - 1 and chars[i] == buffer): break 
                cii += 1
                buffer = chars[i]
                data.insert(cii, chars[i])
                cc = 1
                    
            else:
                cc += 1
                 
                     

        chars[:] = data      
        # for i in range(len(data)):
        #     print(data[i])

        return len(data)            


                
