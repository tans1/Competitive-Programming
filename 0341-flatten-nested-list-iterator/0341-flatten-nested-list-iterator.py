# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        temp = []
        stack = nestedList
        while stack:
            top = stack.pop()
            if top._integer != None:
                temp.append(top._integer)
                continue
            
            for child in top._list:
                stack.append(child)
        self.root = temp[::-1]
        self.index = 0
        
    def next(self) -> int:
        self.index += 1
        return self.root[self.index - 1]
    def hasNext(self) -> bool:
        return self.index < len(self.root)
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())