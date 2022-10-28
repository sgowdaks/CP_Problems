class Trie_node:
    def __init__(self):
        self.childern = {}
        self.last = False


class Trie:

    def __init__(self):
        self.root = Trie_node()        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for letter in word:
            if letter not in curr.childern:
                curr.childern[letter] = Trie_node()
            curr = curr.childern[letter]                
        curr.last = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for letter in word:
            if letter not in curr.childern:
                return False
            curr = curr.childern[letter]

        return curr.last
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for letter in prefix:
            if letter not in curr.childern:
                return False
            curr = curr.childern[letter]

        return True
