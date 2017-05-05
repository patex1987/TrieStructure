# TrieStructure
> My implementation of a simple trie structure using lists for data storage

The main idea came from this code snippet: [http://pythonfiddle.com/python-trie-implementation/](http://pythonfiddle.com/python-trie-implementation/)
I wanted to make something similar but based on lists instead of dictionaries (just for the sake of fun). I've used Pylint for code linting, and Pytest for the unit tests


## Installation

To be added later

## Usage example

You can find some examples in the ExampleUsage.py code.
Creating a Trie instance:
```python
import TrieStruct
trie = TrieStruct.Trie()
```
Add a single word to the Trie:
```python
trie.insert_multiple_words(trie, ["0903127"])
```
Add collection of words to the Trie
```python
words_to_insert = ["0902123456", "0904126345", "12345678", "12356", "26736"]
trie.insert_multiple_words(trie, words_to_insert)
```

## Development setup

To be added later

## Release History

To be added later

## Meta

Gabor Patassy – patex1987@gmail.com

[https://github.com/patex1987](https://github.com/patex1987)

## Contributing

To be added later
