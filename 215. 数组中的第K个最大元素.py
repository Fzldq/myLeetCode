class Solution:
    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, a, b):
        self.data_list[a], self.data_list[b] = self.data_list[b], self.data_list[a]

    def insert(self, value):
        self.data_list.append(value)
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[parent] > self.data_list[index]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(index)

    def heapify(self, index=0):
        total_index = self.k
        while True:
            minvalue_index = index
            if 2 * index + 1 < total_index and self.data_list[2 * index + 1] < self.data_list[minvalue_index]:
                minvalue_index = 2 * index + 1
            if 2 * index + 2 < total_index and self.data_list[2 * index + 2] < self.data_list[minvalue_index]:
                minvalue_index = 2 * index + 2
            if minvalue_index == index:
                break
            self.swap(index, minvalue_index)
            index = minvalue_index

    def heappop(self):
        remove_data, self.data_list[0] = self.data_list[0], self.data_list[-1]
        self.data_list.pop()
        self.heapify()
        return remove_data

    def heappushpop(self, value, index=0):
        if self.data_list[0] >= value:
            return
        self.data_list[0] = value
        self.heapify()

    def findKthLargest(self, nums, k: int) -> int:
        self.k = k
        self.data_list = []
        for num in nums:
            if len(self.data_list) < k:
                self.insert(num)
            else:
                self.heappushpop(num)
        return self.data_list[0]
