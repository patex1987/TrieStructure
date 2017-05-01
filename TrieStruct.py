"""
My implementation of a Trie structure
"""


class TrieNode(object):
    """
    Trie structure class
    """
    def __init__(self, cur_char=None, is_word=False, word=None):
        self.cur_char = cur_char
        self.is_word = is_word
        self.children = []
        self.word = word

    def __insert_multiple_words__(self, root_object, words, word_pos=0,
                                  string_pos=0):
        """
        Inserts a collection of words into the Trie

        Args:
            words (:obj:`list` or :obj:'tuple' of :obj:`str`):
                List or tuple of words
            word_pos (int, Optional): position of the word in the
                words collection
            string_pos (int, Optional): position of the character
                in the current word

        Returns:
            None: this method doesnt return any value

        Raises:

        Todo:
            sending the root_object in the argument is a kind of forced
            solution

        Example:

        """
        word = words[word_pos]
        current_char = word[string_pos]
        if current_char not in self.__get_children_chars__():
            self.children.append(TrieNode(current_char))
        current_char_position = self.__find_char_pos_in_childs__(
            current_char)
        if string_pos + 1 == len(word):
            self.children[current_char_position].is_word = True
            self.children[current_char_position].word = word
            if word_pos + 1 == len(words):
                return
            root_object.__insert_multiple_words__(
                root_object,
                words,
                word_pos + 1,
                0)
        else:
            self.children[current_char_position].__insert_multiple_words__(
                root_object,
                words,
                word_pos,
                string_pos + 1)

    def __find_char_pos_in_childs__(self, char):
        """
        Finds the position of the character in the list of childrens of
        the current Node

        Args:
            char (:obj:`str`): the character to find

        Returns:
            index (int): The position of the character

        Raises:

        Todo:

        Example:

        """
        for index, child in enumerate(self.children):
            if child.cur_char == char:
                return index

    def __get_children_chars__(self):
        """
        Gets the list of all childrens of the current Node

        Args:

        Returns:
            children_chars (:obj:`list` of :obj:'str'):
                list child nodes

        Raises:

        Todo:

        Example:

        """
        children_chars = list()
        for child in self.children:
            children_chars.append(child.cur_char)
        return children_chars

    def __get_all_words__(self):
        """
        Gets all the words stored in the Trie

        Args:

        Returns:
            words (:obj:`list` of :obj:'str'):
                list of words stored in the Trie (starting from the given node)

        Raises:

        Todo:

        Example:

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

        Args:
            prefix(:obj:'str'): The prefix

        Returns:
            words (:obj:`list` of :obj:'str'):
                list of words stored in the Trie,
                starting from the given prefix

        Raises:

        Todo:

        Example:

        """
        # words = list()
        prefix_node = self.__get_prefix_node__(prefix, 0)
        if prefix_node is None:
            return None
        words = prefix_node.__get_all_words__()
        return words

    def __get_prefix_node__(self, prefix, position):
        """
        Returns the node containing the prefix, if there is such

        Args:
            prefix(:obj:'str'): The prefix

        Returns:
            words (:obj:`list` of :obj:'str'):
                list of words stored in the Trie,
                starting from the given prefix

        Raises:

        Todo:

        Example:

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

    def insert_multiple_words(self, words):
        """
        Inserts the provided word into the trie structure
        """
        self.root.__insert_multiple_words__(self.root, words)

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
MY_TRIE.insert_multiple_words(["1234", "1236", "1235", "11", "12"])
print MY_TRIE.get_words()
