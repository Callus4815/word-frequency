import re


def get_text():
    with open('sample.txt') as file:  #imports file(and closes file when done with it??)
        file = file.read()
        file = re.sub(r'[^A-Za-z0-9]',' ',file)#strips characters
        file = re.sub(r'[\s]+  ','', file)#strips whitespace
        file = file.lower()#lowercases
        a_list = file.split()#turns file to a list of strings
    return a_list

def ignore_words(file):
    words=[]
    all_words = get_text()
    common_words = ['a', 'able', 'about', 'across', 'after', 'all', 'almost',
     'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be',
     'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did',
     'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get',
      'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how',
      'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just',
      'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must',
      'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on',
      'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says',
      'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the',
      'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to',
      'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when',
      'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with',
      'would', 'yet', 'you', 'your', 's']
    for word in all_words:
        if word not in common_words:
            words.append(word)
    return words

def count_text(a_list):
    wordcount={}#my empty dictionary to plug into
    for word in a_list:
        if word not in wordcount:
            wordcount[word] = 1
        else:                   #Counted the occurences of all words and added them to list(wordcount)
            wordcount[word] += 1
    return wordcount

def top_20(a_dict):
    a_dict = dict(a_dict)
    top_list = sorted(a_dict.items(), key=lambda x: x[1], reverse=True)
    top20 = top_list[:20]
    return top20

def normalize(a_list, normalize_to=50):
    divisor = a_list[0][1] / normalize_to
    return divisor

def tables(a_list):
    for index in a_list:
        print(index[0].ljust(10),"|".center(1),
        ("#"*(int(index[1])//normalize(a_list))).rjust(1))

def word_frequency():
    clean = get_text()
    not_ignored = ignore_words(clean)
    counter = count_text(not_ignored)
    freq = top_20(counter)
    tables(freq)

word_frequency()
