def reverse_string(s):
    return(s[::-1])

'''some working Examples'''
print(reverse_string("hello"))
print(reverse_string("Andela"))
print(reverse_string("Andela Bootcamp test"))
#comment

def swap(list_,i,j):
    list_[i], list_[j] = list_[j], list_[i]

def reverse_x(s):
    s = list(s)
    length = len(s)
    for i in range(length//2):
        swap(s,i,length-1-i)
                
    return s
print (reverse_x("Denis"))

