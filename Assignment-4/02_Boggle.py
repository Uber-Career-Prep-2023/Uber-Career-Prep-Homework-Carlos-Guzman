"""Boggle is a word game in which players compete to find the most words on a square grid of random letters. Valid words must be at least three characters and formed from non-overlapping (i.e., a position on the board can only be used once in a word) adjacent (including diagonal) letters. Given a Boggle board and a dictionary of valid words, return all valid words on the board.
Example:
Dictionary:
Ace             Ape         Cape        Clap        Clay    Gape            Grape
Lace            Lap         Lay         Mace        Map     May             Pace            
Pay             Rap         Ray         Tap         Tape    Trace           Trap
Tray            Yap


BOARD =      [[A, D, E],
             [ R, C, P],
             [ L, A, Y]]
             
Ouput:

Ace     Race        Pace        Lace        Pay     Lay     Clay        Ray
Lap     Rap         Clap        Ape         Cape    Yap

"""

"""
THIS IS SOLVED WITH THE TECHNIQUE OF TRIE AS A PARAMETER
1) Create a trie to store all the words in the dictionary and a set to store the final valid words.
2) Create a copy of the board, but this time only with the values of false to verify that we have already passed through that value 
and not to take repeated values.
3) Iterate through each cell of the matrix and do a depth search for each value of the matrix. 
We pass an extra value in the DFS to build a word as we advance through the depth search.
4) Depth search for each possible cell of the matrix and check if the current letter of the matrix is in the current node of the trie.
5) If the current letter of the matrix is not in the current node of the trie, 
stop the search or if there are no more possible unvisited places in the matrix, stop the search.
6) If the current letter of the matrix exists in the current node of the trie, check if the current word being built is a valid word.
7) If it is a valid word, add the value of the current word to the set of valid words. 
Mark that place in the matrix as true indicating that we have already passed through there.
8) If the current word is not a valid word, concatenate the current letter to the value of the current word and continue 
searching in all available directions.
9) In the backtracking, set all the values of the copy of the matrix back to false.
10) Repeat from step 4, iterating from all possible starting points in the matrix until there are no more valid directions 
in the matrix or the current node does not contain the letter in the current position of the matrix.
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


def dfs(copy_board,board,crr_word,i,j,valid_words,curr_node):
    # Check if the indices are out of bounds or the character of the current board cell does not exist in the current trie node or the cell has already been visited, then return the set of valid words
    if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
        return valid_words
    if board[i][j] not in curr_node.childs or copy_board[i][j]:
        return valid_words
    
    # Add the character of the current cell to the current word
    crr_word += board[i][j]
    # Update the current node to its child that has the same character as the current cell
    curr_node = curr_node.childs[board[i][j]]

    if curr_node.validWord:
        valid_words.add(crr_word)

    # Mark the current cell as visited
    copy_board[i][j] = True

    # Continue the depth-first search in all eight directions
    dfs(copy_board, board, crr_word, i - 1, j, valid_words, curr_node)  # Up
    dfs(copy_board, board, crr_word, i + 1, j, valid_words, curr_node)  # Down
    dfs(copy_board, board, crr_word, i, j - 1, valid_words, curr_node)  # Left
    dfs(copy_board, board, crr_word, i, j + 1, valid_words, curr_node)  # Right
    dfs(copy_board, board, crr_word, i - 1, j - 1, valid_words, curr_node)  # Up-Left
    dfs(copy_board, board, crr_word, i - 1, j + 1, valid_words, curr_node)  # Up-Right
    dfs(copy_board, board, crr_word, i + 1, j - 1, valid_words, curr_node)  # Down-Left
    dfs(copy_board, board, crr_word, i + 1, j + 1, valid_words, curr_node)  # Down-Right


    # Backtrack: mark the current cell as unvisited
    copy_board[i][j] = False

    return valid_words



def Boggle(dictionary, board):
    # Initialize an object of Trie class
    trie = Trie()
    # Insert all words from the dictionary into the trie
    for word in dictionary:
        trie.insert(word)

    # Initialize a set to hold all valid words
    valid_words = set()
    # Initialize a copy of the board with all cells unvisited (marked as False)
    copy_board = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    #for i in range(len(board)):
    #    copy_board.append([False] * len(board[i]))

    # For each cell in the board, run a DFS to find all valid words starting from this cell
    for i in range(len(board)):
        for j in range(len(board[0])):
           valid_words = dfs(copy_board, board, "", i, j, valid_words, trie.root)

    # After all cells have been considered, return the set of valid words
    return valid_words

"""dictionary = ["ace", "race", "pace", "lace", "pay", "lay", "clay", "ray", "lap", "rap", "clap", "ape", "cape", "yap"]

# Test case 1
board = [
    ["a", "d", "e"],
    ["r", "c", "p"],
    ["l", "a", "y"]
]
print(Boggle(dictionary, board))  
# Expected output: {'lay', 'ace', 'lap', 'rap', 'clap', 'yap', 'pay', 'ray'}

# Test case 2
board = [
    ["a", "c", "e"],
    ["r", "a", "p"],
    ["l", "p", "y"]
]
print(Boggle(dictionary, board))  
# Expected output: {'ace', 'lap', 'clap', 'yap', 'pay'}

# Test case 3
board = [
    ["r", "a", "y"],
    ["p", "a", "p"],
    ["l", "a", "y"]
]
print(Boggle(dictionary, board))  
# Expected output: {'lay', 'lap', 'rap', 'yap', 'pay', 'ray'}


"""

