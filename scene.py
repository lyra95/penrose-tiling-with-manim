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

def nextGen(first: Union[Pentagon,None], second: Pentagon):
    g = Group().add(second.group)
    if first == None:
        for p in second.boundary.get_vertices():
            g.add(second.group.copy().rotate(ROTATION_ANGLE, about_point=p))
    else:
        for p in second.boundary.get_vertices():
            g.add(second.group.copy().rotate(ROTATION_ANGLE, about_point=p))
            g.add(first.group.copy().rotate(math.pi, about_point=p))

    return Pentagon(g,
        second.boundary.copy().rotate(math.pi, about_point=second.com).scale_about_point(SCALE, second.com))


GEN_ZERO_RADIUS = 0.2
START_ANGLE = math.pi/10.0
BOUNDARY_COLOR = "GREEN"
DEPTH = 2

class PenroseOne(Scene):
    def construct(self):
        p = RegularPolygon(5, radius=GEN_ZERO_RADIUS,
                           start_angle=START_ANGLE, color=BOUNDARY_COLOR)
        # p.set_fill(PURE_GREEN, opacity=1.0)
        first = None
        second = Pentagon(Group(p), p.copy())
        for _ in range(DEPTH):
            second, first = nextGen(first, second), second
            self.show(second)

    def show(self, gen: Pentagon):
        # self.play(FadeIn(gen.group))
        self.add(gen.group)
