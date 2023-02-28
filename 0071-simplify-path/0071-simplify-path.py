class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        temp = path.split("/")
        for i in range(len(temp)):
            if len(temp[i]) != 0:
                if temp[i] == ".":
                    continue

                elif st and temp[i] == "..":
                    st.pop()

                else:
                    st.append(temp[i])
        res = ""
        for x in st:
            if x != "..":
                res += "/" + x
        if len(res) == 0:
            res = "/"
        return res