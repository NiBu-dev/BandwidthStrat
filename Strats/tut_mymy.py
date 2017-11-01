# SATURN

def init_bw():
    return 15

def decision(new, list_entry):
    idList = []
    for index in xrange(len(list_entry)):
        if list_entry[index][0] == 'bronze':
            idList.append(0)
        elif list_entry[index][0] == 'silver':
            idList.append(1)
        elif list_entry[index][0] == 'gold':
            idList.append(2)
    return [newM(new), [x for x in idList]]


def newM(newmemb):                              # TODO: change this function such that it doesn't take in account the skipped entries
    if newmemb == 'bronze':
        return 0
    elif newmemb == 'silver':
        return 1
    elif newmemb == 'gold':
        return 2


