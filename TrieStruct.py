"""
My implementation of a Trie structure
"""


class Trie(object):
    """
    Trie structure class
    """
    def __init__(self, cur_char=None, is_word=False, word=None):
        """
        Constructor of the Trie class

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            cur_char (:obj:`str`): The character of the current node
            is_word (bool, optional): A boolean determining if a node points
                to a word
            word (:obj:`str`): The word stored at the node

        """
        self.cur_char = cur_char
        self.is_word = is_word
        self.children = []
        self.word = word

    def __insert__(self, word, string_pos=0):
        """
        Inserts a simple word into the Trie (internal method)

        Args:
            word (:obj:`str`):
                word to insert
            string_pos (int, Optional): position of the character
                in the current word

        Returns:
            None: this method doesnt return any value

        Raises:

        Todo:

        Example:
        """
        current_char = word[string_pos]
        if current_char not in self.__get_children_chars__():
            self.children.append(Trie(current_char))
        current_char_position = self.__find_char_pos_in_childs__(current_char)
        if string_pos + 1 == len(word):
            self.children[current_char_position].is_word = True
            self.children[current_char_position].word = word
        else:
            self.children[current_char_position].__insert__(
                word,
                string_pos + 1)

    def insert_multiple_words(self, words, string_pos=0):
        """
        Inserts a collection of words into the Trie

        Args:
            words (:obj:`list` or :obj:'tuple' of :obj:`str`):
                List or tuple of words
            string_pos (int, Optional): position of the character
                in the current word

        Returns:
            None: this method doesnt return any value

        Raises:

        Todo:

        Example:

        """
        for word in words:
            self.__insert__(word)

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

    def get_all_words(self):
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
            words += child.get_all_words()
        return words

    def count_unique_nodes(self):
        """
        Calculates the count of unique nodes in the Trie

        Args:

        Returns:
            count (int):
                Count of the unique nodes

        Raises:

        Todo:

        Example:

        """
        count = 0
        for child in self.children:
            count += 1
            count += child.count_unique_nodes()
        return count

    def get_unique_nodes(self):
        """
        Returns a list of unique nodes in the Trie

        Args:

        Returns:
            count (int):
                Count of the unique nodes

        Raises:

        Todo:

        Example:

        """
        unique_nodes = []
        for child in self.children:
            unique_nodes.append(child.cur_char)
            unique_nodes += child.get_unique_nodes()
        return unique_nodes

    def get_all_words_with_prefix(self, prefix):
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
        words = prefix_node.get_all_words()
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
