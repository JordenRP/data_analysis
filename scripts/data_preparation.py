
import pandas as pd

def load_and_clean_data(filepath):
    # Загружаем данные
    df = pd.read_csv(filepath)
    
    # Простейшая очистка данных
    df.dropna(inplace=True)

    # Замена запятых на точки в числовых значениях
    df = df.replace(',', '.', regex=True)

        # Преобразование всех значений в числовой формат
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

    months = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']

    df['Average_Salary'] = df[months].mean(axis=1)

    return df

if __name__ == "__main__":
    df = load_and_clean_data('data/raw/average_salary_russia.csv')
    df.to_csv('data/processed/cleaned_data.csv', index=False)
