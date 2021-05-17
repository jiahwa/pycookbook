#!/usr/bin/env python
# ask me and make choice
print('Press Ctrl-C to quit.')
stat = '** ASK ME **'
count = 1
try:
    while count-1<len(stat):
        # back keyboard count times, count ++ until len(stat), end is from count pos to the last pos
        startPos = len(stat) - count
        endPos = len(stat)
        count = count + 1
        # if(count == endPos):
        #     count = 1
        print('\b' * 12, end=stat[0:startPos] + '/' + stat[startPos+1:endPos], flush=True)
except KeyboardInterrupt:
    print('\nDone.')