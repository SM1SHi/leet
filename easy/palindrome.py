# !! DOES NOT WORK FOR NEGATIVE NUMBERS 
f = 121
def is_palindrome(x):
    lst = []
    while x > 0:
        lst.insert(0, x % 10)
        x //= 10 
    if lst == lst[::-1]:
        return True
    else:
        return False

k = is_palindrome(f) 
print(k)