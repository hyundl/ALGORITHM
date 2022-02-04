def isPalindrome(self, x):
    if x < 0:
        return False
    revx = int(str(x)[::-1])
    if x == revx:
        return True
    else:
        return False  
