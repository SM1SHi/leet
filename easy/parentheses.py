def parentheses_valid(s):
    lst = []
    check1 = ["(", "[", "{"]
    check2 = [")", "]", "}"]
    for i in s:
        lst.append(i)
    for j in check1:
        if j in lst:
            index = check1.index(j)
            if check2[index] in s and check1[index] in s:
                return True
    return False

print(parentheses_valid("{]"))
