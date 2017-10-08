from collections import Counter
import numpy as np
import pandas as pd
import os
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt

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
    frequency_of_counts = list(distribution.values())
    sum_of_frequency = np.cumsum(frequency_of_counts)
    max_of_freq = max(sum_of_frequency)
    new_ratio = []
    for i in sum_of_frequency:
        new_ratio.append(1 - i/float(max_of_freq))
    return dict(zip(counts, new_ratio))

book_titles = {'English': {'shakespeare': ("A+Midsummer+Night's+Dream",
   'Hamlet',
   'Macbeth',
   'Othello',
   'Richard+III',
   'Romeo+and+Juliet',
   'The+Merchant+of+Venice')},
 'French': {'chevalier': ("L'enfer+et+le+paradis+de+l'autre+monde",
   "L'i%CC%82le+de+sable",
   'La+capitaine',
   'La+fille+des+indiens+rouges',
   'La+fille+du+pirate',
   'Le+chasseur+noir',
   'Les+derniers+Iroquois')},
 'German': {'shakespeare': ('Der+Kaufmann+von+Venedig',
   'Ein+Sommernachtstraum',
   'Hamlet',
   'Macbeth',
   'Othello',
   'Richard+III',
   'Romeo+und+Julia')},
 'Portuguese': {'shakespeare': ('Hamlet',)}}


hamlets = pd.DataFrame(columns=["language", "distribution"])
book_dir = "Books"
data_filepath = os.getcwd() +"/"
title_num = 1
for language in book_titles:
    for author in book_titles[language]:
        for title in book_titles[language][author]:
            if title == "Hamlet":
                inputfile = data_filepath+"Books/"+language+"/"+author+"/"+title+".txt"
                text = read_book(inputfile)
                distribution = word_count_distribution(text)
                hamlets.loc[title_num] = language, distribution
                title_num += 1

colors = ["crimson", "forestgreen", "blueviolet"]
handles, hamlet_languages = [], []
for index in range(hamlets.shape[0]):
    language, distribution = hamlets.language[index+1], hamlets.distribution[index+1]
    dist = more_frequent(distribution)
    plot, = plt.loglog(sorted(list(dist.keys())),sorted(list(dist.values()),
        reverse = True), color = colors[index], linewidth = 2)
    handles.append(plot)
    hamlet_languages.append(language)
plt.title("Word Frequencies in Hamlet Translations")
xlim    = [0, 2e3]
xlabel  = "Frequency of Word $W$"
ylabel  = "Fraction of Words\nWith Greater Frequency than $W$"
plt.xlim(xlim); plt.xlabel(xlabel); plt.ylabel(ylabel)
plt.legend(handles, hamlet_languages, loc = "upper right", numpoints = 1)
