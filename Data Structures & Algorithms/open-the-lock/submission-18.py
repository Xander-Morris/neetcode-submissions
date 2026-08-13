class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        st = set(deadends)
        visited = set("0000")

        if "0000" in st:
            return -1

        def _build_next_combos(base_combo):
            valid_combos = []

            def _add_valid_combo(i, next_num):
                combo = base_combo.copy()
                combo[i] = str(next_num)
                s = "".join(combo)

                if s in st:
                    return
                if s in visited:
                    return

                visited.add(s)
                valid_combos.append(combo)

            for i in range(len(base_combo)): 
                to_num = int(base_combo[i])

                if to_num < 9:
                    _add_valid_combo(i, to_num + 1)
                if to_num > 0:
                    _add_valid_combo(i, to_num - 1)
                if to_num == 0:
                    _add_valid_combo(i, 9)
                elif to_num == 9:
                    _add_valid_combo(i, 0)
            
            return valid_combos

        q = deque([['0', '0', '0', '0']])
        turns = 0

        while q:
            for _ in range(len(q)):
                combo = q.popleft()

                if "".join(combo) == target:
                    return turns 

                next_combos = _build_next_combos(combo)
                
                for next_combo in next_combos:
                    q.append(next_combo)
            turns += 1

        return -1