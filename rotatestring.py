def stringShift(s: str, shift) -> str:
    for i in range(len(shift)):
        if (shift[i][0] == 1):
            right = shift[i][1]
            first_r = s[0:len(s) - right]
            second_r = s[len(s) - right:]

            s =  second_r+first_r
        else:
            left = shift[i][1]

            first_l = s[0:left]
            second_l = s[left:]
            s = second_l+first_l
    return s

print(stringShift('abc',[[0,1],[1,2]]))