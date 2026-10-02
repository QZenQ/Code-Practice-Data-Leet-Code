class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        arr = []
        self.ls = []
        self.ls.append(arr)
        self.validRM = 0
        self.validLM = 0
        self.il = []

    def push(self, val: int) -> None:

        self.il = [x for x in self.il if x <= self.validRM]
         
        if self.il:
            i = self.il[0]
            self.ls[i].append(val)
            if len(self.ls[i]) == self.capacity:
                self.il.pop(0)
            return
        if(len(self.ls[self.validRM]) == self.capacity):

            self.validRM += 1
            if self.validRM == len(self.ls):
                self.ls.append([])
            

         

        # print("pushh",index)
        # print("len",len(self.ls))

        self.ls[self.validRM].append(val)

    def pop(self) -> int:
        print(self.validRM)
        while(self.isEmpty(self.validRM)):
            self.validRM -= 1
            if(self.validRM < 0):
                self.validRM = 0
                return -1
        
        return self.ls[self.validRM].pop()

    def popAtStack(self, index: int) -> int:
        if(self.isEmpty(index)):
            return -1
        elif(index not in self.il):
            self.il.append(index)
            self.il.sort()
            #print("pop {}"self.il)
        
        return self.ls[index].pop()

    def isEmpty(self, index):
        if(len(self.ls) - 1 < index): return True
        return len(self.ls[index]) == 0

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)