import cv2
import weave
import numpy as np
import matplotlib.pyplot as plt
 
img = cv2.imread("orginal_sjencenje_50.jpg",cv2.IMREAD_GRAYSCALE)
height, width = img.shape
 
def usporedjivanje(IN,width,height,OUT):
  code = """
 int i, j;
   for ( i=2; i<height-2; i++ ) {
       for( j=2; j<width-2; j++ ) {
           if ( IN [(i-1) * width + j-1] >= IN [i * width + j] ) OUT[(i-1) * width + j-1] += 128;
           if ( IN [(i-1) * width + j] >= IN [i * width + j] )   OUT[(i-1) * width + j-1] += 64;
           if ( IN [(i-1) * width + j+1] >= IN [i * width + j] ) OUT[(i-1) * width + j-1] += 32;
           if ( IN [(i) * width + j+1] >= IN [i * width + j] )   OUT[(i-1) * width + j-1] += 16;
           if ( IN [(i+1) * width + j+1] >= IN [i * width + j] ) OUT[(i-1) * width + j-1] += 8;
           if ( IN [(i+1) * width + j] >= IN [i * width + j] )   OUT[(i-1) * width + j-1] += 4;
           if ( IN [(i+1) * width + j-1] >= IN [i * width + j] ) OUT[(i-1) * width + j-1] += 2;
           if ( IN [(i) * width + j-1] >= IN [i * width + j] )   OUT[(i-1) * width + j-1] += 1;
          }
    }
 
"""
  weave.inline(code,['IN','width','height','OUT'])
 
def ovoradi(image):
    output = np.zeros( (image.shape[0],image.shape[1]) )
    usporedjivanje(img,width,height,output)
    output = output.astype(np.uint8)
    return output

def showhist(img):
  hist,bins = np.histogram(img.flatten(), bins=256, range=(0,255))
  plt.vlines(np.arange(len(hist)), 0, hist)
  plt.title("Histogram")
  plt.show()
 
def show(img, title="title"):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
show(img, "Originalna slika")
nestodobro = ovoradi(img)
show(nestodobro, "LBP slika")
showhist(nestodobro)
 	