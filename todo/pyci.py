#!/usr/bin/env python
# ci use
print('Select A')
print('Select B')
print('Select C')
print('Press Ctrl-C to quit.')
try:
    while True:
        print('\b' * 6, end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')