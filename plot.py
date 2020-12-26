import pygame as pg
import pygame.locals as pgl
import math as m
import OpenGL.GL as gl
import OpenGL.GLU as glu

class Scatter:

    def __init__(self, data, color):
        self.opd = data
        self.cpd = data
        self.col = color

    def norm(self, ndata):
        self.cpd = []
        for point in self.opd:
            self.cpd.append([point[0] + ndata[0], point[1] + ndata[1], point[2] + ndata[2]])

    def render(self):
        gl.glBegin(gl.GL_POINTS)
        gl.glColor3f(self.col[0] / 255, self.col[1] / 255, self.col[2] / 255)
        for point in self.cpd:
            gl.glVertex3fv(point)
        gl.glEnd()

class Plot:

    def __init__(self, data, color):
        self.opd = data
        self.cpd = data
        self.col = color

    def norm(self, ndata):
        self.cpd = []
        for point in self.opd:
            self.cpd.append([point[0] + ndata[0], point[1] + ndata[1], point[2] + ndata[2]])

    def render(self):
        gl.glBegin(gl.GL_LINES)
        gl.glColor3f(self.col[0] / 255, self.col[1] / 255, self.col[2] / 255)
        for n in range(1, len(self.cpd)):
            gl.glVertex3fv(self.cpd[n - 1])
            gl.glVertex3fv(self.cpd[n])
        gl.glEnd()

class Figure:

    def __init__(self, ww, wh, color, mode = 0):
        self.display = (ww, wh)
        self.plots = []
        self.col = color
        self.mode = mode

    def grid(self):
        lx = 0; ly = 0; lz = 0
        hx = 0; hy = 0; hz = 0
        edges = (
            (0,1), (0,3),
            (0,4), (2,1),
            (2,3), (2,7),
            (6,3), (6,4),
            (6,7), (5,1),
            (5,4), (5,7)
        )

        bound = []
        for plot in self.plots:
            bound += plot.opd

        lx = min(bound, key = lambda x: x[0])[0] - 0.1
        ly = min(bound, key = lambda y: y[1])[1] - 0.1
        lz = min(bound, key = lambda z: z[2])[2] - 0.1
        hx = max(bound, key = lambda x: x[0])[0] + 0.1
        hy = max(bound, key = lambda y: y[1])[1] + 0.1
        hz = max(bound, key = lambda z: z[2])[2] + 0.1

        cx = (hx + lx) / 2; cy = (hy + ly) / 2; cz = (hz + lz) /2
        lx -= cx; ly -= cy; lz -= cz; hx -= cx; hy -= cy; hz -= cz


        vertices= (
            (hx, ly, lz), (hx, hy, lz),
            (lx, hy, lz), (lx, ly, lz),
            (hx, ly, hz), (hx, hy, hz),
            (lx, ly, hz), (lx, hy, hz)
        )

        gl.glBegin(gl.GL_LINES)
        gl.glColor3f(self.col[0] / 255, self.col[1] / 255, self.col[2] / 255)
        for edge in edges:
            for vertex in edge:
                gl.glVertex3fv(vertices[vertex])
        gl.glEnd()

        return (-cx, -cy, -cz)

    def rotate(self, rot = (0.0, 0.0, 0.0)):
        gl.glRotate(rot[0], 1, 0, 0)
        gl.glRotate(rot[1], 0, 1, 0)
        gl.glRotate(rot[2], 0, 0, 1)

    def show(self):
        pg.init()
        pg.display.set_mode(self.display, pgl.DOUBLEBUF | pgl.OPENGL)
        if self.mode == 0:
            bound = []
            for plot in self.plots:
                bound += plot.cpd
            lbx = min(bound, key = lambda x: x[0])[0] - 0.5
            lby = min(bound, key = lambda y: y[1])[1] - 0.5
            hbx = max(bound, key = lambda x: x[0])[0] + 0.5
            hby = max(bound, key = lambda y: y[1])[1] + 0.5
            cbx = (hbx + lbx) / 2; cby = (hby + lby) / 2
            lbx -= cbx; lby -= cby; hbx -= cbx; hby -= cby
            gl.glOrtho((3/2)*lbx, (3/2)*hbx, (3/2)*lby, (3/2)*hby, -100, 100)
        elif self.mode == 1:
            glu.gluPerspective(40, (self.display[0]/self.display[1]), 0, 100)

        self.ocpos = [0.0, 0.0, -5.0]
        self.ocrot = [0.0, 0.0, 0.0]
        self.cpos = self.ocpos
        self.crot = self.ocrot

        gl.glTranslatef(self.ocpos[0], self.ocpos[1], self.ocpos[2])
        self.rotate(self.ocrot)
        rdrag = False
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

                elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        rdrag = True
                        rx, ry = event.pos

                elif event.type == pg.MOUSEBUTTONUP:
                    if event.button == 1:
                        rdrag = False

                elif event.type == pg.MOUSEMOTION:
                    if rdrag:
                        nx, ny = event.pos
                        dx, dy = (nx - rx, ny - ry)
                        self.crot[1] += dx/250

                        a, b, c = self.crot
                        self.rotate((0, dx/250, 0))

                        cz = m.sin(m.radians(b)) * (dy/250)
                        cx = m.cos(m.radians(b)) * (dy/250)
                        self.rotate((cx, 0, cz))
                        self.crot = [a + cx, b, c + cz]

            gl.glClear(gl.GL_COLOR_BUFFER_BIT|gl.GL_DEPTH_BUFFER_BIT)
            gl.glPointSize(9.0)
            ndata = self.grid()
            for plot in self.plots:
                plot.norm(ndata)
                plot.render()
            pg.display.flip()
            pg.time.wait(10)

    def scatter(self, data, color):
        self.plots.append(Scatter(data, color))
        return self.plots[len(self.plots) - 1]

    def plot(self, data, color):
        self.plots.append(Plot(data, color))
        return self.plots[len(self.plots) - 1]
