def string1(string):
    legnth=len(string)
    if legnth>2:
        if(string[-3:] == 'ing'):
            print(string+"ly")
        else:
            print(string+"ing")
sent=input("enter the string");
string1(sent)
