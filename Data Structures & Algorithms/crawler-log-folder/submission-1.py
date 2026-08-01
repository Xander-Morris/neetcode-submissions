class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st = []

        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                if st:
                    st.pop()
            else:
                st.append(log)

        return len(st)