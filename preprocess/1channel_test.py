import numpy as np
import cv2

test_features = []
data = []
labels = []
for i in range(len(l_test)):
  file_name,label = l_test[i]
  img = cv2.imread(file_name)
  try:
    img = cv2.resize(img,(224,224),interpolation = cv2.INTER_CUBIC)

    img = img.astype('float32')/255.0

    data.append(img[:,:,2])

    labels.append(label)
  except:
    print(file_name,i)  
 
  
test_data = np.array(data)
print(test_data.shape)


test_labels = np.array(labels)
print(test_labels.shape)    

print('^_^-testing data finished-^_^')
