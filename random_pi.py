import math
import multiprocessing
import random


def dartboard_hits(iterations):
    count = 0.0

    for _ in xrange(iterations):
        x = random.random()
        y = random.random()
        dist = math.sqrt((x * x) + (y * y))
        if dist <= 1.0:
            count += 1.0

    return count


def random_pi(iterations=1000000):
    return 4.0 * (dartboard_hits(iterations) / float(iterations))


def parallel_random_pi(iterations=1000000, processes=4):
    pool = multiprocessing.Pool(processes)
    hits = sum(pool.map(dartboard_hits, [iterations // processes] * processes))
    return 4.0 * (hits / float(iterations))


print random_pi(iterations=10000000)
print parallel_random_pi(iterations=10000000, processes=8)
