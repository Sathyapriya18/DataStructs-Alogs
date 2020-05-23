def checlstring(s):
    star = []
    para = []
    for i in range(len(s)):
        if (s[i] == '('):
            para.append(i)
        elif (s[i] == '*'):
            star.append(i)
        else:
            if (para):
                para.pop()
            elif (star):
                star.pop()
            else:
                return False
    while (para):
        if (not (star)):
            return False
        elif (para[0]< star[0]):
            para.pop()
            star.pop()
        else:
            return False
    return True







#print(checlstring('(((******))'))
print(checlstring('((()))()(())(*()()())**(())()()()()((*()*))((*()*)'))
