import pymunk
from numpy import pi


# print(tor1, tor2)
space = pymunk.Space()
space.gravity = float(0), float(0)

ground = pymunk.Body(body_type = pymunk.Body.STATIC)
ground.position = (float(320), float(-5))
polyG =pymunk.Poly.create_box(ground,  size=(float(640), float(10)))

rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC)
rotation_center_body.position = (float(320), float(285.84))

poly = pymunk.Poly.create_box(None, size=(float(10), float(200)))
moment = pymunk.moment_for_poly(float(1), poly.get_vertices())
body = pymunk.Body(float(1),float(moment))
poly.body = body
body.position = float(249.29), float(215.13)
body.angle = float(-(45 * pi /180))

poly2 = pymunk.Poly.create_box(None, size=(float(10), float(200)))
moment2 = pymunk.moment_for_poly(float(1), poly2.get_vertices())
body2 = pymunk.Body(float(1),float(moment2))
poly2.body = body2
body2.position = float(249.29), float(73.71)
body2.angle = float(45 * pi / 180)

rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (float(0),float(100)), (float(0),float(0)))
rotation_center_joint2 = pymunk.PinJoint(body, body2, (float(0),float(-100)), (float(0),float(105)))

space.add(body,body2, poly, poly2, rotation_center_joint, rotation_center_joint2)

def reset():
    body.angle = float(-(45 * pi / 180))
    body2.angle =float(45 * pi / 180)
    space.step(0.01)


def Update(tor1, tor2):
    tor1 = tor1 * 100000
    tor2 = tor2 * 100000
    # if tor1 > 100000000:
    #     tor1 = 100000000
    # if tor2 > 100000000:
    #     tor2 = 100000000
    # print("tor", tor1, tor2)

    body.torque = float(tor1)
    body2.torque = float(tor2)
    space.step(0.01)
    # print(body.angle, body2.angle)
    return body.angle, body2.angle






