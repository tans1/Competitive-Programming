class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        pos_sp = []
        n = len(position)

        for i in range(n):
            pos_sp.append([position[i], speed[i]])

        ps = sorted(pos_sp, key = lambda x: -x[0]) # sort by closenes to the target
        
        for i in range(n):
            t = (target - ps[i][0]) / ps[i][1] #time required to get at the destination
            time.append(t)
        st = []
        
        for t in time: 
            if not st:
                st.append(t)
            elif st and st[-1] < t: # can the car with t be catched by st[-1] (or the behind)?
                st.append(t)

        return len(st)
                

