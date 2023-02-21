class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        
        if not self.head or index >= self.size:
            return -1
        
        if index == 0:
            return self.head.val
        
        cur = self.head
        
        while index:
            cur = cur.next
            index -= 1
        
        return cur.val
            
            
    def addAtHead(self, val: int) -> None:
        
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        
        if not self.head:
            self.head = newNode
        
        else:
            
            cur = self.head
            
            while cur.next:
                cur = cur.next
            
            cur.next = newNode
        
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        if index > self.size:
            return -1
        
        if not self.head or index == 0:
            self.addAtHead(val)
        
        elif self.size == index:
            self.addAtTail(val)
            
       
        
        else:
            
            cur = self.head
            
            while cur and index > 1:
                cur = cur.next
                index -= 1
                
            temp = cur.next
            cur.next = newNode
            newNode.next = temp
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        
        if not self.head or index >= self.size:
            return -1

        dummy = Node()
        dummy.next = self.head
        
        cur = dummy
        
        while index:
            cur = cur.next
            index -= 1
            ''
        cur.next = cur.next.next
        self.head = dummy.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)