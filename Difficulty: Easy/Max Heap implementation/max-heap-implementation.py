class maxHeap:

    def __init__(self):
        # Initialize your data members
        self.heap = []

    # Insert x into the heap
    def push(self, x: int):
        self.heap.append(x)

        index = len(self.heap) - 1

        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    # Remove the top (maximum) element
    def pop(self):
        if len(self.heap) == 0:
            return -1

        answer = self.heap[0]

        # Move the last element to the root
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        index = 0
        n = len(self.heap)

        while True:

            left = (2 * index) + 1
            right = (2 * index) + 2

            largest = index

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]

            index = largest

        return answer

    # Return the top element or -1 if empty
    def peek(self) -> int:
        if len(self.heap) == 0:
            return -1
        return self.heap[0]

    # Return the number of elements in the heap
    def size(self) -> int:
        return len(self.heap)