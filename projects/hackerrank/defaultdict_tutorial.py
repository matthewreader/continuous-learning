# In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group A.
# There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
# Print the indices of each occurrence of in group . If it does not appear, print -1.

from collections import defaultdict
n_dict = defaultdict(list)
m_list = []

n, m = map(int, input().split())

for i in range(0, n):
    n_dict[input()].append(i+1)

for i in range(0, m):
    m_list = m_list+[input()]

for word in m_list:
    if word in n_dict:
        print(" ".join(map(str, n_dict[word])))
    else:
        print(-1)
