import collections

words = ["i", "love", "leetcode", "i", "love", "coding"]

k = 3
count = collections.Counter(words)
candidates = count.keys()
candidates.sort(key=lambda w: (-count[w], w))
print(candidates[:k])