#!/usr/local/bin/python3

import queue as q

def hot_potato(names, num):
    queue = q.Queue()
    for name in names:
        queue.enqueue(name)

    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()


print(hot_potato(('Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'), 9))
