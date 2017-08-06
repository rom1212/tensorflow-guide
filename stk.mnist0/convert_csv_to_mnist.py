import numpy as np


def read_data(csv_filename):
    csv = np.genfromtxt(csv_filename, delimiter=",")
    print '======== read_csv file:', csv_filename
    print 'csv.dtype:', csv.dtype, ', csv.shape:', csv.shape
    
    # Change the first column to be 0
    for i in range(csv.shape[0]):
        csv[i, 0] = 0

    # useful data, remove the header, and the first column
    data = csv[1:,:]
    # remove volume = 0
    indexes = []
    for i in range(1, data.shape[0]):
      if data[i, 5] != 0.0:
        indexes.append(i)
    return data[indexes,:]

    #return data


def create_images_labels_flat(data, day_len):
    num_samples = data.shape[0] - day_len  # need one more sample for label.
    # contrib/learn/python/learn/datasets/mnist.py. images are is unint8, 
    images = np.arange(0, dtype=np.float64)
    labels = np.arange(0, dtype=np.uint8)
    for i in xrange(num_samples):
        sample = data[i:i+day_len,:]
        close_delta = data[i+day_len, 3] - data[i+day_len-1, 3]
        ratio = 1.0 * close_delta / data[i+day_len-1, 3]
#        label = 1
#        if ratio > 0.02:
#            label = 2
#        elif ratio < -0.11:
#            label = 0
        #label = 1 if ratio > 0.000001 else 0
        label = 1 if close_delta > 0 else 0
        label = 0
        if close_delta > 0:
           label = 1
        elif close_delta < 0:
           label = 0
        else:
           label = 2
        # print 'ratio:{}, label:{}'.format(ratio, label)
        images = np.append(images, sample)
        labels = np.append(labels, label)
    print 'labels:', labels, ', np.sum(labels):', np.sum(labels)
    return (images, labels, num_samples)


def read_csv_images_lables(csv_filename, day_len, dup=1):
    data = read_data(csv_filename)
    images, labels, num_samples = create_images_labels_flat(data, day_len)
    print 'num_samples:', num_samples
    print 'before reshape:'
    print '\timages.ndim:', images.ndim, ', images.shape:', images.shape
    print '\tlabels.ndim:', labels.ndim, ', labels.shape:', labels.shape

    images = images.reshape(num_samples, images.shape[0]/num_samples)
    labels = labels.reshape(num_samples, 1)
    print 'after reshape:'
    print '\timages.ndim:', images.ndim, ', images.shape:', images.shape
    print '\tlabels.ndim:', labels.ndim, ', labels.shape:', labels.shape

    out = images.reshape(-1, images.shape[1]/data.shape[1], data.shape[1])
    #print 'out.shape:', out.shape
    #print 'out[0,:]:', out[0,:]

    if (dup == 1):
        return (images, labels)

    images_2d = images.reshape(num_samples, images.shape[1]/data.shape[1], data.shape[1])
    images_2d_dup = images_2d
    for _ in range(dup - 1):
        images_2d_dup = np.concatenate((images_2d_dup, images_2d), axis=2)
    images = images_2d_dup.reshape(images_2d_dup.shape[0], images_2d_dup.shape[1]*images_2d_dup.shape[2])

    print 'after duplication:'
    print '\timages.ndim:', images.ndim, ', images.shape:', images.shape
    print '\tlabels.ndim:', labels.ndim, ', labels.shape:', labels.shape

    # out = images.reshape(-1, images.shape[1]/(data.shape[1] * dup), data.shape[1] * dup)
    #print 'out.shape:', out.shape
    #print 'out[0,:]:', out[0,:]

    return (images, labels)


def convert_tdx_txt_to_csv(txt_filename):
  csv_filename = txt_filename + '.csv'
  with open(txt_filename) as file:
    lines = file.readlines()
#    for i in range(len(lines)):
#      lines[i].strip()
    for i in range(5):
      print 'line:', lines[i]
      print 'line strip:', lines[i].rstrip()

    out_lines = []
    out_lines.append('Index,Open,High,Low,Close,Volume,Cap\n')
    # out_lines.extend(lines[2:-2])
    for line in lines[2:-2]:
      out_lines.append(line.rstrip() + '\n')

    print 'out_lines:', len(out_lines)
    with open(csv_filename, 'w') as out:
      out.writelines(out_lines)
      print 'wrote to ', csv_filename
  return csv_filename


def split_tdx_csv_to_train_test(csv_filename, start_year, test_days):
  selected_lines = []
  test_lines = []
  with open(csv_filename) as file:
    lines = file.readlines()

    selected_lines.append(lines[0])
    ok_to_add = False
    for line in lines:
      if line.startswith(start_year):
        ok_to_add = True
      if ok_to_add:
        selected_lines.append(line)

  train_filename = csv_filename + '.train.csv'
  with open(train_filename, 'w') as out:
    out.writelines(selected_lines[:-test_days])
    print 'wrote to ', train_filename

  test_lines.append(selected_lines[0])
  test_lines.extend(selected_lines[-test_days:])
  test_filename = csv_filename + '.test.csv'
  with open(test_filename, 'w') as out:
    out.writelines(test_lines)
    print 'wrote to ', test_filename
  return (train_filename, test_filename)


def convert_tdx_txt_to_train_test(txt_filename):
  csv_filename = convert_tdx_txt_to_csv(txt_filename)
  return split_tdx_csv_to_train_test(csv_filename, '2016', 50)
#  return read_csv_images_lables(csv_filename, day_len, dup)


#def write_training(images, labels):
    

#csv_filename = './600000.ss.txt'
#data = read_data(csv_filename)
#
#images, labels = create_images_labels(data, 2)
#print('images')
#print 'images.shape:', images.shape
#print 'images.ndim:', images.ndim
#print images[0:48]
#
#print('labels')
#print 'labels.shape:', labels.shape
#print 'labels.ndim:', labels.ndim
#print labels[:10]
