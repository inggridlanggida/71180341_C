class Node:
    def __init__(self, data, parent):
        self._data = data
        self._children = []
        self._parent = parent
 
    #menambahkan child
    def addChild(self, data):
        self._children.append(data)
 
    #mendapatkan isi elemen
    def operator(self):
        return self._data
 
    #mendapatkan node parent
    def parent(self):
        return self._parent
 
    #mendapatkan node children
    def children(self):
        return self._children
 
    #mengecek apakah node merupakan root
    def isRoot(self):
        return self._parent is None
 
    #mengecek apakah node merupakan external/leaf
    def isExternal(self):
        return len(self._children) == 0
 
def preorder(node):
    print(node.operator(), end = ' ')
    for i in node.children():
        preorder(i)
 
def postorder(node):
    for i in node.children():
        postorder(i)
    print(node.operator(), end = ' ')
 
def depth(node):
    if node.isRoot():
        return 0
    else:
        return 1+depth(node.parent())
 
def height(node):
    if node.isExternal():
        return 0
    else:
        h = 0
        for i in node.children():
            h = max(h, height(i))
        return 1+h
 
 
# child daftar ke parent
val300 = Node(300, None)
a = Node(9, val300)
b = Node(1, val300)
c = Node(11, a)
d = Node(99, a)
e = Node(17, b)
f = Node(28, c)
g = Node(72, c)
h = Node(90, d)
i = Node(33, d)
j = Node(2, e)
k = Node(4, e)
l = Node(43, e)
 
# parent daftarin childnya
a.addChild(c)
a.addChild(d)
b.addChild(e)
c.addChild(f)
c.addChild(g)
d.addChild(h)
d.addChild(i)
e.addChild(j)
e.addChild(k)
e.addChild(l)
val300.addChild(a)
val300.addChild(b)
 
#cetak data pada node val300
print(val300.operator())
 
#cetak data dari parent node e
print(e.parent().operator())
 
#cetak data children dari node val300
for i in val300.children():
    print(i.operator(), end = ' ')