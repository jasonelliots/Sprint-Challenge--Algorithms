'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    #need to count how many times 'th' occurs within word 
    wordLength = len(word)

    # base case 
    if (wordLength == 0 or wordLength < 2): 
        return 0
  
  
    if (word[0 : 2] == 'th'): 
        return count_th(word[1:]) + 1 
  
    # Otherwise, return the count  
    # from the remaining index 
    return count_th(word[1:])

    
