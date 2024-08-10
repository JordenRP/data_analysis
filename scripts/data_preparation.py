
import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    
    df.dropna(inplace=True)

    df = df.replace(',', '.', regex=True)

    df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

    months = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']

    df['Average_Salary'] = df[months].mean(axis=1)

    return df

if __name__ == "__main__":
    df = load_and_clean_data('data/raw/average_salary_russia.csv')
    df.to_csv('data/processed/cleaned_data.csv', index=False)
