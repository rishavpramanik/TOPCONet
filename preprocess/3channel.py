import cv2
import numpy as np

covid_dic_list = {}
data = []
labels = []
for i in range(len(l)):
  file_name,label = l[i]
  img = cv2.imread(file_name)
  try:
    img = cv2.resize(img,(224,224),interpolation = cv2.INTER_CUBIC)
    height, width = img.shape[:2]
    img = img.astype('float32')/255.0
    data.append(img)

    labels.append(label)

  except:
    print(i,file_name)
    print("Not possible")  
  
       
train_data = np.array(data)
print(train_data.shape)


train_labels = np.array(labels)
print(train_labels.shape)    

print('^_^-training data finished-^_^')
