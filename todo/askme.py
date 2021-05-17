#!/usr/bin/env python
# ask me and make choice
print('Press Ctrl-C to quit.')
stat = '*-* ASK ME'
try:
    while True:
        print(stat)
        print('\b' * len(stat), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')