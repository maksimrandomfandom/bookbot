def get_num_words(booktext):
    numofwords = len(booktext.split())
    return numofwords

def get_char(booktext):
    mydict = {}
    for char in booktext:
        char = char.lower()
        if char in mydict:
            mydict[char] += 1
        else:
            mydict[char] = 1
    return mydict

def sortlist(booktext):
    mydict = get_char(booktext)
    mylist = []
    for key, value in mydict.items():
        mylist.append({"char":key,"num":value})
    mylist.sort(key=lambda item: item["num"], reverse=True)
    return mylist







