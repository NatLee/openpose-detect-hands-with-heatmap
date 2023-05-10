
import cv2
from openpose import OpenposeModel
from utils import draw_heat, FPS, ROIs

from pathlib import Path

if __name__ == '__main__':
    
    om = OpenposeModel('/model/weights.h5')
    cap = cv2.VideoCapture('/data/test.mp4')

    frame_pass = 30
    offset = -5
    
    # =====================
    # ROIs
    points_for_each_polygons = [
        [(0, 0), (384, 0), (384, 216), (0, 216)]
        #[(106, 187), (256, 263), (197, 303), (63, 220)],
    ]
    rois = ROIs(points_for_each_polygons)
    # =====================

    polys = list()

    fps = FPS().start()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if fps.totalFrame() % frame_pass == 0:
                frame = cv2.resize(frame, None, fx=0.3, fy=0.3)
                frame = frame[:215, :215]
                open_pose_result = om.predict(frame, scale_search=[0.5, 1])

                if len(open_pose_result) > 0:
                    polys.append(open_pose_result)

                #get_non_zero_dots = [poly for poly in polys if len(poly) > 0]
                all_frame_points = list()
                for poly in polys:
                    for dots in poly:
                        # find max
                        point = max(dots, key=lambda point: point[1])
                        point = (point[0], point[1]+offset)
                        if rois.is_a_point_in_all_polygons(point):
                            all_frame_points.append(point)
                            
                roi = rois.get_mask_frame(frame)
                frame = cv2.addWeighted(src1=frame, alpha=0.5, src2=roi, beta=0.5, gamma=0)

                if not Path('/tmp').is_dir():
                    Path('/tmp').mkdir()
                filename = '/tmp/{}.png'.format(str(int(fps.totalFrame()/5)).zfill(5))
                cv2.imwrite(filename, frame)
                draw_heat(filename, filename, all_frame_points)

            fps.update()
        else:
            break
        '''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        '''

    cap.release()
    #cv2.destroyAllWindows()

    fps.stop()
    print("[INFO] total frames: {:.2f}".format(fps.totalFrame()))
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    get_non_zero_dots = [poly for poly in polys if len(poly)>0]
    
    all_frame_points = list()
    offset = 0
    for frame_dots in get_non_zero_dots:
        for frame_dot in frame_dots:
            point = max(frame_dot, key=lambda point: point[1])
            all_frame_points.append((point[0], point[1]+offset))

    # draw all points into first frame
    draw_heat('/tmp/00000.png', '/tmp/00000.heatmap.png', all_frame_points)

