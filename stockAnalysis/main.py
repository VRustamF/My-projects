from data_download import fetch_stock_data, add_moving_average
from data_plotting import create_and_save_plot


def main():
    """

    Ввод данных пользователем.
    """
    ticker = input("Введите тикер акции (например, 'AAPL'): ")  #Символ тикера акции, который указывает, данные какой компании следует загрузить.
    period = input("Введите временной период для анализа (например, '1mo'): ") #Этот параметр указывает, за какой период времени следует загрузить данные.
    window_size = int(input("Введите размер окна для скользящего среднего (например, 20): ")) #Этот параметр указывает, сколько последних значений использовать для расчёта среднего.

    dataframe_ = fetch_stock_data(ticker, period)
    dataframe_ = add_moving_average(dataframe_, window_size)

    filename = f"{ticker}_{period}.png"  #Имя файла для сохранения графика. Генерируется автоматически на основе тикера и периода.
    create_and_save_plot(dataframe_, ticker, period, filename)
    print(f"График сохранен как {filename}")


if __name__ == "__main__":
    main()
