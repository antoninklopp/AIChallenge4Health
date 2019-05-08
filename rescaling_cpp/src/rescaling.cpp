#include "rescaling.h"

vector<int> histogram(Mat &img, int binSize)
{
    vector<int> hist(255 / binSize + 1);
    for (int i = 0; i < img.rows; i++)
    {
        for (int j = 0; j < img.cols; j++)
        {
            hist[(int)(img.at<double>(i, j) / binSize)]++;
        }
    }
    return hist;
}

double rescale_pixel(double x, int minimum, int maximum)
{
    int newValue = (int)((x - minimum) / (float)(maximum - minimum) * 255);
    if (newValue < 0)
    {
        newValue = 0;
    }
    if (newValue > 255)
    {
        newValue = 255;
    }
    return (double)newValue;
}

void rescale_image(string pathImage, int imageNumber)
{
    int RESIZE_FACTOR = 5;
    Mat img = imread(pathImage, IMREAD_GRAYSCALE);
    img.convertTo(img, CV_64FC1);
    int BIN_SIZE = 10;
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

    for (int i = 0; i < img.rows; i++)
    {
        for (int j = 0; j < img.cols; j++)
        {
            img.at<double>(i, j) = rescale_pixel(img.at<double>(i, j), minimum,
                                                  maximum);
        }
    }

    cerr << "minimum " << minimum << " maxmimum " << maximum << endl; 

    Size rescaledSize(img.rows * RESIZE_FACTOR, img.cols * RESIZE_FACTOR);
    Mat dest(rescaledSize, CV_8UC1);
    std::stringstream buffer;
    buffer << setfill('0') << setw(6) << imageNumber;
    string destName = path + buffer.str();
    cv::resize(img, dest, rescaledSize, INTER_CUBIC);
    cv::imwrite(destName + "_rescaled.jpg", dest);
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

void rescale_all_images()
{
    vector<string> files = globVector(path + "*.jpg");
    cerr << path + "*.jpg" << endl; 
    int f = 0; 
    // #pragma omp for private(f)
    for (f = 0; f < files.size(); f++)
    {
        if (f > 10){
            break; 
        }
        cerr << f << "\n"; 
        rescale_image(files[f], f); 
    }

}

int main(){
    rescale_all_images(); 
}