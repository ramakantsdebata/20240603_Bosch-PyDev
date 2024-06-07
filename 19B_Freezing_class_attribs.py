import attr

@attr.s(frozen=True)
class Point:
    x = attr.ib()
    y = attr.ib()

point = Point(1, 2)

try:
    point.x = 10
except attr.exceptions.FrozenInstanceError as e:
    print("Exception:", e.msg)
