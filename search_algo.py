import streamlit as st 
import random
from time import perf_counter
def linear_search(arr,k):
    start = perf_counter()
    flag = 0
    for i, j in enumerate(arr):
        if j == k:  #element found
            flag = 1 
            break
    end = perf_counter()
    if flag:
        return "Element Found",end-start
    else:
        return "Element not Found",end-start
   
def binary_search(arr,k):
    sample_array = sorted(arr)  #sorting the array to apply binary search
    start = perf_counter()  #to calculate run times
    l, r = 0, len(arr)-1
    flag = 0
    while l <= r:
        mid = (l + r) // 2
        if sample_array[mid] < k:
            l = mid + 1 
        elif sample_array[mid] == k:
            flag = 1 
            break
        else:
            r = mid - 1 
    end = perf_counter() 
    if flag:
        return "Element Found",end - start
    else:
        return "Element not Found",end - start

def searching_in_bst(arr,value):
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def insert_value(node, value):  #inserting the nodes into bst
        if node is None:
            return Node(value)
        if value == node.value:
            pass
        if value < node.value:
            node.left = insert_value(node.left, value)
        elif value > node.value:
            node.right = insert_value(node.right, value)

        return node

    def bst_search(root, value):    #search in bst
        if root is None or root.value == value:
            return root
        if root.value < value:
            return bst_search(root.right, value)
        else:
            return bst_search(root.left, value)
        
    root = None 
    for val in arr:
        root = insert_value(root, val)
    start = perf_counter()
    result = bst_search(root,value)	
    end = perf_counter()
    if result is None:
        return "Element not Found", end - start
    else:
        return "Element Found", end - start
    
def searching_in_rbt(arr,val):
    class RBT_Node:
        def __init__(self, data):
            self.data = data
            self.rbt_left = None
            self.rbt_right = None
            self.rbt_parent = None
            self.color = 'R'    #R - Red, B - Black


    class RedBlackTree:
        def __init__(self):
            self.value = RBT_Node(0)
            self.value.color = 'B'
            self.value.rbt_left = None
            self.value.rbt_right = None
            self.root = self.value

        def insert_data(self, data):    #inserting values into rbt
            node = RBT_Node(data)
            node.rbt_parent = None
            node.data = data
            node.rbt_left = self.value
            node.rbt_right = self.value
            node.color = 'R'    # new node always red

            rbt_parent = None
            current_node = self.root
            while current_node != self.value:
                rbt_parent = current_node
                if node.data < current_node.data:
                    current_node = current_node.rbt_left
                else:
                    current_node = current_node.rbt_right

            node.rbt_parent = rbt_parent
            if rbt_parent is None:
                self.root = node
            elif node.data < rbt_parent.data:
                rbt_parent.rbt_left = node
            else:
                rbt_parent.rbt_right = node

            if node.rbt_parent is None:
                node.color = 'B'
                return

            if node.rbt_parent.rbt_parent is None:
                return

            self.insertion_fix(node)

        def insertion_fix(self, k):     #fixing the tree after insertion
            while k.rbt_parent.color == 'R':
                if k.rbt_parent == k.rbt_parent.rbt_parent.rbt_right:
                    u = k.rbt_parent.rbt_parent.rbt_left
                    if u.color == 'R':
                        u.color = 'B'
                        k.rbt_parent.color = 'B'
                        k.rbt_parent.rbt_parent.color = 'R'
                        k = k.rbt_parent.rbt_parent
                    else:
                        if k == k.rbt_parent.rbt_left:
                            k = k.rbt_parent
                            self.right_rotate(k)
                        k.rbt_parent.color = 'B'
                        k.rbt_parent.rbt_parent.color = 'R'
                        self.left_rotate(k.rbt_parent.rbt_parent)
                else:
                    u = k.rbt_parent.rbt_parent.rbt_right

                    if u.color == 'R':
                        u.color = 'B'
                        k.rbt_parent.color = 'B'
                        k.rbt_parent.rbt_parent.color = 'R'
                        k = k.rbt_parent.rbt_parent
                    else:
                        if k == k.rbt_parent.rbt_right:
                            k = k.rbt_parent
                            self.left_rotate(k)
                        k.rbt_parent.color = 'B'
                        k.rbt_parent.rbt_parent.color = 'R'
                        self.right_rotate(k.rbt_parent.rbt_parent)
                if k == self.root:
                    break
            self.root.color = 'B'

        def right_rotate(self, x):  #right rotation
            y = x.rbt_left
            x.rbt_left = y.rbt_right
            if y.rbt_right != self.value:
                y.rbt_right.rbt_parent = x

            y.rbt_parent = x.rbt_parent
            if x.rbt_parent is None:
                self.root = y
            elif x == x.rbt_parent.rbt_right:
                x.rbt_parent.rbt_right = y
            else:
                x.rbt_parent.rbt_left = y
            y.rbt_right = x
            x.rbt_parent = y

        def left_rotate(self, x):   #left rotation
            y = x.rbt_right
            x.rbt_right = y.rbt_left
            if y.rbt_left != self.value:
                y.rbt_left.rbt_parent = x

            y.rbt_parent = x.rbt_parent
            if x.rbt_parent is None:
                self.root = y
            elif x == x.rbt_parent.rbt_left:
                x.rbt_parent.rbt_left = y
            else:
                x.rbt_parent.rbt_right = y
            y.rbt_left = x
            x.rbt_parent = y

        def rbt_search(self, node, data):   #searching in rbt
            if node == self.value or data == node.data:
                return node

            if data < node.data:
                return self.rbt_search(node.rbt_left, data)
            return self.rbt_search(node.rbt_right, data)

    
    tree = RedBlackTree()
    for val in arr:
        tree.insert_data(val)

    start = perf_counter()	
    result = tree.rbt_search(tree.root, search_key)
    end = perf_counter()
    if result != tree.value:
        return "Element Found",end - start
    else:
        return "Element not Found", end - start

#GUI Representation using streamlit

st.title("Runtimes Comparision:clock12: ")
st.header(':blue[Search Algorithms]', divider='rainbow')

arr_len = st.text_input("Enter the length of array",100)
arr = [random.randint(1, int(arr_len)*2) for _ in range(int(arr_len))]
search_key = random.randint(1,int(arr_len)*2)
l = [linear_search(arr,search_key),binary_search(arr,search_key),searching_in_bst(arr,search_key),searching_in_rbt(arr,search_key)]


select = st.multiselect(
    'Choose the algorithms you would like to compare',
    ['Linear Search', 'Binary Search', 'Binary Search Tree', 'Red-Black Tree'])


st.button("Compare")

d = {}

x_sample = ['LS','BS','BST','RBT']

x = [] # x-axis
y = [] # y-axis

flag_sample = 0

for i in select:
    if i=="Linear Search":
        j = 0
    elif i == "Binary Search":
        j = 1 
    elif i == "Binary Search Tree":
        j = 2 
    elif i == "Red-Black Tree":
        j = 3
    if l[j][0] == "Element Found":
        flag_sample = 1
    d[x_sample[j]] = l[j][1]


st.bar_chart(data=d, x=None, y=None, color=None, width=0, height=0, use_container_width=True)


if flag_sample:
    st.write("Element Found")
else:
    st.write("Element not Found")


if st.button("Stream data"):
    st.write("Search Element:",search_key)
    st.write("Array Generated: ")
    st.write(arr)