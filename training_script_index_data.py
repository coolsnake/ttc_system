########## Index Model #############

from utility.ML_main import *
from utility.ML_kbar_prep import *
from utility.ML_model_prep import *


# from tensorflow.python.client import device_lib
# 
# print(device_lib.list_local_devices())

mbt = ML_biaoli_train({'ts':False,
                       'rq':False, 
                       'isAnal':True, 
                       'index_list':['000016.XSHG','000905.XSHG','399300.XSHE', '000001.XSHG', '399001.XSHE', '399333.XSHE', '399006.XSHE']
                       })

# mbt.prepare_initial_training_data(initial_path='./training_data/')

#C:/Users/MetalInvest/Desktop/ML/201805-839-1200-nomacd-subBLprocess/base_data/training_index.pkl
#C:/Users/MetalInvest/Desktop/ML/201804-839-1200-nomacd-nosubBLprocess/base_data/training_index_old.pkl
mbt.initial_training(initial_data_path=['C:/Users/MetalInvest/Desktop/ML/201805-839-1200-nomacd-subBLprocess/base_data/training_index.pkl'],
                     model_name='./training_model/cnn_lstm_model_index.h5',
                     epochs=13)