'''
Input:
s = 'I like eating cheese do you like cheese'
t = 'like cheese'

Output:
'I eating do you like cheese'
'''

from collections import Counter
def missingWords(s, t):
    s_words = s.split(' ')
    t_words = t.split(' ')
    ans = []
    t_counter = Counter(t_words)
    
    for i in range(len(s_words)):
        word = s_words[i]

        if word in t_counter:
            t_counter[word] -= 1
            if t_counter[word] == 0:
                del t_counter[word]
        else:
            ans.append(word)

    return ' '.join(ans)
    
    


