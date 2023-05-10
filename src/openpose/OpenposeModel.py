import time
import cv2
from .prediction import process, draw_poly, model_predict
from .model import get_testing_model

class OpenposeModel():

    def __init__(self, weights):
        self.model = get_testing_model()
        self.model.load_weights(weights)

    def predict(self, input_image, scale_search=[0.5, 1, 1.5, 2]):
        tic = time.time()
        heatmap_avg, paf_avg = model_predict(input_image, self.model, scale_search=scale_search)
        subset, candidate = process(heatmap_avg, paf_avg)
        _, polygons = draw_poly(input_image, subset, candidate)
        toc = time.time()
        print('[INFO] processing time is %.5f' % (toc - tic))
        return polygons