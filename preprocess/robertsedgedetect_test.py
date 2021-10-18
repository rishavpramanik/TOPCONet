import cv2
from skimage.filters import roberts
import numpy as np


test_text = []
data = []
normal = []
test3 = []
labels = []
for i in range(len(l_test)):
    file_name,label = l_test[i]

    img = cv2.imread(file_name)
    img0 = cv2.imread(file_name,0)
    
    try:

        img0 = np.asarray(img0)
        arr_1 = np.asarray(img) 
        edge_roberts = roberts(img0)

        arr_img = cv2.resize(arr_1,(224,224),interpolation = cv2.INTER_CUBIC)
        r_img = cv2.resize(edge_roberts,(224,224),interpolation = cv2.INTER_CUBIC)

        arr_2 = np.expand_dims(r_img,axis = -1)


        img2 = np.concatenate((arr_img,arr_2),axis = -1)
     
        img2 = img2.astype('float32')/255.0
        test_text.append(img2)


        labels.append(label)

    except:
        print(i,file_name)
        print("Not possible")  
  
       

test_roberts_text = np.array(test_text)
print(test_roberts_text.shape)

test_labels = np.array(labels)
print(test_labels.shape)   

print('^_^-testing data finished-^_^')
