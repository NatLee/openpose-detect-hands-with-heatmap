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

        self._mask = None

    def get_mask_frame(self, frame):
        if self._mask is None or self._mask.shape != frame.shape[:2]:
            self._mask = np.zeros(frame.shape[:2], np.uint8)
            for points in self.points_for_each_polygons:
                roi_points = np.array(points, np.int32).reshape((-1, 1, 2))
                cv2.fillPoly(self._mask, [roi_points], 255)
        return cv2.bitwise_and(frame, frame, mask=self._mask)

    def is_a_point_in_all_polygons(self, point: tuple) -> bool:
        for polygon in self.polygons:
            if polygon.contains(Point(point)):
                return True
        return False
