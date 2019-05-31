from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from localization import localization

# this gets all the connected regions and groups them together
def cca2():
    binary_car_image, grey_car_image=localization()
    label_image = measure.label(binary_car_image)

# getting the maximum width, height and minimum width and height that a license plate can be
    plate_dimensions = (0.05*label_image.shape[0], 0.2*label_image.shape[0], 0.15*label_image.shape[1], 0.5*label_image.shape[1]) 
    min_height, max_height, min_width, max_width = plate_dimensions
#print(plate_dimensions)
    plate_objects_cordinates = []
    plate_like_objects = []
    fig, (ax1) = plt.subplots(1)
    ax1.imshow(grey_car_image, cmap="gray");

# regionprops creates a list of properties of all the labelled regions
    for region in regionprops(label_image):
        if region.area < 50:
        #if the region is so small then it's likely not a license plate
            continue
    # the bounding box coordinates
        min_row, min_col, max_row, max_col = region.bbox
        region_height = max_row - min_row
        region_width = max_col - min_col
    #print("%s %s" % (region_height, region_width))
        plate_objects_cordinates.append((min_row, min_col,max_row, max_col))
        rectBorder = patches.Rectangle((min_col, min_row), max_col-min_col, max_row-min_row, edgecolor="red", linewidth=2, fill=False)
        ax1.add_patch(rectBorder)
    # ensuring that the region identified satisfies the condition of a typical license plate
        if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height:
            plate_like_objects.append(binary_car_image[min_row:max_row, min_col:max_col])
            plate_objects_cordinates.append((min_row, min_col,max_row, max_col))
            rectBorder = patches.Rectangle((min_col, min_row), max_col-min_col, max_row-min_row, edgecolor="red", linewidth=2, fill=False)
            ax1.add_patch(rectBorder)
    # let's draw a red rectangle over those regions
    #plt.show()
    return(plate_like_objects)


