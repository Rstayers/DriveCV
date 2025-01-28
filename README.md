# Project Overview
This application analyzes dashcam footage to identify other vehicles, road lanes, and relevant road signs in real-time using Computer Vision algorithms and techniques. It should be able to accuractely perform in many environments and scene conditions. 

## Dataset
For this project, I am choosing to use [http://bdd-data.berkeley.edu/download.html][Berkely's DeepDrive dataset] (BDD100K). I asked Claude Sonnet to produce five of the most used and modern datasets for training computer vision applications for autonomous vehicles, and the top two were [https://www.nuscenes.org/nuscenes][NuScenes] and DeepDrive. NuScenes is a multi-modal dataset with 3D annotated bounding boxes, but lacks the amount of data that DeepDrive contains. After talking to professor Schreirer, I have chosen to go with DeepDrive as it has more documented use. 

## High-Level Structure
The basic structure of the project pipeline could be as follows: 

**Frame Preprocessing** → **Detection Module** → **Tracking Module** → **Visualization Module**

### Frame Preprocessing
The first would be standard Machine Learning practices for preprocessing and formatting data. This could be standardizes resolutions, color adjustments, noise reductions or normalizations. I took a machine learning class last semester and this was always the first step (I have not dealt with video before so I do not know how it will differ).

### Detection Module
The next step in my approach will be to develop a pipeline that will identitfy objects of interest in a given frame (cars, lanes, signs, pedestrians, etc.). This will be the bulk of the work and therefore the most important module. Here, deep machine learning techniques for classifcation can be used such as reinforcement and active learning frameworks. The model will need to identity lane boundaries by the color (white / yellow), width, and pattern of the line. To find other cars, identifying features would be wheels, rectangular objects, as well as unique aspects of vehicles like license plates. Pedestrians will probably be the trickiest thing to detect because of the variety of cases. Color is not neccessarily important because clothing comes in all colors. The most identifiable attributes would be the tall slender shape most people have compared to other objects, as well as how we move. Signs will also be tricky because while they are uniform, there are many types of signs. It might be reasonable to only identify stop signs for now. The identifiers are easy for this in the U.S, as all stop signs are red and octagonal. All of these detection types could be split into further sub modules to decouple the model. This would be especially useful for signs, as each type could be in its own sub module. Most of these objects do not require extremely high resolutions to identify, and should be considered in implementation.

### Tracking Module
The tracking module would then associate the detections across multiple frames to calculate trajectories and speeds to be passed onto the visualization. 
### Visulization Module
This is the UI of the project that shows what the model is detecting in real time on the footage.