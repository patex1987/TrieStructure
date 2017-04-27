"""
My implementation of a Trie structure
"""


class TrieNode(object):
    """
    The basic node for the Trie
    """
    def __init__(self, cur_char=None, is_word=False, word=None):
        self.cur_char = cur_char
        self.is_word = is_word
        self.children = []
        self.word = word

    def __insert__(self, word, string_pos=0):
        """
        Inserts a word into the Trie structure
        """
        current_char = word[string_pos]
        if current_char not in self.__get_children_chars__():
            self.children.append(TrieNode(current_char))
        current_char_position = self.__find_char_pos_in_childs__(current_char)
        if string_pos + 1 == len(word):
            self.children[current_char_position].is_word = True
            self.children[current_char_position].word = word
        else:
            self.children[current_char_position].__insert__(
                word,
                string_pos + 1)

    def __find_char_pos_in_childs__(self, char):
        """
        Finds the position of the character in the list of childrens of
        the current Node
        """
        for index, child in enumerate(self.children):
            if child.cur_char == char:
                return index

    def __get_children_chars__(self):
        """
        Gets the list of all childrens of the current Node
        """
        children_chars = list()
        for child in self.children:
            children_chars.append(child.cur_char)
        return children_chars

    def __get_all_words__(self):
        """
        Gets all the words stored in the Trie
        """
        words = list()
        for child in self.children:
            if child.is_word:
                words.append(child.word)
            words += child.__get_all_words__()
        return words

    def __get_all_words_with_prefix__(self, prefix):
        """
        Gets all words starting with the given prefix
        """
        # words = list()
        prefix_node = self.__get_prefix_node__(prefix, 0)
        if prefix_node is None:
            return None
        words = prefix_node.__get_all_words__()
        return words

    def __get_prefix_node__(self, prefix, position):
        """
        Gets all the words stored in the Trie
        """
        if position == len(prefix):
            return self
        if prefix[position] in self.__get_children_chars__():
            child_index = self.__find_char_pos_in_childs__(prefix[position])
            return self.children[child_index].__get_prefix_node__(prefix,
                                                                  position + 1)
        else:
            return None


class Trie(object):
    """
    Trie implementation using lists to store the data
    """
    def __init__(self):
        """
        Constructor - creates the root node - a TrieNode object
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the Trie structure
        """
        self.root.__insert__(word)

    def get_words(self):
        """
        Gets a list of all words stored in the Trie
        """
        return self.root.__get_all_words__()

    def get_words_with_prefix(self, prefix):
        """
        Gets a list of all words stored starting with the provided prefix
        """
        return self.root.__get_all_words_with_prefix__(prefix)


MY_TRIE = Trie()
MY_TRIE.insert("0902")
MY_TRIE.insert("0903")
MY_TRIE.insert("0904")
MY_TRIE.insert("085625")
MY_TRIE.insert("8765625")

print MY_TRIE.get_words_with_prefix("0")
