# Hamilton Evans 
# CSCI 0302 
# Implementation Project 2
# 12/07/2018

"""
This program uses Dynamic Programming to find 
the LCS of two words given by the user. 

Starts automatically when run and prints out animation 
and the step it is on in the console.  
To see each step clearly run on manual speed (click enter to make proceed)
"""

from time import sleep 

def runFunction (): 
    """
    Putting it all together.  Gathers user input and runs the whole program.
    """

    word1 = str(input ('First Sequence: ')).lower().strip().replace(' ', '')
    word2 = str(input ('Second Sequence: ')).lower().strip().replace(' ', '')
    speed = str(input ('How fast would you like to fill out the table? (manual, slow, med, fast, superspeed): ')).lower().strip().replace(' ', '')
    # .lower().strip().replace(' ', '') to get rid of spaces, capital letters
    
    if (speed == 'manual'): 
        print("Press 'Enter' to continue") # Otherwise not clear how to proceed
        input()
        
    table = dynamWoohoo(word1, word2, speed) # Filling out table
    
    if (word1[-1] == word2[-1]): # Fixing bug at the very last step in filling out table
        printTable (table, word1, word2, speed, 'back', 2)
    else: 
        printTable (table, word1, word2, speed, 'back', 3)

    LCS = whatIsLCS (table, word1, word2) # Backtracking through table
    printTable (table, word1, word2, 'slow', 'final', 6, LCS) # Printing final table
    

def dynamWoohoo (word1, word2, speed): 
    """
    This is the core dynamic function.
    Builds the table as a 2-d array and fills it out.
    """
    x = len(word1)
    y = len(word2)

    store = [[' '] * (x+1) for i in range(y+2)] # Initiallizing array
    
    for i in range (x+1): # x and y are incremented by one for base case row.
        for j in range (y+1): 
            if (i == 0 or j == 0): # Base Case
                store[j][i] = 0
                printTable(store, word1, word2, speed, 'fill', 0)
                
            elif (word1[i-1] == word2[j-1]): # Letters are same, increment! 
                store[j][i] = store[j-1][i-1]+1
                printTable(store, word1, word2, speed, 'fill', 1)
                
            else: 
                store[j][i] = max(store[j-1][i], store[j][i-1]) 
                # Letters are different. Take max of number above and number to left.
                printTable(store, word1, word2, speed, 'fill', 2)

    return store

def whatIsLCS (store, word1, word2): 
    """
    This function backtracks through the table and 
    builds the LCS appropriately.
    """
    j = len(word1)
    i = len(word2)
    LCS = ''
    
    while (i>0 and j>0): # Until we hit one of the axis
        if (store[i][j] == store[i-1][j]): # Letter from word 2 doesn't match
            store[i][j] = 'X' # Marking path through table
            i-=1
            printTable(store, word1, word2, 'slow', 'back', 3, LCS)  

        elif (store[i][j] == store[i][j-1]): # Letter from word 1 doesn't match
            store[i][j] = 'X'
            j-=1
            printTable(store, word1, word2, 'slow', 'back', 4, LCS)  
            
        else: # Letters match!
            LCS = word1[j-1] + LCS # Add letter to LCS
            store[i][j] = 'X' 
            i-=1
            j-=1
            printTable(store, word1, word2, 'slow', 'back', 5, LCS)
        
    store[i][j] = 'X' # Fixing bug that didn't fill out the last step
    printTable(store, word1, word2, 'slow', 'back', 6, LCS)
    
    return LCS

def printTable (table, word1, word2, speed, fill, turn, LCS=''):
    """
    This function prints the table and the sentences before and after.
    """
    howFast (speed)
         
    print (50*'\n') # Only one board on the console at a time
    
    if (fill == 'fill'): # What is happening
        print('Filling out table:')
    elif (fill == 'back'): 
        print('Backtracking through table:')
    elif(fill == 'final'): 
        print('Final Table:')
    
    whatsHappening = [ # What step is happening
        'Base Case.', 
        'Letters are the same! Increasing index', 
        'Letters are different. Taking max of left and above.', 
        "Word 2 letter isn't in LCS. Moving up.", 
        "Word 1 letter isn't in LCS. Moving to left.", 
        'Letters are the same! Adding to LCS.',
        'Table Complete!'
    ]
    print(whatsHappening[turn])
        
    print ()
    print('     ', end = '') # Formatting
    
    for z in range(len(word1)): # Printing word 1 at top
        print (word1[z], end='')
        print(' ', end = '')
    print('\n') 
    
    for i in range(len(word2) + 1): 
        if (i!=0): 
            print(word2[i-1], end = '  ') # Prining word 2 vertical
        else: # Formatting Base Case line
            print('   ', end = '') 
            
        for j in range(len(word1) + 1):
            print (table[i][j], end=' ') # Printing table
            
        print()
    print ()
    print('Longest Common Subsequence: ' + str(LCS)) # Live Updating the LCS
    
    if (speed == 'manual'): # To make clear how to proceed
        print()
        print("Press 'Enter' to continue")
        
    
def howFast (speed):
    """
    Controlling the speed.
    """
    if (speed == 'manual'): 
        input()
    elif (speed == 'slow'):
        sleep (1)
    elif (speed == 'med'): 
        sleep (0.4)
    elif (speed == 'fast'):
        sleep(0.25)
       
runFunction () # Running it all!