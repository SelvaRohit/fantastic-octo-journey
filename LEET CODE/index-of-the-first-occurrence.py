haystack = 'abc'
needle = 'c'
occured = -1
length = len(needle)
if (haystack == needle):
    occured=0
for i in   range (len(haystack) - length+1):
    print(haystack[i:length+i])
    if haystack[i:length+i] == needle:
        occured=i
        break
print(occured)
