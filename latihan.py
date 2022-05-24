import math
import rasterio
import matplotlib.pyplot as plt
image_file = "image.tif"
sat_data = rasterio.open(image_file)

with_in_projected_units = sat_data.bounds.right - sat_data.bounds.left
height_in_projected_units = sat_data.bounds.right - sat_data.bounds.bottom
print("widht: {}, Height: {}". format(width_in_projected_units, height_in_projected_units))

print("Rows: {}, Columns: {}". format(sat_data.height, sat_data.width))
print9("Rows: {}".format(sat_data.height, sat_data.width))
row = 0
col_min = 0

row_max = set_data.higth -1
col_max = set_data. width -1
topleft = sat_data. transform * (row_min, col_min)
botright = sat_data. trasform * (row_max, col_max)

print("Top left corner coordinates: {}". format(topleft))
print("Bottom right corner coordinates: {}". format(botright))
print(sat_data)

print(sat_data.indexes)

b, g, r, n = sat_data.read() 