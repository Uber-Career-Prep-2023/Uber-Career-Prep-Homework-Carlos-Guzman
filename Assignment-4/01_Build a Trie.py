"""Implement a trie class, including the insert, search, and delete methods. Your class should adhere to the following API, adjusted appropriately for your language of choice.  

struct TrieNode {
   vector<struct TrieNode *> children; // a (resizable or fixed size) array of size 26
   bool validWord; // boolean to indicate if this node marks the end of a word
};

class Trie {
  struct TrieNode* root;

  void insert(string word); // adds a word to the trie
  bool isValidWord(string word); // returns a boolean indicating whether word is in the trie
  void remove(string word); // removes word, from the trie & deletes unused nodes
}

"""

class TrieNode():
    def __init__(self):
        self.childs = {}  # Dictionary to hold child nodes
        self.validWord = False  # Flag to denote end of a word
    
class Trie():
    def __init__(self):
        self.root = TrieNode()  # Create a root node upon initializing Trie
    
    def insert(self,word) -> None:
        crr_node = self.root

        # Traverse each letter in the word
        for letter in word:
            # If the letter does not exist as a child of the current node, add it
            if letter not in crr_node.childs:
                crr_node.childs[letter] = TrieNode()
            # Move to the child node 
            crr_node = crr_node.childs[letter]
        # Mark the current node as a valid word after processing the entire word
        crr_node.validWord = True
    
    def is_Valid_Word(self,word):
        crr_node = self.root

        # Traverse each letter in the word
        for letter in word:
            # If the letter does not exist as a child, the word is invalid and return False
            if letter not in crr_node.childs:
                return False
            # Move to the child node
            crr_node = crr_node.childs[letter]
        
        # If the entire word has been processed, check the validity of the word
        return crr_node.validWord

    def remove_recursively(self,word,crr_node,index):
        # If the end of the word is reached
        if index == len(word):
            # If it's not a valid word, return False
            if not crr_node.validWord:
                return False
            # If the node has no children, invalidate word and return True
            if len(crr_node.childs) == 0:
                crr_node.validWord = False
                return True
            # If the node has childrens, invalidate word but return False to not remove any other node
            elif len(crr_node.childs) > 0:
                crr_node.validWord = False
                return False
                
        # If the letter does not exist as a child, return False
        letter = word[index]
        if not crr_node.childs[letter]:
            return False 
        

        # Recursively remove the next letter in the word
        if self.remove_recursively(word,crr_node.childs[letter],index + 1): 
            # If removal was successful and the current node is not the end of a word
            # And has only one child, remove the child node and return True
            if not crr_node.validWord and len(crr_node.childs) == 1:
                del crr_node.childs[letter]
                return True
            # Else return False to let know that we can't remove the node
            return False
        # If no nodes can be removed, return False
        return False
        
    def remove(self,word) -> None:
        # Starts recursive removal from the root
        self.remove_recursively(word,self.root,0)



trie = Trie()

# Inserting words
trie.insert("hello")
trie.insert("hello_world")
trie.insert("validWord")
trie.insert("uber")

# Testing the is_Valid_Word function
assert trie.is_Valid_Word("hello") == True, "Test 1 failed"
assert trie.is_Valid_Word("hello_world") == True, "Test 2 failed"
assert trie.is_Valid_Word("validWord") == True, "Test 3 failed"
assert trie.is_Valid_Word("uber") == True, "Test 4 failed"
assert trie.is_Valid_Word("hi") == False, "Test 5 failed"  # This word was not inserted into Trie
assert trie.is_Valid_Word("hel") == False, "Test 6 failed"  # Prefix of a word in Trie but not a complete word

# Testing deletion
trie.remove("hello")
assert trie.is_Valid_Word("hello") == False, "Test 7 failed"  # Word was removed
assert trie.is_Valid_Word("hello_world") == True, "Test 8 failed"  # "hello_world" should still be present

trie.remove("uber")
assert trie.is_Valid_Word("uber") == False, "Test 9 failed"  # Word was removed

trie.remove("hello_world")
assert trie.is_Valid_Word("hello_world") == False, "Test 10 failed"  # Word was removed

trie.remove("validWord")
assert trie.is_Valid_Word("validWord") == False, "Test 11 failed"  # Word was removed

# Checking that Trie is empty
assert trie.is_Valid_Word("hello") == False, "Test 12 failed"
assert trie.is_Valid_Word("hello_world") == False, "Test 13 failed"
assert trie.is_Valid_Word("validWord") == False, "Test 14 failed"
assert trie.is_Valid_Word("uber") == False, "Test 15 failed"

print("All test cases passed.")