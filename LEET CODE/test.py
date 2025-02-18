a= '1'
b='1'
carry='1'
i=0
d= int(a)|int(b)|int(carry)
print(d)
carry=((int(a[i])&int(b[i]))|(int(b)&carry)|(carry&int(a)))
print(carry)

