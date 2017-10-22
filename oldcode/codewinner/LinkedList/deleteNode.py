#!/usr/bin/python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def deleteNode(self, delete_node):
        print delete_node.data
        print delete_node.next
        delete_node.data = delete_node.next.data
        delete_node.next = delete_node.next.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next

# Driver program
llist = LinkedList()

llist.push(5)

llist.push(10)

llist.push(7)

llist.push(3)

llist.push(1)
print "Create Linked List"
llist.printList()

delete_node = Node(3)
llist.deleteNode(delete_node)
print "After Delete Node"
llist.printList()