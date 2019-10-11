import cv2
vidcap=cv2.VideoCapture("clip1.mp4")
success,image=vidcap.read()
count=0 
success=True
while success:
	cv2.imwrite("frame%d.jpg"%count,image)    #save frame as jpeg
	success,image=vidcap.read()
	success=True
	print('Read a new frame:',success)
	count+=1