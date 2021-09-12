from manim import *
import math
from typing import *

# class Crown:
#     x

# class Star:


ROTATION_ANGLE = 3.0*math.pi/5.0
golden = (1 + 5 ** 0.5) / 2
SCALE = 2.0 + 1.0/golden

class Pentagon:
    group: Group
    boundary: RegularPolygon
    com: Sequence[float]

    def __init__(self, group, boundary: RegularPolygon):
        self.group = group
        self.boundary = boundary
        self.com = boundary.get_center_of_mass()

    def nextGen(self):
        g = Group().add(self.group)
        for p in self.boundary.get_vertices():
            g.add(self.group.copy().rotate(ROTATION_ANGLE, about_point=p))
        self.group = g
        self.boundary.rotate(
            math.pi, about_point=self.com).scale_about_point(SCALE, self.com)


GEN_ZERO_RADIUS = 0.125
START_ANGLE = math.pi/10.0
BOUNDARY_COLOR = "GREEN"
DEPTH = 3

class PenroseOne(Scene):
    def construct(self):
        p = RegularPolygon(5, radius=GEN_ZERO_RADIUS,
                           start_angle=START_ANGLE, color=BOUNDARY_COLOR)
        # p.set_fill(PURE_GREEN, opacity=1.0)
        gen = Pentagon(Group(p), p.copy())
        for _ in range(DEPTH):
            gen.nextGen()
            self.show(gen)

    def show(self, gen: Pentagon):
        # self.play(FadeIn(gen.group))
        self.add(gen.group)
