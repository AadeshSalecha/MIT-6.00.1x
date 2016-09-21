'''
Author    : Aadesh Salecha
Course    : MIT 6.00.1x
Date      : October - November 2015
'''
def dict_invert(d):
    l1 = d.keys()
    l2 = d.values()
    
    ans = {}
    
    for i in range(len(l2)):
        if l2[i] in ans.keys():
            ans[l2[i]] = ans[l2[i]] + [l1[i]]
            ans[l2[i]] = sorted(ans[l2[i]])
        else:
            ans[l2[i]] = [l1[i]]
        #print ans
    
    return ans
    