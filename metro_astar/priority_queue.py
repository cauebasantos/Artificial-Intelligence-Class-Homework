# Priority Queue by Marcos Castro
# https://gist.github.com/marcoscastro/c6bcb67d7c50078d20fd

import heapq

class Priority_Queue:

	def __init__(self):
		self._queue = []
		self._index = 0

	def insert(self, item, priority):
		heapq.heappush(self._queue, (priority, self._index, item))
		self._index += 1

	def remove(self):
		return heapq.heappop(self._queue)[-1]