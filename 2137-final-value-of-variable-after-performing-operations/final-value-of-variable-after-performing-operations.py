class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        p=0
        m=0
        for i in range(len(operations)):
            if operations[i]=="X++"or operations[i]=="++X":
                p=p+1
            elif operations[i]=="X--" or operations[i]=="--X":
                m=m+1
        return p-m