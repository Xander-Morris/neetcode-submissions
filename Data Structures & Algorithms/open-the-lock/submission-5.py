class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        st = set(deadends)

        if "0000" in st:
            return -1

        def _build_next_combos(base_combo):
            valid_combos = []

            for i in range(len(base_combo)): 
                to_num = int(base_combo[i])
                valid_next_nums = []

                if to_num < 9:
                    valid_next_nums.append(to_num + 1)
                if to_num > 0:
                    valid_next_nums.append(to_num - 1)
                if to_num == 0:
                    valid_next_nums.append(9)
                elif to_num == 9:
                    valid_next_nums.append(0)

                for next_num in valid_next_nums:
                    combo = base_combo.copy()
                    combo[i] = str(next_num)

                    if "".join(combo) in st:
                        continue

                    valid_combos.append(combo)
            
            return valid_combos
                    
        q = deque()
        q.append((0, ['0', '0', '0', '0']))
        visited = set("0000")
        min_turns = float('inf')

        while q:
            turns, combo = q.popleft()

            if "".join(combo) == target:
                min_turns = min(min_turns, turns)

            next_combos = _build_next_combos(combo)
            
            for next_combo in next_combos:
                if "".join(next_combo) in visited:
                    continue
                visited.add("".join(next_combo))
                q.append((turns + 1, next_combo))

        return min_turns if min_turns != float('inf') else -1