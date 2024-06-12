import time
from platform import python_version

# Common letters in two strings
# intersection function of sets (&) and put into a list
def common(s1,s2):
    a = list(set(s1)&set(s2))
    return a
s1, s2 = 'pythonn', 'cythonn'
print(common(s1, s2))

# Speed test
def speed_test():
    n = 0
    start_time = time.perf_counter_ns()
    while(n < 1000000):
        n += 1
    print(time.perf_counter_ns() - start_time, 'ns')

print('Speed test in version', python_version(), ':')
speed_test()