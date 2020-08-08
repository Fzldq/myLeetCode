class Solution:
    def get_parent_index(self, index):
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, a, b):
        self.data_list[a], self.data_list[b] = self.data_list[b], self.data_list[a]

    def insert(self, key, value):
        self.data_list.append([key, value])
        index = len(self.data_list) - 1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[parent][1] > self.data_list[index][1]:
            self.swap(parent, index)
            index = parent
            parent = self.get_parent_index(index)

    def heappushpop(self, key, value, index=0):
        if self.data_list[0][1] >= value:
            return
        self.data_list[0] = [key, value]
        while True:
            minvalue_index = index
            if 2 * index + 1 < self.k and self.data_list[2 * index + 1][1] < self.data_list[minvalue_index][1]:
                minvalue_index = 2 * index + 1
            if 2 * index + 2 < self.k and self.data_list[2 * index + 2][1] < self.data_list[minvalue_index][1]:
                minvalue_index = 2 * index + 2
            if minvalue_index == index:
                break
            self.swap(index, minvalue_index)
            index = minvalue_index

    def topKFrequent(self, nums, k):
        from collections import Counter
        self.k = k
        self.data_list = []
        dic = Counter(nums)
        for key, value in dic.items():
            if len(self.data_list) < k:
                self.insert(key, value)
            else:
                self.heappushpop(key, value)
        return [i[0] for i in self.data_list]


nums = [1, 2]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
