import pytest
import TrieStruct


def test_insert_single():
    """
    Test of the structure, when a single element is inserted
    """
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(trie, ["1234"])
    assert len(trie.get_all_words()) == 1


def test_insert_list():
    """
    Test of the structure, when a collection of elements is inserted
    """
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(trie, ["1234", "5678", "345287"])
    assert len(trie.get_all_words()) == 3


def test_get_words_with_prefixes():
    """
    Test of the get words with prefix method
    """
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(trie, ["0902123456", "0902123897", "09023452",
                                      "09026745362", "76453", "98763"])
    prefix_words = trie.get_all_words_with_prefix("0902123")
    assert len(prefix_words) == 2
