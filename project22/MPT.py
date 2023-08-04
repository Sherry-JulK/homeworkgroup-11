from hashlib import sha256
import time


class extension:
    def __init__(self):
        self.type = 'extension'
        self.key = None
        self.value = branch()
        self.prefix = None
        self.nodehash = None
        self.nodevalue = None


class leaf:
    def __init__(self):
        self.type = 'leaf'
        self.key = None
        self.value = None
        self.prefix = None
        self.nodehash = None
        self.nodevalue = None


class branch:
    def __init__(self):
        self.type = 'branch'
        self.children = {'0': None, '1': None, '2': None, '3': None, '4': None, '5': None,
                         'b': None, '6': None, '7': None, '8': None, '9': None, 'a': None,
                         'c': None, 'd': None, 'e': None, 'f': None, 'value': False}



class tree:
    def __init__(self, tree=None):
        if tree != None:
            self.root = tree
        else:
            self.root = self.make_extension()
            self.root.prefix = 'root'
            self.nodehash = None
            self.nodevalue = None

    def make_leaf(self, prefix, key, value):
        temp = leaf()
        temp.key = key
        temp.prefix = prefix
        temp.value = value
        temp.nodevalue = sha256(value.encode('utf-8')).hexdigest()
        temp.nodehash = sha256(str(temp).encode('utf-8')).hexdigest()
        return temp

    def make_extension(self):
        temp = extension()
        return temp

    def different(self, node, key):
        if len(key) < len(node.prefix):
            length = len(key)
        else:
            length = len(node.prefix)
        count = 0
        while count < length:
            if node.prefix[count] != key[count]:
                return count
            count += 1
        return count

    def add(self, node, key, value):
        if node.prefix == 'root':
            if self.root.value.children[key[0]] == None:
                self.root.value.children[key[0]] = self.make_leaf(key[1::], key[1::], value)
                node.value.children['value'] = False
                return
            else:
                self.root.value.children[key[0]] = self.add(self.root.value.children[key[0]], key[1::], value)
                return
        father = node
        index = self.different(father, key)
        prefix = key[:index:]
        if index < len(father.prefix):
            if father.type == 'extension':
                return self.qian_extension(father, prefix, key[index::], index, value)
            else:
                return self.hou_extension(father, prefix, key[index::], index, value)
        else:
            if father.value.children[key[index]] == None:
                father.value.children[key[index]] = self.make_leaf(key[index + 1::], key[index])
                father.value.children['value'] = False
                return father
            else:
                father = self.add(father.value.children[key[index]], key[index::], value)
                return father

    def qian_extension(self, node, prefix, key, index, value):
        temp = self.make_extension()
        temp.prefix = prefix
        temp.value.children[node.prefix[index]] = node
        temp.value.children[node.prefix[index]].prefix = node.prefix[index + 1::]
        temp.value.children[key[0]] = self.make_leaf(key[1::], key[0], value)
        return temp

    def hou_extension(self, node, prefix, key, index, value):
        temp = self.make_extension()
        temp.prefix = prefix
        temp.value.children[node.key[index]] = node
        temp.value.children[node.key[index]].key = node.key[index + 1::]
        temp.value.children[key[0]] = self.make_leaf(key[1::], key[0], value)
        return temp

    def print_tree(self, node):
        print('extension of prefix', node.prefix)
        for key in node.value.children:
            if key == 'value':
                break
            if node.value.children[key] == None:
                continue
            elif node.value.children[key].type == 'leaf':
                print('branch', key)
                print('leaf of key', node.value.children[key].key)
            elif node.value.children[key].type == 'extension':
                print('branch', key)
                self.print_tree('leaf of key', node.value.children[key])

    def update_tree(self, node):
        temp = ''
        if node.value.children['value'] == True:
            return node.node_value
        for key in node.value.children:
            if key == 'value':
                break
            if node.value.children[key] == None:
                continue
            if node.value.children[key].type == 'leaf':
                temp = temp + node.value.children[key].nodevalue
            elif node.value.children[key].type == 'extension':
                temp = temp + self.update_tree(node.value.children[key])
        node.value.children['value'] = True
        node.node_value = sha256(temp.encode()).hexdigest()
        node.node_hash = sha256(str(node).encode()).hexdigest()
        print('prefix:', node.prefix)
        print('node_value:', node.nodevalue)
        return node

    def add_update(self, key, value, node=None):
        if node == None:
            node = self.root
        self.add(node, key, value)
        return self.update_tree(self.root)


t = tree()
a = t.add_update('123', 'a')
t.print_tree(a)
