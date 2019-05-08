#include <cmath>
#include <iostream>
#include <fstream>
#include <ctime>
#include <vector>
#include <omp.h>
#include <opencv2/opencv.hpp>
#include <iomanip>
#include <glob.h>

using namespace std;
using namespace cv;

string path = "../../DataChallenge/train_individuals/"; 

void rescale_all_images(); 

vector<string> globVector(const string &pattern); 

void rescale_image(string path, int imageNumber); 

uint8_t rescale_pixel(int x, int minimum, int maximum); 

vector<int> histogram(Mat &img, int binSize); 