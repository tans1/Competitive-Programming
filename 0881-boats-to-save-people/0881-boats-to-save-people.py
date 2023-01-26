class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counter = i = 0
        j = len(people)-1
        people.sort()
        
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            counter += 1
        return counter