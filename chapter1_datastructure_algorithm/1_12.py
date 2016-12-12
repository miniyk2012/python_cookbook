import logging

_logger = logging.getLogger(__name__)

# 怎样找出一个序列中出现次数最多的元素呢？

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
print(word_counts)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['not'])

morewords = ['why','are','you','not','looking','in','my','eyes']
# for word in morewords:
#     word_counts[word] += 1
word_counts.update(morewords)
word_counts.update({'why':1})
print(word_counts)