class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None
class Slinkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.nextval = self.headval
        self.headval = new_node
    def append(self, new_data):
        new_node = Node(new_data)
        if self.headval is None:
            self.headval = new_node
            return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = new_node
    def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return

      NewNode = Node(newdata)
      NewNode.nextval = middle_node.nextval
      middle_node.nextval = NewNode
    def deleteNode(self, key):
        temp = self.headval
        if (temp is not None):
            if (temp.dataval == key):
                self.headval = temp.nextval
                temp = None
                return
