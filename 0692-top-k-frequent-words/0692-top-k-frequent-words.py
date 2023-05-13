class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = [(-frequency, word) for word, frequency in freq.items()]
        heapq.heapify(heap)
        
        ans = []
        temp = nsmallest(k,heap)
        temp2 = sorted(temp, key = lambda x: (x[0], x[1]))
        
        for fr, wrd in temp2:
            ans.append(wrd)

        return ans