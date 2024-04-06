from build123d import *
from ocp_vscode import show


length, width, thickness = 80.0, 60.0, 30.0
center_hole_dia = 30.0

with BuildPart() as ex2:
    Box(length, width, thickness)
    Cylinder(radius=center_hole_dia / 2, height=thickness, mode=Mode.SUBTRACT)

    fillet(ex2.edges(), radius=2)
show(ex2)