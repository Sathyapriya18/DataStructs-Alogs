def backspace(strs):

 try:

  for i in strs:
   if(i=='#'):
     if(strs):
       index=strs.index(i)
       if(index==0):
           strs=strs[1:]

       else:
        strs_r=strs[index+1:]
        strs_l=strs[:index-1]
        strs=strs_l+strs_r

  return strs
 except ValueError:
   return strs


#print(backspace('rheyggodcclgstf'))
#print(backspace('#rheyggodcclgstf'))
print(backspace('#a#c'))




