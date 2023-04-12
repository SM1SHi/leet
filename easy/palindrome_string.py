number = -121

def palindrome_str(x):
    lst = []

    for i in str(x):
        lst.append(i)

    if lst == lst[::-1]:
        return True

    else:
        return False
    
k = palindrome_str(number)
print(k)