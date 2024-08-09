import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def analyze_data(filepath):
    # Загружаем очищенные данные
    df = pd.read_csv(filepath)
    
    # Преобразуем столбцы в числовой формат, если это необходимо
    df['Год'] = pd.to_numeric(df['Год'], errors='coerce')
    df['Average_Salary'] = pd.to_numeric(df['Average_Salary'], errors='coerce')
    
    # Удаляем строки с некорректными значениями после преобразования
    df = df.dropna(subset=['Год', 'Average_Salary'])
    
    # Проверка данных по месяцам
    months = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
    
    print("Проверка данных по месяцам:")
    print(df[months].describe())
    
    # Визуальный анализ различий между месяцами
    plt.figure(figsize=(14, 8))
    for month in months:
        plt.plot(df['Год'], df[month], label=month)
    plt.title('Динамика заработной платы по месяцам')
    plt.xlabel('Год')
    plt.ylabel('Заработная плата (тыс. руб)')
    plt.legend()
    plt.grid(True)
    plt.savefig('data/processed/monthly_salary_trends.png')
    print("График динамики по месяцам сохранен в 'data/processed/monthly_salary_trends.png'")
    
    # Корреляционный анализ между месяцами
    corr_matrix = df[months].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.4f')
    plt.title('Корреляция между месяцами по зарплатам')
    plt.savefig('data/processed/correlation_matrix.png')
    print("Корреляционная матрица сохранена в 'data/processed/correlation_matrix.png'")


if __name__ == "__main__":
    analyze_data('data/processed/cleaned_data.csv')
