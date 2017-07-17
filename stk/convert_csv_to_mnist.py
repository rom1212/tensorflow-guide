import numpy as np


def read_data(csv_filename):
    csv = np.genfromtxt(csv_filename, delimiter=",")
    print csv.dtype
    print csv.shape
    
    # useful data, remove the header, and the first column
    data = csv[1:,1:]
    return data


def create_images_labels(data, day_len):
    num_samples = data.shape[0] - day_len  # need one more sample for label.
    # contrib/learn/python/learn/datasets/mnist.py. images are is unint8, 
    images = np.arange(0, dtype=np.float64)
    labels = np.arange(0, dtype=np.uint8)
    for i in xrange(num_samples):
        sample = data[i:i+day_len,:]
	close_delta = data[i+day_len, 3] - data[i+day_len-1, 3]
	label = 1 if close_delta > 0 else 0
	images = np.append(images, sample)
	labels = np.append(labels, label)
    return (images, labels)


#def write_training(images, labels):
    

csv_filename = './600000.ss.txt'
data = read_data(csv_filename)

images, labels = create_images_labels(data, 2)
print('images')
print 'images.shape:', images.shape
print 'images.ndim:', images.ndim
print images[0:48]

print('labels')
print 'labels.shape:', labels.shape
print 'labels.ndim:', labels.ndim
print labels[:10]



        
    





