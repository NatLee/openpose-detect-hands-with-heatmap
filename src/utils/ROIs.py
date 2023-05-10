import numpy as np
import cv2
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class ROIs():

    def __init__(self, points_for_each_polygons: list):
        self.points_for_each_polygons = points_for_each_polygons
        self.polygons = list()
        for points_in_a_polygon in self.points_for_each_polygons:
            self.polygons.append(Polygon(points_in_a_polygon))

        self.region_masks = list()
        self.GET_MASK = False

    def get_mask_frame(self, frame):

        if not self.GET_MASK:
            #show_image_masks = list()
            for points_in_a_polygon in self.points_for_each_polygons:
                roi_points = np.array(points_in_a_polygon, np.int32).reshape((-1, 1, 2))
                mask = cv2.polylines(np.zeros(frame.shape, np.uint8), [roi_points], True, (255, 255, 255), 2)
                self.region_masks.append(cv2.fillPoly(mask.copy(), [roi_points], (255, 255, 255)))
                #show_image_masks.append(cv2.fillPoly(mask.copy(), [roi_points], (0, 255, 0)))
            self.GET_MASK = True

        roi = np.zeros(frame.shape, np.uint8)
        for region_mask in self.region_masks:
            roi = roi + cv2.bitwise_and(frame, region_mask)
        return roi

    def is_a_point_in_all_polygons(self, point: tuple) -> bool:
        for polygon in self.polygons:
            if polygon.contains(Point(point)):
                return True
        return False
