a = "1010"
b = "1011"
out=""
carry=0
if(len(a)<len(b)):
    a=(len(b)-len(a))*'0'+a
elif(len(a)>len(b)):
    b=(len(a)-len(b))*'0'+b
# largest=(len(a),len(b))[len(a)<len(b)]
print(a,b)
for i in range(len(a)-1,-1,-1):
    # if(i==1):
    #      print(a[i],b[i],carry)
    out=str(int(a[i])^int(b[i])^carry)+out
    carry=((int(a[i])&int(b[i]))|(int(b[i])&carry)|(carry&int(a[i])))
    # if(i==1):
    #     print(out,carry)
if carry:
    out='1'+out
print(out)
