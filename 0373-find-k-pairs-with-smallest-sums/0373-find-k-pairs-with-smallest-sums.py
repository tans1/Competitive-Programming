class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))
        count = 0

        for _ in range(k):
            if minHeap:
                val, (i, j) = heappop(minHeap)
                ans.append([nums1[i], nums2[j]])

                if i + 1 < len(nums1) and (i + 1, j) not in visited:
                    heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                    visited.add((i + 1, j))

                if j + 1 < len(nums2) and (i, j + 1) not in visited:
                    heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                    visited.add((i, j + 1))

        return ans