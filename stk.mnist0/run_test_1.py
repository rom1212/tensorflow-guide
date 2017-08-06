#!/usr/bin/python

import argparse
import sys
import mnist_softmax

FLAGS = None
if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='./testdata_1/',
                      help='Directory for storing input data')
  FLAGS, unparsed = parser.parse_known_args()
  print('FLAGS:', FLAGS, ', unparsed:', unparsed)

  mnist_softmax.FLAGS = FLAGS
  accuracy, precision = mnist_softmax.main([sys.argv[0]] + unparsed)
  print('accuracy: {}, precision: {}'.format(accuracy, precision))

  # tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
