def merge(firstList,secondList):
    i,j = 0,0

    myMerged=[]
    while i < len(firstList) and j <len(secondList):
        if firstList[i] <= secondList[j]:
            myMerged.append(firstList[i])
            i+=i
        else:
            myMerged.append(secondList[j])
            j+=1
    myMerged.extend(firstList[i:])
    myMerged.extend(secondList[j:])
    return myMerged





