# purpose: utilities to identify and stat files inside given directories

import os, os.path

def count(path):
    '''
    returns number of files in current path. Recursive.
    '''
    x = 0
    for name in os.listdir(path):
        fullname = os.path.join(path, name)
        if (os.path.isfile(fullname)):
            x += 1
        elif (os.path.isdir(fullname)):
            # print(f"going to check dir {fullname}")
            # y = count(fullname)
            # print(f"there are {y} files in {fullname}")
            # x += y
            x += count(fullname)
    return x

def classify(path):
    '''
    Returns dictionary containing each file type and number of appearances. 
    '''
    return recursive_classify(path, {})

def recursive_classify(path, dic):
    '''
    Returns dictionary containing each file type and number of appearances. 
    '''
    for name in os.listdir(path):
        fullname = os.path.join(path, name)
        if (os.path.isfile(fullname)):
            (_, ext) = os.path.splitext(name)
            dic = add_two_dictionaries(dic, {ext: 1})
        elif (os.path.isdir(fullname)):
            dic = recursive_classify(fullname, dic)
    return dic

def add_two_dictionaries(dic, subdic):
    '''
    adds all of subdictionary into dictionary and returns
    '''
    for (ext, val) in subdic.items():
        if (ext not in dic):
            dic[ext] = 0
        dic[ext] += val
    return dic

