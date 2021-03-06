import pytest
import TrieStruct


def test_insert_single():
    """
    Test of the structure, when a single element is inserted
    """
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(["1234"])
    assert len(trie.get_all_words()) == 1


def test_insert_list():
    """
    Test of the structure, when a collection of elements is inserted
    """
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(["1234", "5678", "345287"])
    assert len(trie.get_all_words()) == 3


def test_get_words_with_prefixes():
    """
    Test of the get words with prefix method
    """
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(["0902123456", "0902123897", "09023452",
                                "09026745362", "76453", "98763"])
    prefix_words = trie.get_all_words_with_prefix("0902123")
    assert len(prefix_words) == 2


def test_count_unique_nodes():
    """
    Test of the count_unique_nodes method
    """
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(["1234"])
    assert trie.count_unique_nodes() == 4
    trie.insert_multiple_words(["1235"])
    assert trie.count_unique_nodes() == 5
    trie.insert_multiple_words(["12345"])
    assert trie.count_unique_nodes() == 6
    trie.insert_multiple_words(["234"])
    assert trie.count_unique_nodes() == 9


def test_get_unique_nodes():
    """
    Test of the get_unique_nodes method
    """
    trie = TrieStruct.Trie()
    trie.insert_multiple_words(["1234"])
    assert len(trie.get_unique_nodes()) == 4
    trie.insert_multiple_words(["1235"])
    assert len(trie.get_unique_nodes()) == 5
    trie.insert_multiple_words(["12345"])
    assert len(trie.get_unique_nodes()) == 6
    trie.insert_multiple_words(["234"])
    assert len(trie.get_unique_nodes()) == 9
    assert sorted(trie.get_unique_nodes()) == sorted(
        ["1", "2", "3", "4", "5", "5", "2", "3", "4"])
