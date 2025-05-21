#fichier contentant toutes les constantes et les informations importantes

#back test informations
capital =   1000
risk_max = (1.5/100)
risk_min = (0.5/100)

#intervals
fast_intervals = ['1m','3m','5m','15m', '1h']
slow_intervals = ['1h', '2h', '4h', '1d']
long_term_intervals = ['1w', '1mo','1y', '5y', '10y']


#API KEYS
CLE_API_BROKER = 'api_key'

#data resssources
forex_tickers = [
    "EURUSD=X",  # Euro / US Dollar
    "USDJPY=X",  # US Dollar / Japanese Yen
    "GBPUSD=X",  # British Pound / US Dollar
    "USDCHF=X",  # US Dollar / Swiss Franc
    "AUDUSD=X",  # Australian Dollar / US Dollar
    "NZDUSD=X",  # New Zealand Dollar / US Dollar
    "USDCAD=X",  # US Dollar / Canadian Dollar

    "EURGBP=X",  # Euro / British Pound
    "EURJPY=X",  # Euro / Japanese Yen
    "GBPJPY=X",  # British Pound / Japanese Yen
    "AUDJPY=X",  # Australian Dollar / Japanese Yen
    "NZDJPY=X",  # New Zealand Dollar / Japanese Yen

    "EURAUD=X",  # Euro / Australian Dollar
    "GBPAUD=X",  # British Pound / Australian Dollar
    "EURCHF=X",  # Euro / Swiss Franc
]

#data refreshing timeframes
data_refersh = "daily"

#modules weights
weights = {"quant":0.2,"tech":0.3, "macro":0.4,"risk":0.1 }

