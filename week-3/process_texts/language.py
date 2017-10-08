from collections import Counter

text = "This is my text text. We're keeping this text short to keep things manageable."

def count_words(text):
    '''
    Count the number of times each word occurs in text(str).
    '''
    text = text.lower()
    word_counts = {}
    skips = [".", ",", ":", ";", "'", '"']
    for char in skips:
        text = text.replace(char, "")
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def count_words_fast(text):
    '''
    Count the number of times each word occurs in text(str).
    '''
    text = text.lower()
    skips = [".", ",", ":", ";", "'", '"']
    for char in skips:
        text = text.replace(char, "")

    word_counts = Counter(text.split(" "))
    return word_counts

def read_book(title_path):
    '''
    Read a book and return it as a string
    '''
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r", "")
    return text

def word_stats(word_counts):
    '''
    Return number of unique words and word frequencies.
    '''
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

def word_count_distribution(text):
    '''
    Takes a string as input.
    '''
    word_counts = count_words_fast(text)
    count_distribution = {}
    for key in word_counts.values():
        if key in count_distribution:
            count_distribution[key] += 1
        else:
            count_distribution[key] = 1
    return count_distribution

def more_frequent(distribution):
    '''
    You might begin with storing the counts of the distribution as follows: counts = list(distribution.keys())
    Store the values of the distribution with frequency_of_counts = list(distribution.values()).
    numpy is preloaded into memory as np: find the cumulative sum of these using np.cumsum().
    To obtain the fraction of words more frequent than this, divide this cumulative sum by its maximum,
    and subtract this value from 1. You're ready to make a dictionary with the results of this calculation as values
    and counts as keys!
    '''
    counts = list(distribution.keys())
    return distribution
