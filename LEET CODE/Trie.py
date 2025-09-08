class TrieNode():
    def __init__(self,character,is_end):
        self.character=character
        self.is_end=is_end
        self.hashmap={}
        
class Trie(object):
    def __init__(self):
        pass
        self.first_char_map={}
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if len(word)==1:
            # self.first_char_map[word[0]][1]=True
            if word[0] in self.first_char_map:
                lastNode=self.first_char_map[word]
                self.first_char_map.is_end=True
            else:
                lastNode=TrieNode(word[0],True)
                self.first_char_map[word[0]]=(lastNode)
                self.first_char_map[word[0]].is_end=True
        else:
            if word[0] in self.first_char_map:
                lastNode=self.first_char_map[word[0]]
            else:
                lastNode=TrieNode(word[0],False)
                self.first_char_map[word[0]]=(lastNode)
                self.first_char_map[word[0]].is_end=(False)
            for index,letter in enumerate(word[1:]):
                if letter in lastNode.hashmap:
                    if index+2 == len(word):
                    # if lastNode.hashmap[letter][1] == False and index+2 == len(word):
                        lastNode.hashmap[letter].is_end=True
                    lastNode=lastNode.hashmap[letter]

                else:
                    lastNode.hashmap[letter]=TrieNode(letter,index+2==len(word))
                    lastNode=lastNode.hashmap[letter]
        return None
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)==1:
            if word in self.first_char_map and self.first_char_map[word].is_end:
                return True
            else:
                return False
        else:
            # if word[0] in self.first_char_map and self.first_char_map[word[0]][1] == False:
            if word[0] in self.first_char_map:
                last_node=self.first_char_map[word[0]]
                for index,letter in enumerate(word[1:]):
                    if letter in last_node.hashmap:
                        if (index+2 == len(word)) and last_node.hashmap[letter].is_end:
                            return True
                        last_node=last_node.hashmap[letter]
                    else:
                        return False
            return False
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if len(prefix)==1 and prefix in self.first_char_map:
            return True
        else:
            if prefix[0] in self.first_char_map:
                last_node=self.first_char_map[prefix[0]]
                for index,letter in enumerate(prefix[1:]):
                    if letter in last_node.hashmap:
                        last_node=last_node.hashmap[letter]
                    else:
                        return False
                return True
            else:
                return False        

if __name__ == "__main__":
    trie = Trie()
trie.insert("app")
trie.insert("apple")

print(trie.search("apple"))  # ✅ True
print(trie.search("app"))   # True
