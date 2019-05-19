from src.image import Image
from src.import_data import RESIZE_FACTOR

def is_spot_possible(left, right, bottom, top):
    """
    Says if the spot is in an impossible location or impossible size
    """
    return True
    if right < 6 or bottom < 6:
        # print("IMPOSSIBLE", left, right, top, bottom)
        return False
    if left > 18 or top > 18:
        # print("IMPOSSIBLE", left, right, top, bottom)
        return False
    if abs(top - bottom) > 16 or abs(right - left) > 16:
        # print("IMPOSSIBLE", left, right, top, bottom)
        return False
    return True

def parse_current_images(current_image_points, index):
    if not current_image_points:
        image_out = Image(index - 1, 0, 0, 0, 0, 0)
    elif len(current_image_points) == 1:
        if is_spot_possible(current_image_points[0][1]/float(RESIZE_FACTOR), \
            current_image_points[0][2]/float(RESIZE_FACTOR), \
            current_image_points[0][3]/float(RESIZE_FACTOR), \
            current_image_points[0][4]/float(RESIZE_FACTOR)):
            spot = ((current_image_points[0][1] + current_image_points[0][2])/float(2 * RESIZE_FACTOR), \
                (current_image_points[0][3] + current_image_points[0][4])/float(2 * RESIZE_FACTOR))
            image_out = Image(index - 1, 1, spot[0], spot[1], 0, 0)
        else:
            image_out = Image(index - 1, 0, 0, 0, 0, 0)
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
            image_out = Image(index - 1, 0, 0, 0, 0, 0)
        elif len(spots) == 1:
            image_out = Image(index - 1, 1, spots[0][0], spots[0][1], 0, 0)
        else:
            image_out = Image(index - 1, 2, spot1[0], spot1[1], spot2[0], spot2[1])
    
    return image_out

def read_in():
    """
    Reads in the file from yolo and creates a set of images
    """
    list_images_out = []
    index = 0
    current_image_points = []
    with open("./darknet/output.txt") as results:
        lines = results.readlines()
        for line in lines:
            try:
                i = int(line[-(4+6+1):][:6]) # ex of file 000000.jpg 6 + 4 characters
                if i != index:
                    print("PROBLEM")
                    print(i, index)
                    exit()
                
                list_images_out.append(parse_current_images(current_image_points, index))
                # Reset the current image
                current_image_points = []
                index += 1
            except ValueError:
                # Real line
                left, top, right, bottom = line.split(" ")
                left, right, top, bottom = int(left), int(right), int(top), int(bottom)
                current_image_points.append([0, left, right, bottom, top])

        list_images_out.append(parse_current_images(current_image_points, index))

    # We remove the first image due to line 36 test
    list_images_out.pop(0)
    print(len(list_images_out))
    return list_images_out

if __name__ == "__main__":
    for image in read_in():
        print(image)
