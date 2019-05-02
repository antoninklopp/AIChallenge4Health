from image import Image
from import_data import RESIZE_FACTOR

def read_in():
    """
    Reads in the file from yolo and creates a set of images
    """
    list_images_out = []
    index = 0
    current_image_points = []
    with open("yolo_results.txt") as results:
        lines = results.readlines()
        for line in lines:
            try:
                i = int(line)
                if i != index:
                    print("PROBLEM")
                    raise
                    exit()
                if not current_image_points:
                    list_images_out.append(Image(index, 0, 0, 0, 0, 0))
                elif len(current_image_points) == 1:
                    spot = ((current_image_points[0][1] + current_image_points[0][2])/float(RESIZE_FACTOR), \
                        (current_image_points[0][3] + current_image_points[0][4])/float(RESIZE_FACTOR))
                    list_images_out.append(Image(index, 1, spot[0], spot[1], 0, 0))
                else:
                    # Reverse sort the mostr likely images
                    sort(current_image_points, lambda x: -x[0])
                    spot1 = ((current_image_points[0][1] + current_image_points[0][2])/float(RESIZE_FACTOR), \
                        (current_image_points[0][3] + current_image_points[0][4])/float(RESIZE_FACTOR))
                    spot2 = ((current_image_points[1][1] + current_image_points[1][2])/float(RESIZE_FACTOR), \
                        (current_image_points[1][3] + current_image_points[1][4])/float(RESIZE_FACTOR))
                    list_images_out.append(Image(index, 2, spot1[0], spot1[1], spot2[0], spot2[1]))

                index += 1
            except:
                # Real line
                percentage, left, right, top, bottom = line.split(" ")
                percentage, left, right, top, bottom = float(percentage), int(left), int(right), int(top), int(bottom)
                
                

if __name__ == "__main__":
    read_in()