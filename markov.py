"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split() 

    for word in range(len(words)-2):
        keys = (words[word], words[word + 1])
        # print('keys =' , keys)
        # generate values
        # pair the keys and values
        # put them into chains {}
        # print(keys[word])
        # print(chains.keys())
        if keys in chains.keys():
            # chains.keys() will be empty 1st time running it -> False.
            # check to see if key is in chains. If it is, append the value to the list of value of keys
            chains[keys].append(words[word + 2])
        else:
            chains[keys] = []
                # chains[("hi", "there")] = [] (created empty list)
            chains[keys].append(words[word + 2])
                # add word[2] (i.e. mary) in to the list of chains[("hi", "there")]


        #how to loop to avoid index error?
        
    return chains


# def make_text(chains):
#     """Return text from chains."""

#     words = []

#     # your code goes here

#     return ' '.join(words)


# input_path = 'green-eggs.txt'

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)
