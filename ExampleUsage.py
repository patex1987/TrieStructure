'''
Created on 28. 4. 2017

@author: patex1987
'''
import TrieStruct


def trie_usage():
    """
    This function demonstrates how to use the Trie structure
    1. It inserts multiple words into the Trie stored in a list
    2. It inserts single words into the Trie
    3. Finds all the words starting with the provided prefix and
        prints them out
    """
    words_to_insert = ["0902123456",
                       "0904126345",
                       "12345678",
                       "12356",
                       "26736"]
    trie = TrieStruct.Trie()
    # Step nr.1
    trie.insert_multiple_words(words_to_insert)
    # Step nr.2
    trie.insert("0903127")
    trie.insert("0903458")
    # Step nr.3
    for word_with_prefix in trie.get_words_with_prefix("090"):
        print word_with_prefix

if __name__ == '__main__':
    trie_usage()
