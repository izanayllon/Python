import sys, os
sys.path.append(os.getcwd())
import entities
import pygame
import numpy as np

class Viewer(object):
    """docstring for Viewer."""

    def __init__(self, width, height, background_color=(0, 0, 0)):
        super(Viewer, self).__init__()
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        pygame.init()
        self.objects = {}

    def addObjects(self, objects):
        for obj in objects:
            self.objects[obj.name] = obj

    def run(self):
        KtF = {
            pygame.K_w: (lambda x: x.translateAll([0, -10, 0])),
            pygame.K_a: (lambda x: x.translateAll([-10, 0, 0])),
            pygame.K_s: (lambda x: x.translateAll([0, 10, 0])),
            pygame.K_d: (lambda x: x.translateAll([10, 0, 0])),
            pygame.K_INSERT: (lambda x: x.scaleAll(1.25)),
            pygame.K_DELETE: (lambda x: x.scaleAll(0.8)),
            pygame.K_q: (lambda x: x.rotate(0.1, "z")), # counterclockwise
            pygame.K_e: (lambda x: x.rotate(-0.1, "z")), # clockwise
            pygame.K_LEFT: (lambda x: x.rotate(-0.1, "y")), # clockwise
            pygame.K_RIGHT: (lambda x: x.rotate(0.1, "y")), # counterclockwise
            pygame.K_UP: (lambda x: x.rotate(-0.1, "x")), # forward
            pygame.K_DOWN: (lambda x: x.rotate(0.1, "x")) # backward
        }
        running = True
        while running:
            pressed_keys = pygame.key.get_pressed()
            for key in KtF.keys():
                if pressed_keys[key]:
                    KtF[key](self)


            running = not pressed_keys[pygame.K_ESCAPE]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.display()
            pygame.display.flip()
            pygame.time.delay(100)

        pygame.quit()

    def display(self):
        self.screen.fill(self.background_color)
        pygame.display.flip()
        for obj in self.objects.values():
            for node in obj.nodes:
                pygame.draw.circle(self.screen, obj.node_color, (int(node[0]+self.width/2), int(node[1]+self.height/2)), int(obj.node_radius/2), 0)
            for start, end in obj.edges:
                pygame.draw.line(self.screen, obj.edge_color, (obj.nodes[start][0]+self.width/2, obj.nodes[start][1]+self.height/2), (obj.nodes[end][0]+self.width/2, obj.nodes[end][1]+self.height/2), 1)

    # def display(self):
    #     self.screen.fill(self.background_color)
    #     pygame.display.flip()
    #     for obj in self.objects.values():
    #         i = 0
    #         color = (0, 255, 0)
    #         while i < 4:
    #
    #             pygame.draw.circle(self.screen, (0, 255, 0), (int(obj.nodes[i][0]+self.width/2), int(obj.nodes[i][1]+self.height/2)), obj.node_radius, 0)
    #             i += 1
    #
    #         color = (255, 255, 255)
    #         while i < len(obj.nodes):
    #             pygame.draw.circle(self.screen, color, (int(obj.nodes[i][0]+self.width/2), int(obj.nodes[i][1]+self.height/2)), int(obj.node_radius/2), 0)
    #             i += 1
    #
    #         for start, end in obj.edges:
    #             pygame.draw.line(self.screen, obj.edge_color, (obj.nodes[start][0]+self.width/2, obj.nodes[start][1]+self.height/2), (obj.nodes[end][0]+self.width/2, obj.nodes[end][1]+self.height/2), 1)

    def translateAll(self, movement):
        matrix = entities.translationMatrix(*movement)
        for obj in self.objects.values():
            obj.transform(matrix)

    def scaleAll(self, scalar):
        matrix = entities.scalingMatrix(scalar, scalar, scalar)
        for obj in self.objects.values():
            obj.transform(matrix)

    def rotate(self, radians, axis, exclude=None):
        rotateMatrix = "rotate"+axis.title()+"matrix"
        matrix = getattr(entities, rotateMatrix)(radians)
        for obj in self.objects.values():
            obj.transform(matrix)

import string
