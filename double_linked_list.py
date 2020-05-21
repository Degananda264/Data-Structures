# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:52:37 2020

@author: degananda.reddy
"""

class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
class DoubleLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_ending(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
        
    def get_length(self):
        count=1
        itr=self.head
        while itr.next:
            itr=itr.next
            count+=1
        print("lenght of the linked list:",count)
        return
    
    def print_forward(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        itr=self.head
        llstr=''
        while itr:
            llstr=llstr+str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
        return
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        
        print("Link list in reverse: ", llstr)  
        return
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
if __name__=='__main__':
    dll=DoubleLinkedList()
    dll.insert_at_beginning("dega")
    dll.insert_at_beginning("rajula")
    dll.insert_at_ending("nanda")
    dll.insert_at_ending("reddy")
    dll.get_last_node()
    dll.get_length()
    dll.print_forward()
    dll.print_backward()
    