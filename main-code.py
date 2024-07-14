import cv2
import imutils
import numpy as np

HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
def detectbyimage(int):

    path = "img.jpg"
    output_path ="blank.jpg"

    image = cv2.imread(path)

    image = imutils.resize(image, width = min(800, image.shape[1]))

    frame = image

    #bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride = (5, 5), padding = (9, 9), scale = 1.03)
    bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)

    person = 1
    for x,y,w,h in bounding_box_cordinates:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
        person += 1

    cv2.putText(frame, 'Status : Detecting ', (30,30), cv2.FONT_HERSHEY_TRIPLEX, 0.8, (0,0,255), 2)
    cv2.putText(frame, f"Total Persons : {person-1}", (30,60), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
# cv2.imshow(‘output’, frame)
    number_person = {person-1}

    result_image = frame

    if output_path is not None:
        cv2.imwrite(output_path, result_image)

    else:
        print("Error Encountered", 1/0)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


#code to detect by camera
def detectbycamera():
    def detect(frame):
        bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
        person = 1
        for x,y,w,h in bounding_box_cordinates:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            person += 1
    
        cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.imshow('output', frame)

        return frame

    def detectByCamera(writer):   
        video = cv2.VideoCapture(0)
        print('Detecting people...')

        while True:
            check, frame = video.read()

            frame = detect(frame)
            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()
    writer=None
    detectByCamera(writer)

def  detectbyvideo():
    video_path = "video1.mp4"
    def detect(frame):
        bounding_box_cordinates, weights =  HOGCV.detectMultiScale(frame, winStride = (4, 4), padding = (8, 8), scale = 1.03)
    
        person = 1
        for x,y,w,h in bounding_box_cordinates:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(frame, f'person {person}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 1)
            person += 1
    
        cv2.putText(frame, 'Status : Detecting ', (40,40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.putText(frame, f'Total Persons : {person-1}', (40,70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2)
        cv2.imshow('output', frame)

        return frame

    def detectByPathVideo(path, writer):

        video = cv2.VideoCapture(path)
        check, frame = video.read()
        if check == False:
            print('Video Not Found. Please Enter a Valid Path (Full path of Video Should be Provided).')
            return

        print('Detecting people...')
        while video.isOpened():
        #check is True if reading was successful 
            check, frame =  video.read()

            if check:
                frame = imutils.resize(frame , width=min(800,frame.shape[1]))
                frame = detect(frame)
            
                if writer is not None:
                    writer.write(frame)
            
                key = cv2.waitKey(2)
                if key== ord('q'):
                    break
            else:
                break
        video.release()
        cv2.destroyAllWindows()
    writer=None
    detectByPathVideo(video_path, writer)



if __name__=='__main__':  
    print("\nPress 1 to detect by image\nPress 2 to detect by camera\nPress 3 to detect by video\n")
    ch=int(input("Enter your choice:"))
    #writer=None
    print(ch)
    match ch:
        case 1:
            detectbyimage(0)

        case 2:
            detectbycamera()

        case 3:
            detectbyvideo()