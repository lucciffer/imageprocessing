import os
import glob
import micasense.capture as capture
import cv2
import numpy as np
import matplotlib.pyplot as plt
import micasense.imageutils as imageutils
import micasense.plotutils as plotutils


panelNames = None

imagePath = os.path.expanduser(os.path.join(
    '/home/cvg-ws05/msi_up/nikhil/MSI/data/micasense_datasets/Part1/', '000'))
imageNames = glob.glob(os.path.join(imagePath, 'IMG_0007_*.tif'))
panelNames = glob.glob(os.path.join(
    '/home/cvg-ws05/msi_up/nikhil/MSI/data/micasense_datasets/Part1/000/IMG_0000*.tif'))


if panelNames is not None:
    panelCap = capture.Capture.from_filelist(panelNames)
else:
    panelCap = None


print(imagePath)
print(imageNames)

capture = capture.Capture.from_filelist(imageNames)

if panelCap is not None:
    if panelCap.panel_albedo() is not None:
        panel_reflectance_by_band = panelCap.panel_albedo()
    else:
        panel_reflectance_by_hand = [0.67, 0.69, 0.68, 0.61, 0.67]
    panel_irradiance = panelCap.panel_irradiance(panel_reflectance_by_band)
    img_type = "reflectance"
    capture.plot_undistorted_reflectance(panel_irradiance)
else:
    if capture.dls_present():
        img_type = 'reflectance'
        capture.plot_undistorted_reflectance(capture.dls_irradiance())
    else:
        img_type = 'radiance'
        capture.plot_undistorted_radiance()


match_index = 0
max_alignment_iterations = 20
warp_mode = cv2.MOTION_HOMOGRAPHY
pyramid_levels = 1

warp_matrices, alignment_pairs = imageutils.align_capture(
    capture, ref_index=match_index, max_iterations = max_alignment_iterations, warp_mode=warp_mode, pyramid_levels=pyramid_levels)

print("Finished aligning...")