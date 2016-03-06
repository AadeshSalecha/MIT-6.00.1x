s = 'azcbobobegghakl'

counter = 0

for num in range(len(s)):
    
    if s[num] == 'a' or s[num] == 'u' or s[num] == 'o' or s[num] == 'i' or s[num]  == 'e':
        counter += 1
    
print "Numer of vowels: " + str(counter)