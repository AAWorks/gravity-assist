from .point import Point
from .constants import G

class Planet:
    def __init__(self, mass: int, radius: int, origin: Point):
        self._m = mass
        self._r = radius
        self._origin = origin
    @property
    def mass(self):
        return self._m
    @property
    def radius(self):
        return self._r
    @property
    def origin(self):
        return self._origin
    def gravitational_force(self, distance: int, object_mass: int):
        """Get gravitational force exerted on an object of mass object_mass and distance distance"""
        return (G * self._m * object_mass) / (distance ** 2)
    def __str__(self):
        return f"Planet(Mass={self._m}, Radius={self._r}, Origin={self._origin})"
