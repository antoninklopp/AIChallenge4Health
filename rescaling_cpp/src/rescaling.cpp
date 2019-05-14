#include "rescaling.h"

vector<int> histogram(Mat &img, int binSize)
{
    vector<int> hist(255 / binSize + 1);
    for (int i = 0; i < img.rows; i++)
    {
        for (int j = 0; j < img.cols; j++)
        {
            hist[(int)(img.at<double>(i, j) / binSize) + 1]++;
        }
    }
    return hist;
}

double rescale_pixel(double x, int minimum, int maximum)
{
    double newValue = (int)((float)(x - minimum) / (float)(maximum - minimum) * 255);
    if (newValue < 0)
    {
        newValue = 0;
    }
    if (newValue > 255)
    {
        newValue = 255;
    }
    return newValue;
}

double findMinimum(Mat &img){
    double minimum = 255; 
    for (int i = 0; i < img.rows; i++)
    {
        for (int j = 0; j < img.cols; j++)
        {
            if (img.at<double>(i, j) < minimum){
                minimum = img.at<double>(i, j); 
            }
        }
    }
    return minimum;
}

void rescale_image(string pathImage, int imageNumber, string pathDirectory)
{
    int RESIZE_FACTOR = 5;
    Mat img = imread(pathImage, IMREAD_GRAYSCALE);
    img.convertTo(img, CV_64FC1);
    int BIN_SIZE = 5;
    int MULTIPLE = 3;
    int CHANNELS = 1;

    vector<int> hist = histogram(img, BIN_SIZE);

    // First find min and max of the images
    int minimum = 0;
    int maximum = 255;

    // Min
    for (int i = 0; i < hist.size(); i++)
    {  
        if (hist[i] > 10 * CHANNELS)
        {
            minimum = i * BIN_SIZE;
            break;
        }
    }

    // Max
    for (int i = hist.size() - 1; i >= 0; i--)
    {
        if (hist[i] > 10 * CHANNELS)
        {
            maximum = (i * BIN_SIZE);
            break;
        }
    }

    // We rescale this value because some time it is too high
    maximum = min(maximum, 80);
    minimum = min(minimum, maximum); 

    for (int i = 0; i < img.rows; i++)
    {
        for (int j = 0; j < img.cols; j++)
        {
            img.at<double>(i, j) = rescale_pixel(img.at<double>(i, j), minimum,
                                                  maximum);
        }
    }

    cerr << "minimum " << minimum << " maxmimum " << maximum << endl; 
    assert (findMinimum(img) < 1); 
    assert (findMinimum(img) >= 0); 

    Size rescaledSize(img.rows * RESIZE_FACTOR, img.cols * RESIZE_FACTOR);
    Mat dest(rescaledSize, CV_8UC1);
    std::stringstream buffer;
    buffer << setfill('0') << setw(6) << imageNumber;
    string destName = pathDirectory + buffer.str();
    cv::resize(img, dest, rescaledSize, INTER_LINEAR);
    cv::imwrite(destName + ".jpg", dest);
}

vector<string> globVector(const string &pattern)
{
    glob_t glob_result;
    glob(pattern.c_str(), GLOB_TILDE, NULL, &glob_result);
    vector<string> files;
    for (unsigned int i = 0; i < glob_result.gl_pathc; ++i)
    {
        files.push_back(string(glob_result.gl_pathv[i]));
    }
    globfree(&glob_result);
    return files;
}

void rescale_all_images(string pathDirectory)
{
    vector<string> files = globVector(pathDirectory + "*.jpg");
    cerr << pathDirectory + "*.jpg" << endl; 
    int f = 0; 
    // #pragma omp for private(f)
    for (f = 0; f < files.size(); f++)
    {
        cerr << f << "\n"; 
        rescale_image(files[f], f, pathDirectory); 
    }

}

int main(){
    rescale_all_images(path); 
    rescale_all_images("../../DataChallenge/train_individuals_test/"); 
}