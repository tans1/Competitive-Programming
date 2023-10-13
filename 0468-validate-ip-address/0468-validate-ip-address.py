class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkIPV4(ip):
            list_ip = ip.split(".")
            if len(list_ip) != 4: return False
            for ip_ in list_ip:
                if not ip_.isdigit(): return False
                else:
                    if len(str(int(ip_))) != len(ip_): return False
                    else:
                        if not (0 <= int(ip_) <= 255): return False
            return True
        def checkIPV6(ip):
            list_ip = ip.split(":")
            if len(list_ip) != 8: return False
            for ip_ in list_ip:
                if not (1 <= len(ip_) <= 4): return False
                for char in ip_:
                    if char.isalpha() and not char.upper() in ["A","B","C","D","E","F"]: return False
            return True
            
        if checkIPV4(queryIP):
            return "IPv4"
        if checkIPV6(queryIP):
            return "IPv6"
        return "Neither"
        
        