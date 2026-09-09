class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        tup_arr = []

        for key, value in counts.items():
            # where key is num and value is count
            tup_arr.append((key, value))

        tup_arr = sorted(tup_arr, key=lambda item: item[1], reverse=True)

        res = []
        for i in range(k):
            res.append(tup_arr[i][0])

        return res

        