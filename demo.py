class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def apppend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        new_node.prev=last
    def display(self):
        print("Forward transversal:")
        temp=self.head
        last=None
        while temp:
            print(temp.data,end=" ")
            last=temp
            temp=temp.next
        print("\nBackward transversal:")
        while last:
            print(last.data,end=" ")
            last=last.prev
        print()
if __name__=="__main__":
    dll= DoublyLinkedList()
    dll.apppend(10)
    dll.apppend(20)
    dll.apppend(30)
    dll.display()