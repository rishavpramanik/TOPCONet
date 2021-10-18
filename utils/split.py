
import os
import glob
import random

normal_dir = "appropiate path"
dir1 = os.path.join(normal_dir,"*.png")
dir2 = os.path.join(normal_dir,"*.jpeg")
dir = os.path.join(normal_dir,"*.jpg")
normal_files = glob.glob(dir)
normal_1 = glob.glob(dir1)
normal_2 = glob.glob(dir2)
normal_files.extend(normal_1)
normal_files.extend(normal_2)

normal_dir = "appropiate path"
dir1 = os.path.join(normal_dir,"*.png")
dir2 = os.path.join(normal_dir,"*.jpeg")
dir = os.path.join(normal_dir,"*.jpg")
pneumonia_files = glob.glob(dir)
pneumonia_1 = glob.glob(dir1)
pneumonia_2 = glob.glob(dir2)
pneumonia_files.extend(pneumonia_1)
pneumonia_files.extend(pneumonia_2)

normal_dir = "appropiate path"
dir1 = os.path.join(normal_dir,"*.png")
dir = os.path.join(normal_dir,"*.jpg")
dir2 = os.path.join(normal_dir,"*.jpeg")
covid_files = glob.glob(dir)
covid_files2 = glob.glob(dir2)
covid_files1 = glob.glob(dir1)
covid_files.extend(covid_files2)
covid_files.extend(covid_files1)

random.shuffle(covid_files)
random.shuffle(pneumonia_files)
random.shuffle(normal_files)
