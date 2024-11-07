import yfinance as yf

def fetch_stock_data(ticker, period):
    """
    Получает исторические данные об акциях для указанного тикера и временного периода.
    Возвращает dataframe_ с данными.
    """
    ticker_ = yf.Ticker(ticker)
    dataframe_ = ticker_.history(period=period)
    return dataframe_

def add_moving_average(dataframe_, window_size):
    """
    Добавляет в dataframe_ колонку со скользящим средним, рассчитанным на основе цен закрытия.
    Возвращает изменённый dataframe_, который теперь содержит новый столбец со значениями скользящего среднего.
    """
    dataframe_[f'MA_{window_size}'] = dataframe_['Close'].rolling(window=window_size).mean()
    return dataframe_
