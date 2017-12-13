"""wcount.py: count words from an Internet file.

__author__ = "Zhangsan"
__pkuid__  = "1600012345"
__email__  = "zhangsan@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    counts={}
    for x in range(64):
        lines=lines.replace(chr(x),' ')
    words=lines.split()
    for l in words:
        counts[l]=counts.get(l,0)+1
    numbers=list(counts.values())
    numbers.sort()
    number=set(numbers)
    numbers=list(number)
    numbers.reverse()
    n=0
    m=0
    while n <=9 and n<=len(numbers)-1:
        for i in counts.keys():
            if counts[i]==numbers[n] and m<=9:
                print('%-10s'%i,counts[i])
                m=m+1
        n=n+1
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
