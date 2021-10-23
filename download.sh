#!/usr/bin/env bash
set -ex

unzip covid19-radiography-database.zip
unzip chest-xray-pneumonia.zip

kaggle datasets download -d tawsifurrahman/covid19-radiography-database
git clone https://github.com/ieee8023/covid-chestxray-dataset.git
kaggle datasets download -d paultimothymooney/chest-xray-pneumonia
