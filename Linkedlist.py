class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
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
        
    def insert_values(self,data_list):
        for data in data_list:
            self.insert_at_ending(data)
            
    
    
    def insert_at_index(self,index,data):
        if index<0:
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_beginning(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=Node(data,itr.next)
                
                break
            itr=itr.next
            count+=1
            
    def insert_after_value(self,data_after,insert_data):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next=Node(insert_data,self.head.next)
            return
        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(insert_data,itr.next)
                break
            itr=itr.next
    def remove_at_index(self, index):
        if index<0:
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1
        
    def remove_by_value(self,data_remove):
        if self.head is None:
            return
        if self.head.data==data_remove:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next: 
            if itr.next.data==data_remove:
                itr.next=itr.next.next
            itr=itr.next
    def get_length(self):
        count=1
        itr=self.head
        while itr.next:
            itr=itr.next
            count+=1
        print("lenght of the linked list:",count)
        return
    
    def print(self):
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
    def reverse(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
        itr=self.head
        llstr=''
        while itr:
            llstr=llstr+str(itr.data)+'-->'
            itr=itr.next
        print(llstr)
        return
    
    
if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_ending(3)
    ll.insert_at_beginning(34)
    ll.insert_at_ending(65)
    ll.insert_at_ending(3)
    ll.insert_at_beginning(34)
    ll.insert_values(['dega','nanda'])
    ll.get_length()
    ll.remove_at_index(5)
    ll.insert_at_index(5,"dega")
    ll.insert_after_value("dega","reddy")
    ll.insert_after_value("reddy","rajula")
    ll.remove_by_value("reddy")
    ll.print()
    ll.reverse()
    ll.get_length()
