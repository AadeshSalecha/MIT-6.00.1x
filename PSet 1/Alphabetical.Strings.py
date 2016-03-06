longest = ''
current = ''
copy_s = s[:]

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        current = current + s[i]
        
    else:
        if s[i] >= s[i-1]:
            current = current + s[i]
        
        if len(current) > len(longest):
            longest = current[:]
            current = ''
    
print 'Longest substring in alphabetical order is: ',longest     