import pandas as pd


def get_student_number(sayi):
    
    file = "numbers.XLS"
    df = pd.read_excel(file)
    df['Unnamed: 1'] = pd.to_numeric(df['Unnamed: 1'], errors='coerce')
    student_no = df['Unnamed: 1'].dropna()
    student_no = student_no[student_no > sayi]
    student_number = list(map(int, student_no))

    return student_number

def get_new_student_number():
    
    file = "empty_number.XLS"
    df = pd.read_excel(file)
    new_no = df['Unnamed: 0'].dropna()
    new_number = list(map(int, new_no))

    return new_number