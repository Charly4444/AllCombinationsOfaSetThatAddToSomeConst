from itertools import product


# This program gives you all the different combinantions of n-objects chosen from a specified set
# that will add up to a specified number(logSize).
# 
# initially applied this to the Logsize problem, a pre-processing stage of the optimization problem


trees = {"a":0.6, "b":1.5, "c":2}
# another test I carried
# trees = {"a":80, "b":45, "c":27}  #also logSize=180 for this problem specs
treeNames = list(trees.keys())

validLists = []

def whatLogSizes(trees, logSize=3):
    treeValues = list(trees.values())
    

# This is the mainLogic:
    def whiteListing(keyFocus, remainingLinks):

            for b in remainingLinks:
                newKeyFocus = keyFocus.copy()
                newKeyFocus.append(b)
                newRemainingLinks = [a for a in treeValues if (a+sum(newKeyFocus) <=logSize)]
                validLists.append(newKeyFocus)
                if(len(newRemainingLinks)>0): whiteListing(newKeyFocus,newRemainingLinks)
                
    for treeValue in treeValues:
        keyFocus = [treeValue]
        remainingBranches = [a for a in treeValues if (a+sum(keyFocus) <=logSize)]

        validLists.append(keyFocus)
        whiteListing(keyFocus,remainingBranches)


    # you can see the lists here... if you wish
    # print(validLists)
# ========================================================================================
# 
# 
whatLogSizes(trees)
# 
# 
# ========================================================================================
###
# Lets clean up the generated list
###


validCounts = []

def generateCounts(treeNames, validListsWithRepeats):

    tally={}

    # initialization... with names of trees "a, b, c " for instance
    for t in treeNames:
        tally.__setitem__(t,0)


    for group in validListsWithRepeats:
        tallyCopy = tally.copy()    
        for member in group:
            for k in trees.keys():
                if (trees.__getitem__(k)==member): tallyCopy.__setitem__(k, (tallyCopy.__getitem__(k) + 1))
        
        validCounts.append(tallyCopy)

    # print(validCounts)
# 
# 
# ========================================================================================
# 
# 
generateCounts(treeNames,validLists)
# 
# 
# ========================================================================================
###
# Lets remove duplicates
###
cleanedList = []
[cleanedList.append(x) for x in validCounts if x not in cleanedList]

for m in cleanedList:
    print(f"{m} \n")


### you may now include the default 0 0 0 input as the last one 
#  GOODLUCK !!
# ###