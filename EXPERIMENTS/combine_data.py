import numpy as np
import csv
import keras
#TODO:upgrade keras 2.0.5 to 2.0.8 to use Sequence??
#from keras.utils.data_utils import Sequence



#print('\n\nDEBUGGING-data_utils module: {}\n\n'.format(dir(keras.utils)))

class DataGenerator():#Sequence):
    'Generates data for keras'
    def __init__(self, adversarial_split=0.5, use_validation=False, validation_split=0.,batch_size=128, epochs=8):          
        """
            adversarial_split: 
                        Fraction of total training data that will be reserved for adversarial data generation.
                        For each individual dataset, the first (1-adversarial_split) fraction of the training
                        data is reserved for model training and the latter (adversarial_split) fraction of 
                        the training data is reserved for future adversarial data generation.

            use_validation: 
                        Replaces test set with a validation set created from partitioning train set 
                        (for parameter tuning)

                        If True, does NOT load the test set and instead splits the remaining (1-adversarial) fraction                          of each training set in the collection:
                        (1-validation_split) fraction  of the remaining training data is used for training and
                        (validation_split) fraction of the training data is used as the validation set.
                        

            validation_split: 
                        The fraction of each individual dataset that will be used to create a validation set
        """

        'Initialization'

        metadata = self.load_metadata()
        self.config_list = metadata['config_list']
        self.data_generators = self.load_data_generators(self.config_list)
        self.batch_size = batch_size
        self.epochs = epochs

        """ 
        self.labels = 
        self.num_classes = 
        self.data_gens = 
        self.shuffle =
        self.on_epoch_end()
        """

        """ 
        def __len__(self):
        'Gives number of batches per epoch'
        #return int(np.floor( len(self.train_data_len)/self.batch_size ))

        def __getitem__(self,idx):
        'Returns a complete batch'
        batch_x = [idx] 
        batch_y = [idx+1]
        return np.array(batch_x), np.array(batch_y)

        def on_epoch_end(self):
        'Allows modification of the dataset between epochs'
        #self.indexes = np.arrange(len())
        """

    def load_metadata(self):
        metadata = {}
        metadata['config_list'] = []
         
        with open('config_list.txt', 'r') as f:
            rdr = csv.reader(f, delimiter='\n', quotechar='"')
            for row in rdr:
                metadata['config_list'].append(row)
             
        return metadata

    def load_data_gens(self, config_list, use_validation=False, validation_split=0.):
        data_generators = {} 
        metadata['config_list'] = [] 

        with open('config_list.txt', 'r') as f: 
            rdr = csv.reader(f, delimiter='\n', quotechar='"')
            for row in rdr:
                metadata['config_list'].append(row)

        return data_generators 
        
if __name__ == '__main__':
    data_gen = DataGenerator()
    print(data_gen.config_list)
