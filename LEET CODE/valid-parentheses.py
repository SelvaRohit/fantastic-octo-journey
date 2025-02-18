s = "([]"
valid=False
open_parentheses=[]
for i in s:
    print(i)
    try:
        if(i in ["(","[","{"]):
            open_parentheses.append(i)
            valid=False
            print(open_parentheses)
            continue
        elif(i == ")" and open_parentheses[-1] == "("):
            open_parentheses = open_parentheses[:-1]
            valid=True
            continue
        elif(i == "}" and open_parentheses[-1] == "{"):
            open_parentheses = open_parentheses[:-1]
            valid=True
            continue
        elif(i == "]" and open_parentheses[-1] == "["):
            open_parentheses = open_parentheses[:-1]
            valid=True
            print(open_parentheses)
            continue
        else:
            print("else")
            print(open_parentheses[-1])
            valid=False
            break
    except IndexError:
        valid=False
        break
print(valid and len(open_parentheses) == 0)
        


    
