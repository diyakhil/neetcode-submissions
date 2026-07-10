class TrieNode():
    def __init__(self): #if this is omitted then class vars are shared across test cases
        self.children = {} #need to use self. here 
        self.isWord = False #set this to True whenever we hit a word

class PrefixTree:

    def __init__(self):
        self.Trie = TrieNode()
        

    def insert(self, word: str) -> None:
        start = self.Trie

        for c in word:
            #need to just go through the trie if word is already there
            if c in start.children:
                #move onto the next char by doing children[c] for the Trie
                start = start.children[c]
            else:
                #create new TrieNode and attach it
                newNode = TrieNode()
                start.children[c] = newNode
                start = newNode

        start.isWord = True


    def search(self, word: str) -> bool:
        start = self.Trie
        
        for c in word:
            if c in start.children:
                start = start.children[c]
            else:
                return False
        
        return start.isWord
        

    def startsWith(self, prefix: str) -> bool:
        start = self.Trie
        
        for c in prefix:
            if c in start.children:
                start = start.children[c]
            else:
                return False
        return True
        
        