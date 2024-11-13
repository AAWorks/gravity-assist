import math

from .point import Point
from .planet import Planet

class Spaceship:
    def __init__(
            self,
            mass: int,
            v0_y: int,
            v0_x = 0,
            starting_loc = Point(0, 0),
            starting_heading = 0
        ):
        self._m = mass
        self._v_y = v0_y
        self._v_x = v0_x
        self._heading = starting_heading
        self._loc = starting_loc

        self._path = [self._loc.coordinates]
        self._crashed = False
    @property
    def mass(self):
        return self._m
    @property
    def velocity_x(self):
        return self._v_x
    @property
    def velocity_y(self):
        return self._v_y
    @property
    def velocity(self):
        return (self._v_x ** 2 + self._v_y ** 2) ** 0.5
    @property
    def location(self):
        return self._loc
    @property
    def crashed(self):
        return self._crashed
    def _update_velocity(self, planet: Planet):
        dist = self._loc.distance_to(planet.origin)
        f_g = planet.gravitational_force(dist, self._m)
        # print(f"f_g = {f_g}")
        theta = math.asin(abs(self._loc.x - planet.origin.x) / dist)
        # print(f"theta = {theta}")
        a_y = f_g * math.cos(theta) / self._m * (
            1 if self._loc.y < planet.origin.y else -1
        )
        # print(f"a_y = {a_y}")
        a_x = f_g * math.sin(theta) / self._m * (
            1 if self._loc.x < planet.origin.x else -1
        )
        # print(f"a_x = {a_x}")

        self._v_x += a_x
        self._v_y += a_y
    def get_heading_change(self):
        """Returns change in heading from original heading (in degrees)"""
        return math.degrees(math.acos(self._v_y / self.velocity))
    def move(self, planet: Planet):
        """One step (1s) of simulation"""
        self._update_velocity(planet)
        self._loc.x += self._v_x
        self._loc.y += self._v_y

        self._path.append(self._loc.coordinates)

        if self._loc.in_circle(planet.radius, planet.origin):
            print(self._loc, planet.origin)
            self._crashed = True
    def __str__(self):
        return f"Spaceship(Mass={self._m}, Vy={self._v_y}, Vx={self._v_x})"
