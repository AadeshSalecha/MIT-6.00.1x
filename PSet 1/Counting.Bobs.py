s = '1bob2bob3bob4bob'

bob = "bob"
counter = 0

while True:
        index = s[0:len(s) + 1].find(bob)
        
        if(index != -1):
            counter += 1
            s = s[index+1:len(s)]

        else :
            break
            
print counter