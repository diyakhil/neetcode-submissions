class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        start = self.root

        for c in word:
            if c in start.children:
                start = start.children[c]
            else:
                new_node = TrieNode()
                start.children[c] = new_node
                start = start.children[c]
        start.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index >= len(word):
                return node.isWord
            elif word[index] == '.': #check every value in children and recurse on that value
                for child in node.children: #if . is the end, we don't make any recursive calls
                    #can't just check the first child and return true or false, have to check all of them
                    if dfs(node.children[child], index + 1): 
                        return True
                return False
            elif word[index] in node.children:
                return dfs(node.children[word[index]], index + 1)
            else:
                return False
            

        start = self.root

        #use a for loop with a range
        for i in range(len(word)):
            if word[i] == '.':
                #call the dfs here, need to just go ahead and check to see if the whole word is there
                return dfs(start, i)
            
            if word[i] not in start.children:
                return False
            start = start.children[word[i]]
        return start.isWord
