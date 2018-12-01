#encoding=utf-8
import cv2
import os

def getFrame(videofile,frmNum = 36 ,imageInPath="",imageBasePath = "image",idLen = 10):
    # check param
    if imageInPath == "":
        imageInPath = os.path.splitext(os.path.basename(videofile))[0]
    imageInPath = imageBasePath + '/'+imageInPath
    # make img dir
    if not os.path.isdir(imageBasePath):
        os.mkdir(imageBasePath)
    if not os.path.isdir(imageInPath):
        os.mkdir(imageInPath)
    # open video
    vdc = cv2.VideoCapture(videofile)
    # calc frame
    frn = int(vdc.get(cv2.CAP_PROP_FRAME_COUNT))
    fspace = frn / frmNum
    frmp = fspace/2
    for i in range(frmp,frn,fspace):
        # seek
        vdc.set(cv2.CAP_PROP_POS_FRAMES,i)
        # read
        rval , frame = vdc.read()
        if not rval:
            break
        # save
        cv2.imwrite( os.path.join(imageInPath,str(i).zfill(idLen) + '.jpg'),frame) 
    vdc.release()
if __name__ == "__main__":
    getFrame("c1p.mp4")
