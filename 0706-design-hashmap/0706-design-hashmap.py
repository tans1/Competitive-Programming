class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        list1 = self.keys
        list2 = self.values
        
        if key not in list1:
            list1.append(key)
            list2.append(value)
        else:
            index = list1.index(key)
            list1[index] = key
            list2[index] = value

    def get(self, key: int) -> int:
        list1 = self.keys
        list2 = self.values
        
        if key not in list1:
            return -1
        else:
            index = list1.index(key)
            return list2[index]

    def remove(self, key: int) -> None:
        list1 = self.keys
        list2 = self.values
        
        if key in list1:
            index = list1.index(key)
            list1.pop(index)
            list2.pop(index)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)