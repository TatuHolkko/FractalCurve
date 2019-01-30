import pygame
from CoordinateSpace import Coordinatespace
from CoordinateSpaceStack import CSStack


class Graphics:
    """
    Class for drawing
    """
    def __init__(self, root, surface, origin=(0, 0)):
        """
        Initialize graphics
        :param root: first shape to draw
        :param surface: pygame surface object to draw on
        :param origin: (x, y) position of the root. default: (0, 0), top left corner
        """
        self.surf = surface
        self.root = root
        self.cs = Coordinatespace(0, 1, origin)
        self.csstack = CSStack(self.cs)

    def redraw(self, stage):
        """
        Clear surface and redraw fractal
        :param stage: stage of the fractal
        """
        self.draw_bg()
        self.root.draw(stage, self)
        self.csstack.pop()

    def draw_bg(self):
        """
        Clear screen and draw origin
        """
        self.surf.fill((0, 0, 0))
        self.draw_origin()

    def draw_origin(self):
        """
        Draw a 20 by 20 red cross in the origin
        """
        self.draw_line((0, 10), (0,-10), (255, 0, 0))
        self.draw_line((10, 0), (-10, 0), (255, 0, 0))

    def draw_line(self, pos1, pos2, color=(0, 255, 255)):
        """
        Draw a line using local coordinate system by converting pos1 and pos2 into global coordinates
        :param pos1: local point
        :param pos2: local point
        :param color: line color
        """
        global_pos1 = self.cs.get_global_pos(pos1)
        global_pos2 = self.cs.get_global_pos(pos2)
        pygame.draw.line(self.surf,
                         color,
                         (global_pos1[0], global_pos1[1]),
                         (global_pos2[0], global_pos2[1]),
                         1)
