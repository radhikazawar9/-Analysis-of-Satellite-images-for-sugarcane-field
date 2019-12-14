#import required libraries
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
#%matplotlib inline
import os
os.listdir('C:\\Users\\radhi\\Desktop\\MyDatathon\\')
#import bands as separate 1 band raster
band4 = rasterio.open('C:\\Users\\radhi\\Desktop\\MyDatathon\\B04_tiff\\6656-7168-B04-2016-12-22.png.tiff') #red
band5 = rasterio.open('C:\\Users\\radhi\\Desktop\\MyDatathon\\B08_tiff\\6656-7168-B08-2016-12-22.png.tiff') #nir
#number of raster rows
band4.height
#number of raster columns
band4.width
#plot band
#plot.show(band4)
#type of raster byte
band4.dtypes[0]
#raster sytem of reference
band4.crs
#raster transform parameters
band4.transform
#raster values as matrix array
band4.read(1)
#multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
#plot.show(band4, ax=ax1, cmap='Blues') #red
#plot.show(band5, ax=ax2, cmap='Blues') #nir
fig.tight_layout()
fig.suptitle('Multiple band representation', fontsize = 16)
#generate nir and red objects as arrays in float64 format
red = band4.read(1).astype('float64')
nir = band5.read(1).astype('float64')

nir
#ndvi calculation, empty cells or nodata cells are reported as 0
ndvi=np.where(
    (nir+red)==0.,
    0,
    (nir-red)/(nir+red))
ndvi[:5,:5]

print ndvi[:5,:5]
#export ndvi image
ndviImage = rasterio.open('C:\\Users\\radhi\\Desktop\\MyDatathon\\NDVI ouput\\NDVI ouputndviImage.tiff','w',driver='Gtiff',
                          width=band4.width,
                          height = band4.height,
                          count=1, crs=band4.crs,
                          transform=band4.transform,
                          dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()
#plot ndvi
ndvi = rasterio.open('C:\\Users\\radhi\\Desktop\\MyDatathon\\NDVI ouput\\NDVI ouputndviImage.tiff')
fig = plt.figure(figsize=(18,12))
#plot.show(ndvi)

ndvi_class_bin = [-np.inf, 0, 0.1, 0.25, 0.4, np.inf]
ndvi_class = np.digitize(ndviImage, ndvi_class_bin)

ndvi_class = np.ma.masked_where(np.ma.getmask(ndviImage),ndvi_class)
np.unique(ndvi_class)


nbr_colours = ["gray", "y","yellowgreen","g","darkgreen"]
nbr_cmap = ListedColormap(nbr_colours)

# Define class names
ndvi_cat_names = [
    "No Vegetation",
    "Bare Area",
    "Low Vegetation",
    "Moderate Vegetation",
    "High Vegetation",
]

# Get list of classes
classes = np.unique(ndvi_class)
classes = classes.tolist()
# The mask returns a value of none in the classes. remove that
classes = classes[0:5]

# Plot your data
fig, ax = plt.subplots(figsize=(6, 6))
print fig
print ax
im = ax.imshow(ndvi_class, cmap=nbr_cmap)

plt.tight_layout()
