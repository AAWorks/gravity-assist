class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    @property
    def coordinates(self):
        return (self.x, self.y)
    def distance_to(self, point_two: "Point"):
        """Distance formula based calculation"""
        return (
            ((self.x - point_two.x) ** 2) +
            ((self.y - point_two.y) ** 2)
        ) ** 0.5
    def in_circle(self, radius: int, origin: "Point"):
        """Bool whether or not point is in circle"""
        return self.distance_to(origin) <= radius
    def __str__(self):
        return f"({self.x}, {self.y})"
