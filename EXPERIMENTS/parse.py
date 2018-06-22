import numpy as np
from glob import glob
import csv
import os
import re

MAXLEN=2048
TRAIN_SPLIT = 0.9
ignore = ['\r']

up = lambda x: os.path.dirname(x)
dataDir = up(up(os.getcwd()))

sentence_corpus_dir = os.path.join(dataDir,'SentenceCorpus','labeled_articles','*')
errors = []
cat_dict = {}
actual_labels = sorted({'AIMX','BASE','CONT','MISC','OWNX'})
for i,c in enumerate(actual_labels):
    cat_dict[c] = i

parsed_labels = set()#python set stores unique elements

#this split token ordering  gives the best split w.r.t to the other two below
splitTokens = ["\t","--",  " "]
#splitTokens = ["--", "\t", " "]
#splitTokens = [ " ","--", "\t"]
#----------------------------------------------------------------------
def splitTab(idx, inp_str):
    try: #split on first '--'
            cat, x_str = inp_str.split(splitTokens[0],1)
    except:
            try: #split on tab
                    cat,x_str = re.split(splitTokens[1],inp_str)
                    print('\ncat: {} ({}) \nstr: {} \n\n'.format(repr(str(cat_dict[cat])), repr(cat),repr(x_str)))
            except:
                    try: #split on first space
                        cat, x_str = inp_str.split(splitTokens[2],1)
                    except:
                        errors.append([repr(inp_str)])
                        cat,x_str = ('NULL','NULL')
                        print('\ncat: {} \nstr: {} \nerror: {} \n\n'.format(cat,x_str,repr(inp_str)))
    """
    except ValueError:
        raise ValueError(' i: {} re.split("\\t", {})'.format(idx,repr(inp_str)))
    """
    cat = cat.strip(' ')
    parsed_labels.add(cat)
    return cat,x_str
#----------------------------------------------------------------------
journal_files = glob(sentence_corpus_dir)
n_train = int(len(journal_files)*TRAIN_SPLIT)
np.random.shuffle(journal_files)
train_files = journal_files[:n_train]
test_files = journal_files[n_train:]
print('journal train files: {}, journal test files: {}'.format(len(train_files),len(test_files)))

with open('train.csv', 'w') as train_csv:
    train_writer = csv.writer(train_csv, delimiter=',', quotechar='"')
    for file in train_files:
        f = open(file, 'r')
        trainStr = f.read()
        f.close()
        trainStr = re.split("###.*###",trainStr)#Remove abstract and intro line delimiters
        trainStr = trainStr[1:]#Remove empty string
        trainStr1 = re.split("\n",trainStr[0])
        trainStr1 = filter(None,trainStr1)
        trainStr2 = re.split("\n",trainStr[1])
        trainStr2 = filter(None,trainStr2)
        #TODO:REMOVE MAXLEN ON STRINGS???
        #print(trainStr1[0])#DEBUGGING
        train1 = [[str(cat_dict[cat]),repr(x[:MAXLEN])] for cat,x in (splitTab(i,trainEx) for i,trainEx in enumerate(trainStr1) if trainEx not in ignore)]
        train2 = [[str(cat_dict[cat]),repr(x[:MAXLEN])] for cat,x in (splitTab(i,trainEx) for i,trainEx in enumerate(trainStr2) if trainEx not in ignore)]

        #s = f.read(MAXLEN)
        train_writer.writerows(filter(None,train1))
        train_writer.writerows(filter(None,train2))

with open('test.csv', 'w') as test_csv:
    test_writer = csv.writer(test_csv, delimiter=',', quotechar='"')
    for file in test_files:
        f = open(file, 'r')
        testStr = f.read()
        f.close()
        testStr = re.split("###.*###",testStr)#Remove abstract and intro line delimiters
        testStr = testStr[1:]#Remove empty string
        testStr1 = re.split("\n",testStr[0])

        testStr1 = filter(None,testStr1)
        testStr2 = re.split("\n",testStr[1])
        testStr2 = filter(None,testStr2)
        #TODO:REMOVE MAXLEN ON STRINGS???
        test1 = [[str(cat_dict[cat]),repr(x[:MAXLEN])] for cat,x in (splitTab(i,testEx) for i,testEx in enumerate(testStr1) if testEx not in ignore)]
        test2 = [[str(cat_dict[cat]),repr(x[:MAXLEN])] for cat,x in (splitTab(i,testEx) for i,testEx in enumerate(testStr2) if testEx not in ignore)]

        #s = f.read(MAXLEN)
        test_writer.writerows(filter(None,test1))
        test_writer.writerows(filter(None,test2))


print('---------------------------------------------------------------------------------------------------------------------------------------')
with open('errors.csv', 'w') as error_csv:
    print('num errors = {}'.format(len(errors)))
    error_writer = csv.writer(error_csv, delimiter='\n',quotechar='"')
    error_writer.writerows(errors)


#sort labels
parsed_labels = sorted(parsed_labels)
with open('classes.txt', 'w') as classes_csv:
    classes_writer = csv.writer(classes_csv, delimiter='\n',quotechar='"')
    classes_writer.writerows([[label] for label in actual_labels])

print('\nnum parsed_labels = {} \nparsed_labels = {}'.format(len(parsed_labels), parsed_labels))
print('\nnum actual_labels = {} \nactual_labels = {}'.format(len(actual_labels), actual_labels))
print('\ncategory dictionary: {}'.format(cat_dict))
