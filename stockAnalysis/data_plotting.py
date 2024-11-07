import matplotlib.pyplot as plt

def create_and_save_plot(dataframe_, ticker, period, filename):
    """
    Создаёт график, отображающий цены закрытия и скользящие средние.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(dataframe_['Close'], label='Цена закрытия') #Построение графика цен закрытия.


    """
    Построение скользящих средних.
    """
    ma_columns = [col for col in dataframe_.columns if 'MA_' in col]
    for col in ma_columns:
        plt.plot(dataframe_[col], label=col)

    plt.title(f'{ticker} - Цены закрытия и скользящие средние ({period})')
    plt.xlabel('Дата')
    plt.ylabel('Цена')
    plt.legend()
    plt.grid()

    plt.savefig(filename)
    plt.show()
