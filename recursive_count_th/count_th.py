'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    ctr = 0
    idx = word.find('th')
    if (idx is -1):
        return 0
    else:
        ctr = 1 + count_th(word[idx+2:])  
    return ctr