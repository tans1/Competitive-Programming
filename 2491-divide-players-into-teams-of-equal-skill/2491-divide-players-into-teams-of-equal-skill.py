class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        team = []
        skill.sort()
        
        if len(skill) == 2: return skill[0] * skill[1]
        
        i = 0
        j = len(skill)-1
        tm = skill[i] + skill[j]
        
        while i < j:
            if skill[i] + skill[j] != tm:
                return -1
            else:
                team.append([skill[i], skill[j]])
                i += 1
                j -= 1
        res = 0
        
        for pr in team:
            res += pr[0] * pr[1]
        return res