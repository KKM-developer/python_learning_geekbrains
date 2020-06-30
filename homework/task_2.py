class Road:
    _lenght = 0
    _widht = 0

    def depth(self, dep):
        self.dep = dep
        m = self._widht * self._lenght * 25 * dep
        return m

road = Road()

road._widht = 20
road._lenght = 5000
print(road.depth(5))
