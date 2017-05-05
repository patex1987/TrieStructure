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
    trie.insert_multiple_words(["0903127"])
    trie.insert_multiple_words(["0903458"])
    # Step nr.3
    for word_with_prefix in trie.get_all_words_with_prefix("1234"):
        print word_with_prefix


def trie_unique_nodes_count():
    """
    This function returns the count of unique nodes in the Trie

    Example:
        if we insert the following word in the Trie: "1234",
        there will be 4 unique nodes in the Trie,
        namely: "1", "2", "3", "4"
        if we add two more words: "1235", "12345" (there will be 3
        elemnts in the Trie: "1234", "1235", "12345"), there will
        be only 6 unique elements: 1, 2, 3, 4, 5, 5. A simple draw
        is representing it better:
                1
                |
                2
                |
                3
              /  \
              4  5
              |
              5
    """
    words_to_insert = ["1234",
                       "1235",
                       "12345"]
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(words_to_insert)
    output = ("\nNumber of unique nodes in the Trie: {0}"
              "\nThe following words are stored in the Trie: {1}".format(
                  trie.count_unique_nodes(), words_to_insert))
    print output
    output = ("\nHere is a list of unique elements in the Trie: {0}"
              "\nThe following words are stored in the Trie: {1}".format(
                  trie.get_unique_nodes(), words_to_insert))
    print output

if __name__ == '__main__':
    trie_usage()
    trie_unique_nodes_count()
