'''
953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
'''

# in the sequence of words, we only need to compare adjacent words because of transition property
# w1 < w2 < w3 etc.
# the order imposes a numbering on letters, so character comparison becomes number comparison
# words can be of different lengths, with the shorter word having a padding of nulls
def isAlienSorted(words, order):

    # create character to number mapping
    char_dict = {c:i for i,c in enumerate(order)}

    # check adjacent words, at any point returning false if order is not correct
    for i in range(len(words)-1):   #don't fall off the cliff
        word1 = words[i]
        word2 = words[i+1]

        if len(word1) > len(word2) and word1[:len(word2)] == word2:     #example would be 'apple' and 'app'
            return False

        #pick the shorter word
        for k in range(len(word1)):     
            # find first difference
            if word1[k] != word2[k]:
                if char_dict[word1[k]] > char_dict[word2[k]]:
                    return False
                break
    return True

