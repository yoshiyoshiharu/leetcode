def abc(k :int , s:int , t:int) :
    str = 'ABC'
    for i in range(0,k-1) :
        str = 'A' + str + 'B' + str + 'C'
    return str[s-1:t]

input_line = input()
s = input_line.split(' ')
print(abc(int(s[0]) , int(s[1]) , int(s[2])))
