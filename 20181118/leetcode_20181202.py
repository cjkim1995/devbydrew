
def backspaceCompare(self, S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    if self.string_without_backspaces(S) == self.string_without_backspaces(T):
        return True
    return False
    
    
def string_without_backspaces(self, U):
    U_lst = []
    for i in U:
        if i == "#":
            U_lst.pop()
        else:
            U_lst.append(i)
    return "".join(U_lst)



def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    seen = []
    openp = ['(', '[', '{']
    closep = [')', ']', '}']
    p_dict = {')':'(', ']':'[', '}':'{'}
    for i in s:
        if i in openp:
            seen.append(i)
        elif i in closep:
            if len(seen) > 0:
                if p_dict[i] != seen.pop():
                    return False
            else:
                return False
    if len(seen) == 0:
        return True
    return False