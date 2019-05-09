from src.image import Image
from src.import_data import RESIZE_FACTOR

def is_spot_possible(left, right, bottom, top):
    """
    Says if the spot is in an impossible location or impossible size
    """
    if right < 8 or bottom < 8:
        # print("IMPOSSIBLE", left, right, top, bottom)
        return False
    if left > 16 or top > 16:
        # print("IMPOSSIBLE", left, right, top, bottom)
        return False
    if abs(top - bottom) > 14 or abs(right - left) > 14:
        # print("IMPOSSIBLE", left, right, top, bottom)
        return False
    return True

def read_in():
    """
    Reads in the file from yolo and creates a set of images
    """
    list_images_out = []
    index = 0
    current_image_points = []
    with open("./darknet/output_global.txt") as results:
        lines = results.readlines()
        for line in lines:
            try:
                i = int(line)
                if i != index:
                    print("PROBLEM")
                    exit()
                if not current_image_points:
                    list_images_out.append(Image(index, 0, 0, 0, 0, 0))
                elif len(current_image_points) == 1:
                    if is_spot_possible(current_image_points[0][1]/float(RESIZE_FACTOR), \
                        current_image_points[0][2]/float(RESIZE_FACTOR), \
                        current_image_points[0][3]/float(RESIZE_FACTOR), \
                        current_image_points[0][4]/float(RESIZE_FACTOR)):
                        spot = ((current_image_points[0][1] + current_image_points[0][2])/float(2 * RESIZE_FACTOR), \
                            (current_image_points[0][3] + current_image_points[0][4])/float(2 * RESIZE_FACTOR))
                        list_images_out.append(Image(index, 1, spot[0], spot[1], 0, 0))
                    else:
                        list_images_out.append(Image(index, 0, 0, 0, 0, 0))
                else:
                    # Reverse sort the mostr likely images
                    current_image_points.sort(key=lambda x: -x[0])
                    spots = []
                    if is_spot_possible(current_image_points[0][1]/float(RESIZE_FACTOR), \
                        current_image_points[0][2]/float(RESIZE_FACTOR), \
                        current_image_points[0][3]/float(RESIZE_FACTOR), \
                        current_image_points[0][4]/float(RESIZE_FACTOR)):
                        spot1 = ((current_image_points[0][1] + current_image_points[0][2])/float(2 * RESIZE_FACTOR), \
                            (current_image_points[0][3] + current_image_points[0][4])/float(2 * RESIZE_FACTOR))
                        spots.append(spot1)
                    if is_spot_possible(current_image_points[1][1]/float(RESIZE_FACTOR), \
                        current_image_points[1][2]/float(RESIZE_FACTOR), \
                        current_image_points[1][3]/float(RESIZE_FACTOR), \
                        current_image_points[1][4]/float(RESIZE_FACTOR)):
                        spot2 = ((current_image_points[1][1] + current_image_points[1][2])/float(2 * RESIZE_FACTOR), \
                            (current_image_points[1][3] + current_image_points[1][4])/float(2 * RESIZE_FACTOR))
                        spots.append(spot2)
                    if len(spots) == 0:
                        list_images_out.append(Image(index, 0, 0, 0, 0, 0))
                    elif len(spots) == 1:
                        list_images_out.append(Image(index, 1, spots[0][0], spots[0][1], 0, 0))
                    else:
                        list_images_out.append(Image(index, 2, spot1[0], spot1[1], spot2[0], spot2[1]))

                # Reset the current image
                current_image_points = []
                index += 1
            except ValueError:
                # Real line
                left, top, right, bottom = line.split(" ")
                left, right, top, bottom = int(left), int(right), int(top), int(bottom)
                current_image_points.append([0, left, right, bottom, top])

    list_images_out.pop(0)
    return list_images_out

if __name__ == "__main__":
    for image in read_in():
        print(image)
