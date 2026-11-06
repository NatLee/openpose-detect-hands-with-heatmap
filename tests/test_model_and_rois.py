import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from utils.ROIs import ROIs


def test_overlapping_regions_keep_original_intensity_and_resize():
    rois = ROIs([[(1, 1), (6, 1), (6, 6), (1, 6)],
                 [(3, 3), (8, 3), (8, 8), (3, 8)]])
    for size in (10, 20, 6):
        frame = np.full((size, size, 3), 200, np.uint8)
        result = rois.get_mask_frame(frame)
        np.testing.assert_array_equal(result[4, 4], [200, 200, 200])
        np.testing.assert_array_equal(result[0, 0], [0, 0, 0])
        assert result.shape == frame.shape


def test_point_membership_uses_any_region_and_excludes_boundaries():
    rois = ROIs([[(0, 0), (4, 0), (4, 4), (0, 4)]])
    assert rois.is_a_point_in_all_polygons((2, 2))
    assert not rois.is_a_point_in_all_polygons((0, 0))
    assert not rois.is_a_point_in_all_polygons((8, 8))


def test_network_builds_body_paf_and_heatmap_heads():
    from openpose.model import get_testing_model
    model = get_testing_model()
    assert [shape[-1] for shape in model.output_shape] == [38, 19]
