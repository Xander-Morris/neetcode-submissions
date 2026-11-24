class StockSpanner:

    def __init__(self):
        self._st = []

    def next(self, price: int) -> int:
        span = 1

        while self._st and self._st[-1][0] <= price:
            _, sp = self._st.pop()
            span += sp 
        
        self._st.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)