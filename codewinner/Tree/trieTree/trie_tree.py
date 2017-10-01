# -*- coding: utf -*-

class Trie_tree(object):

    def __init__(self):
        # node = [father, child, keep_char, is_word]
        self._root = [None, [], None, False]
        self.tmp = []
        self.allWord = []

    def insert(self, word):
        current_word = word
        current_node = self._root
        self._insert_operation_1(current_word, current_node)

    def _insert_operation_1(self, current_word, current_node):
        if current_word:
            first_char = current_word[0]
            child_node = current_node[1]
            is_in_child_node = False

            for node in child_node:
                if first_char == node[2]:
                    is_in_child_node = True
                    current_word = current_word[1:]
                    current_node = node
                    self._insert_operation_1(current_word, current_node)
                    break

            if not is_in_child_node:
                self._insert_operation_2(current_word, current_node)

        else:
            current_node[3] = True

    def _insert_operation_2(self, current_word, current_node):
        first_char = current_word[0]

        # create a new node and insert it in the tree
        new_node = [None, [], None, False]
        new_node[2] = first_char
        new_node[0] = current_node
        current_node[1].append(new_node) # 添加进child

        current_word = current_word[1:]
        if current_word:
            current_node = new_node
            self._insert_operation_2(current_word, current_node)

        else:
            new_node[3] = True

    def find(self, word):
        current_word = word
        current_node = self._root
        return self._find_operation(current_word, current_node)

    def _find_operation(self, current_word, current_node):
        if current_word:
            first_char = current_word[0]
            child_node = current_node[1]

            if not child_node:
                return False

            is_in_child_node = False
            for node in child_node:
                if first_char == node[2]:
                    is_in_child_node =True
                    current_word = current_word[1:]
                    current_node = node
                    return self._find_operation(current_word, current_node)

            if not is_in_child_node:
                return False

        else:
            return current_node[3]

    def delete(self, word):
        current_word = word
        current_node = self._root
        return self._delete_operation(current_word, current_node)

    def _delete_operation(self, current_word, current_node):
        if current_word:
            first_char = current_word[0]

            child_node = current_node[1]
            if not child_node:
                return False

            is_in_child_node = False
            for node in child_node:
                if first_char == node[2]:
                    is_in_child_node = True
                    current_word = current_word[1:]
                    current_node = node
                    return self._delete_operation(current_word, current_node)

            if not is_in_child_node:
                return False

        else:
            if current_node[1]:
                current_node[3] = False
            # current_node is leaf_node
            else:
                father_node = current_node[0]
                father_node[1].remove(current_node)

            return True

    def print_tree(self, current_node):
        if current_node:
            self._dfs_print(current_node)

    def _dfs_print(self, current_node):
        if current_node[2]:
            self.tmp.append(current_node[2])
        # if it is a word
        if current_node[3]:
            print ("".join(self.tmp))
        for child in current_node[1]:
            self._dfs_print(child)
        if self.tmp:
            self.tmp.pop()

if __name__ == '__main__':
    demo_trie = Trie_tree()
    print ("--------Insert:---------")
    for word in ["apps", "apple", "cook", "cookie", "cold"]:
        print (word)
        demo_trie.insert(word)

    print ("--------Print Test:---------")
    demo_trie.print_tree(demo_trie._root)

    print ("--------Find Test:--------")
    print ("ap:     ", demo_trie.find("ap"))
    print ("apps:   ", demo_trie.find("apps"))
    print ("apple:  ", demo_trie.find("apple"))
    print ("apples: ", demo_trie.find("apples"))
    print ("coo:    ", demo_trie.find("coo"))
    print ("cook:   ", demo_trie.find("cook"))
    print ("cookie: ", demo_trie.find("cookie"))
    print ("cold:   ", demo_trie.find("cold"))

    print ("--------Delete Test:--------")
    demo_trie.delete("cookie")
    print ("> Delete cookie")
    print ("Find cook   ?", demo_trie.find("cook"))
    print ("Find cookie ?", demo_trie.find("cookie"))
    demo_trie.delete("apple")
    print ("> Delete apple")
    print ("Find apps   ?", demo_trie.find("apps"))
    print ("Find apple  ?", demo_trie.find("apple"))

    print ("--------Print Test:---------")
    demo_trie.print_tree(demo_trie._root)
