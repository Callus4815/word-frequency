import re


def get_text():
    with open('sample.txt') as file:#imports file(and closes file when done with it??)

        file = file.read()
        file = re.sub(r'[^A-Za-z\s]','',file)#strips characters
        file = re.sub(r'[\s]+',' ', file)#strips whitespace
        file = file.lower()#lowercases
        a_list = file.split()#turns file to a list of strings
    return a_list
def count_text(a_list):
    wordcount={}#my empty list to plug into
    for word in a_list:
        if word not in wordcount:
            wordcount[word] = 1
        else:                   #Counted the occurences of all words and added them to list(wordcount)
            wordcount[word] += 1
    return wordcount

def frequency(wordcount):
    a_dict = {}
    nums = sorted(wordcount.items(),key = lambda x:x[1], reverse=True)
    sorts_dic = nums[0:20]
    for item in sorts_dic:
        a_dict.update({item[0] : item[1]});
    return a_dict
def print_results(a_dict):
    an_dict = sorted(a_dict.items(),key=lambda x : x[1],reverse=True)
    for items in an_dict:
        print(items[0]+" "+str(items[1]))



def main():
    a_list = get_text()
    wordcount =  count_text(a_list)
    a_dict = frequency(wordcount)
    print_results(a_dict)


main()
