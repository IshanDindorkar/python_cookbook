# Created by Ishan Dindorkar on 03/09/22
# Email: Ishan.Dindorkar@yahoo.com

"""
Priority Queue implementation
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))  # negated prioerity to achieve sorting from highest to lowest
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return f"Item({self._name})"


def main():
    prio_que = PriorityQueue()

    # Pushing items as per the given priority
    prio_que.push(Item("foo"), 1)
    prio_que.push(Item("bar"), 5)
    prio_que.push(Item("spam"), 4)
    prio_que.push(Item("grok"), 1)

    # Popping items from queue
    print(prio_que.pop())      # should pop the highest priority item i.e. bar
    print(prio_que.pop())      # should pop spam
    print(prio_que.pop())      # should pop foo as per the insertion order although priority is same as grok
    print(prio_que.pop())      # should pop grok as it was inserted after foo


if __name__ == "__main__":
    main()
