from sklearn.neighbors import KNeighborsClassifier, KDTree
from sklearn.externals import joblib
import numpy as np
import os
import sys

def read_data(src):
    files = os.listdir(src)
    labels = []
    datas = []
    for i, file in enumerate(files):
        temp = os.path.join(src, file)        
        data = np.load(temp)        
        label = -1
        if file.find('cat') != -1:
            label = 0

        else:
            label = 1
        print("[+] Load file : ", temp , " with label : ",label, " shape : ", data.shape, " data : ", data)
        datas.append(data[0])
        labels.append(label)
    return datas, labels

if __name__ == '__main__':
    src = sys.argv[1]
    datas, labels = read_data(src)
    print("[!] Training models...")
    knn = KNeighborsClassifier(n_neighbors=7, algorithm="kd_tree").fit(datas, labels)
    print("[+] Train finished")
    save_path = "model/knn.joblib"
    print("[+] Save model to file : ", save_path)
    joblib.dump(knn, save_path)