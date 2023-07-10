class Solution:

    def __init__(self) -> None:
        self.list_par=[]
        self.dict_para={'(' : ')','{' : '}','[' : ']',} 
        self.open=['(','{','[']
        self.closed=[')','}',']']
    def valid_parathesis(self,parathesis_string):
            
        for i in parathesis_string:
            if i in self.open:
                self.list_par.append(i)
            elif i in self.closed and  len(self.list_par)!=0 :
                if self.dict_para[self.list_par[-1]]==i :
                    self.list_par.pop()

        if len(self.list_par) != 0:
            print(self.list_par)
            return False
        else:
            return True

Solution1=Solution()
s1="({{}[){}]}"
print(Solution1.valid_parathesis(s1))