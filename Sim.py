import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
from numpy import pi

window = pyglet.window.Window(640 ,480, "Test", resizable=False)
options = DrawOptions()

space = pymunk.Space()
space.gravity = 0, 0

ground = pymunk.Body(body_type = pymunk.Body.STATIC)
ground.position = (320, -5)
polyG =pymunk.Poly.create_box(ground,  size=(640, 10))

rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC)
rotation_center_body.position = (320, 285.84)

poly = pymunk.Poly.create_box(None, size=(10, 200))
moment = pymunk.moment_for_poly(1, poly.get_vertices())
body = pymunk.Body(1,moment)
poly.body = body
body.position = 249.29, 215.13
body.angle = -(45 * pi /180)

poly2 = pymunk.Poly.create_box(None, size=(10, 200))
moment2 = pymunk.moment_for_poly(1, poly2.get_vertices())
body2 = pymunk.Body(1,moment2)
poly2.body = body2
body2.position = 249.29, 73.71
body2.angle = (45 * pi / 180)

rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0,100), (0,0))
rotation_center_joint2 = pymunk.PinJoint(body, body2, (0,-100), (0,105))

space.add(body,body2, poly, poly2, rotation_center_joint, rotation_center_joint2)

@window.event
def on_draw():
    window.clear()
    space.debug_draw(options)

def update(dt):
    body.torque = 100000
    body2.torque = -100000
    space.step(dt)
    print(body.angle * 180 / 3.14, body2.angle * 180 / 3.14)
if __name__ =="__main__":
    pyglet.clock.schedule_interval(update, 1.0/60)
    pyglet.app.run()


