mport numpy as np
import csv
import argparse
import os

defaultDir = '/data/<name>'

parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, default='config_list.txt',
                help='text file containing list of configuration files (default config.txt)')
parser.add_argument('--summaryDir', type=str, default=defaultDir,
                help='specify directory in which to store checkpoints and summaries')
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None #the pointer initially ponits to nothing

args = parser.parse_args()

cat = lambda x,y: os.path.join(x,y)

config_files = []
train_data = []
test_data = []
labels = []

file_data = open(args.config, 'r')

for config in file_data:
    config_files.append(config.rstrip())


for config in config_files:
    with open(config, 'r') as source_file:
        exec(source_file.read())
        print(config.train_data_source)
        cur_train_data = read_data(config.train_data_source)
        cur_test_data = read_data(config.test_data_source)
        cur_labels = read_data(config.data_classes)
        train_data
        #quit()

def read_data(data_source): #config_file.train_data_source)
    #head of linked list
    head = Node(None)
    with open(data_source, 'r') as train_csv:
        train_reader = csv.reader(train_csv, delimiter=',', quotechar='"')
        for i,file in enumerate(train_files):
