#!/bin/python

from pyglet.gl import *
window_width = 1280 
window_height = 720
min_window_width, min_window_height = int(window_width/2), int(window_height/2)

class Triangle:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list(3, ('v3f', [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.0,0.5,0.0]),
                                                        ('c3B', [100,200,220, 200,110,100, 100,250,100]))

class Quad:
    def __init__(self):
        self.vertices = pyglet.graphics.vertex_list_indexed(4, [0,1,2, 2,3,0], 
                                                            ('v3f', [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]),
                                                            ('c3f', [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 0.0,0.0,0.0]))



class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_minimum_size(min_window_width,min_window_height)
        self.set_maximum_size(window_width,window_height)
        glClearColor(0, 0, 0, 1.0)

        self.triangle = Triangle()
        self.quad = Quad()

    def on_draw(self):
        self.clear()
        #self.triangle.vertices.draw(GL_TRIANGLES)
        self.quad.vertices.draw(GL_TRIANGLES)

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)


if __name__ == "__main__":
    window = Window(window_width, window_height, "ReCreation", resizable=False, vsync=True)
    pyglet.app.run()