# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:05:22 2019

@author: Rohit Soni
"""

import os
import cv2

def convert_frames_to_video(input_list,output_file_name,fps,size):
    
    # Define the output video writer object 
    out = cv2.VideoWriter(output_file_name, fourcc, fps, size)
    num_frames = len(input_list)

    for i in range(num_frames):
        base_name='Outframe'
        img_name = base_name + '{:d}'.format(i) + '.jpg.jpg'
        img_path = os.path.join(input_frame_path,img_name)
        
        try:
            img = cv2.imread(img_path)
            out.write(img) # Write out frame to video
        except:
            print(img_name + ' does not exist')
        
        if img is not None:
            cv2.imshow('img',img)
            cv2.waitKey(1)
    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
    print("The output video is {} is saved".format(output_file_name))

if __name__=='__main__':
    
    path = os.getcwd()
    data_dir='Output'
    #data_subdir = 'clip1'
    output_vid_dir = 'output_video_2'

    if not os.path.exists(output_vid_dir):
        os.mkdir(output_vid_dir)
        
    data_dir_list = os.listdir(os.path.join(path,data_dir))
    
    # Loop over all the folder in the data dir list and convert the frames in 
    # each folder to a video file
    
    for data_subdir in data_dir_list:
        
        #print ('Reading the subdir: {}'.format(data_subdir))
        #PATH = os.getcwd()
        input_frame_path = os.path.join(path,data_dir)
    
        img_list = os.listdir(input_frame_path)
    #    img_list = glob.glob(input_frame_path+'/*.png')
        #num_frames = 5400.
        frame = cv2.imread(os.path.join(input_frame_path,'Outframe0.jpg.jpg'))
        height, width, channels = frame.shape
        fps = 15
        output_file_name = 'clip2.mp4'.format(data_subdir,fps)
        # Define the codec.FourCC is a 4-byte code used to specify the video codec
        fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
        size = (width,height)
convert_frames_to_video(img_list,output_file_name,fps,size)
        