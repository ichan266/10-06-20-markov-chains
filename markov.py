"""Generate Markov text from text files."""

from random import choice

import os

import discord

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


def make_text(chains):
    """Return text from chains."""

    words = []
    # print(type(list(chains.keys())))
    random_key = choice(list(chains.keys()))
    words.append(random_key[0])
    words.append(random_key[1])    
    #Select a random key from chains as a starting point.
    #Append the first item from random_key (tuple) to words.
    #Append the second item from random_key (tuple) to words.
    new_value_from_random_key = choice(chains[random_key])
    #Randomly select a Value from the dictionary that is paired with random_key.
    words.append(new_value_from_random_key)
    #Append this Value to the end of words.
    new_key = (words[-2], words[-1])
    #Look at the last two indexes in words; this is your new key.
    while new_key in chains:
        new_value = choice(chains[new_key])
        words.append(new_value)
        new_key = (words[-2], words[-1])
    #If your new key is in the dictionary:
        #continue adding words.

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

#print(random_text)



# Using robot to reply message on Discord

client = discord.Client()
# Create instance of a Client. This client is the connection to Discord

@client.event # it is a decorator to register an event (in a "callback style")

async def on_ready():  # on_ready() event is called when the bot has finished logging in & setting things up
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):  #on_message() event is called when the bot has received a message
    if message.author == client.user:  #  ignore message from ourselves (bot)
        return
    print(f"channel type is {str(type(message.channel))}, {message.content}")
    print(f"text channel is {message.channel.name}")
    if type(message.channel) == discord.channel.DMChannel:
        await message.channel.send(make_text(chains))

client.run(os.environ['DISCORD_TOKEN'])
