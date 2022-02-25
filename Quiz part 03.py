'''
# Checking if two words are anagrams or not
from collections import Counter

def is_anagram(str1, str2):
    return (Counter(str1) == Counter(str2))

print(is_anagram("geeker", "regeek"))
print(is_anagram("qasim", "asim"))

# # Output:
# # True
# # False
'''



# x = 10
# y = x += 20

# print(x)
# # ouput: Error




'''
i = 2
for i in range (i < 2):
    i = i+3
    
print(i)
# ouput: 2
'''





# x = [(3,2), (2,3)]
# x.sort()
# print(x)

# # Output: [(2, 3), (3, 2)]





'''
x = y = [1,2,3]
y[2] = 10
print(x)

# Output: [1, 2, 10]
'''
