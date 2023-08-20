class LockingTree:

    def __init__(self, parent: List[int]):
        self.par = defaultdict(list)
        self.child = defaultdict(list)
        self.locked = {}
        self.locked[0] = -1
        for i in range(1,len(parent)):
            self.child[parent[i]].append(i)
            self.par[i].append(parent[i])
            self.locked[i] = -1
        
    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == -1:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != -1 and self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def unlockDescent(node):
            if self.locked[node] != -1:
                self.locked[node] = -1
            for nb in self.child[node]:
                unlockDescent(nb)
            
        def findLocked(dct, node):
            if self.locked[node] != -1:
                return True
            
            for nb in dct[node]:
                if findLocked(dct, nb):
                    return True
            return False
        if self.locked[num] != -1 or findLocked(self.child, num) == False or findLocked(self.par, num) == True:
            return False
        unlockDescent(num)
        self.locked[num] = user
        return True
        



# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)