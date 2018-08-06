from utility.utility_ts import *
from utility.securityDataManager import *
from ML_main import *
from ML_kbar_prep import *

pd.options.mode.chained_assignment = None


stocks = ['000002.XSHE']

#, '601138.XSHG', '000701.XSHE', '600115.XSHG'
# dates = get_trading_date_ts(count=15)
dates = JqDataRetriever.get_trading_date(count=1)
for day in dates[-1:]:
    
    mbc_week = ML_biaoli_check({'rq':False, 
                           'ts':False,
                           'model_path':'./training_model/weekly_model/cnn_lstm_model_index_weekly.h5', 
                           'isAnal':True,
                           'extra_training':False, 
                           'extra_training_period':250, # 1250
                           'save_new_model':False,
                           'long_threthold':0.9, 
                           'short_threthold':0.9, 
                           'isDebug':True, 
                           'use_latest_pivot':False, 
                           'use_standardized_sub_df':False, 
                           'use_cnn_lstm':True,
                           'use_cnn':False,
                           'check_level':['5d','1d'],
                           'sub_level_max_length':240})    
    gauge_results_week = mbc_week.gauge_stocks_analysis(stocks, today_date=day)
    
    
    mbc_day = ML_biaoli_check({'rq':False, 
                           'ts':False,
                           'model_path':'training_model/nosubprocessed/cnn_lstm_model_base.h5', 
                           'isAnal':True,
                           'extra_training':False, 
                           'extra_training_period':250, # 1250
                           'save_new_model':False,
                           'long_threthold':0.9, 
                           'short_threthold':0.9, 
                           'isDebug':True, 
                           'use_latest_pivot':False, 
                           'use_standardized_sub_df':False,
                           'use_cnn_lstm':True,
                           'use_cnn':False,
                           'check_level':['1d','30m'],
                           'sub_level_max_length':1200})
    gauge_results_day = mbc_day.gauge_stocks_analysis(stocks, today_date=day)
