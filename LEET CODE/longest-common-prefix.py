strs = ["flower","flow","flight"]
string = ""
match= True
for index,each_letter in enumerate(min(strs)):
    # print(each_letter)
    # print(match)
    if (match):
        # print(1)
        string = string + each_letter
        for each_element in strs:
            if (each_element[index] == each_letter):
                match = True
            else:
                match = False
                string = string[:-1]
                break
    else:
        break
print(string)
        
            
