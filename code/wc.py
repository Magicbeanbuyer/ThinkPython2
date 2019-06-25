#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def line_count(filename):
    """A function counts how many lines a file has."""
    cnt = 0
    for line in open(filename):
        cnt += 1
    return cnt

if __name__ == '__main__':
    print(line_count('wc.py'))

