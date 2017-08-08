#!/usr/bin/python

import argparse
import sys
import mnist_softmax
import mnist_deep

FLAGS = None

def test_mnist_softmax():
  print('####################### test mnist_softmax.py #######################')
  mnist_softmax.FLAGS = FLAGS
  iter = 20
  accu_list = []
  prec_list = []
  for i in range(iter):
    print('################## iter: %d #################' % i)
    accuracy, precision = mnist_softmax.main([sys.argv[0]] + unparsed)
    accu_list.append(accuracy)
    prec_list.append(precision)
    print('accuracy: {}, precision: {}'.format(accuracy, precision))

  print('accu_list:', accu_list)
  print('prec_list:', prec_list)
  print('average accuracy :', sum(accu_list)/len(accu_list))
  print('average precision:', sum(prec_list)/len(prec_list))


def test_mnist_deep():
  print('####################### test mnist_deep.py #######################')
  mnist_deep.FLAGS = FLAGS
  iter = 10
  accu_list = []
  prec_list = []
  for i in range(iter):
    print('################## iter: %d #################' % i)
    accuracy, precision = mnist_deep.main([sys.argv[0]] + unparsed)
    accu_list.append(accuracy)
    prec_list.append(precision)
    print('accuracy: {}, precision: {}'.format(accuracy, precision))

  print('accu_list:', accu_list)
  print('prec_list:', prec_list)
  print('average accuracy :', sum(accu_list)/len(accu_list))
  print('average precision:', sum(prec_list)/len(prec_list))


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--data_dir', type=str, default='./testdata_1/',
                      help='Directory for storing input data')
  parser.add_argument('--type', type=str, default='all',
                      help='test type: softmax, deep, all')
  FLAGS, unparsed = parser.parse_known_args()
  print('FLAGS:', FLAGS, ', unparsed:', unparsed)

  if FLAGS.type == 'softmax' or FLAGS.type == 'all':
    test_mnist_softmax()

  if FLAGS.type == 'deep' or FLAGS.type == 'all':
    test_mnist_deep()

  # tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
