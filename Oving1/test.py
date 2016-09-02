from sys import stdin
import timeit
tstart = timeit.default_timer()

b = stdin.readlines()
print(max(b))

tend = timeit.default_timer()
print('time: {}'.format(tend - tstart))

