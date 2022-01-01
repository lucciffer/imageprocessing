import os, glob 
import numpy as np 
import micasense.capture as capture

panelNames = None 

# Image from the example RedEdge imageSet (see the ImageSet notebook) without RigRelatives.
imagePath = os.path.expanduser(os.path.join('../MSI/data/micasense_datasets/Part1','000'))
imageNames = glob.glob(os.path.join(imagePath,'IMG_0016_*.tif'))  # sets to be aligned
panelNames = glob.glob(os.path.join('../MSI/data/micasense_datasets/Part1/000/IMG_0000*.tif'))  # corresponding CRP images for metadata


if panelNames is not None:
    panelCap = capture.Capture.from_filelist(panelNames)
else:
    print("No panel images found")

capture = capture.Capture.from_filelist(imageNames)


if panelCap is not None:
    panel_reflectance_by_band = panelCap.panel_albedo()
else: 
    print("check panel files")

panel_irradiance = panelCap.panel_irradiance(panel_reflectance_by_band)
print("panel reflectance: ",panel_reflectance_by_band)
print("panel irradiance: ",panel_irradiance)

panel_metadata = {'panel_reflectance' : panel_reflectance_by_band, 'panel_irradiance' : panel_irradiance}
np.save('../MSI/data_processing/calibration_matrices/panel_metadata.npy', panel_metadata)
# print(panel_metadata)

print("[INFO] Panel metadata exported...")