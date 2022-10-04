import csv
import numpy as np

def ver_mean(i):
  with open(‘fns_for_model.csv‘) as csv_file:
      row = csv.reader(csv_file, delimiter=‘,‘)

      next(row)  # исключить первую строку
      data = []  # создать массив

    # Прочитайте данные i-го столбца каждой строки, кроме первой строки, и добавьте их в массив
      for r in row:
          data.append(float(r[i]))  # Преобразование строковых данных в число с плавающей запятой и добавление их в массив

  print(np.var(data))  # выходное отклонение
  print(np.mean(data))  # выходное среднее

for i in range(0, 16):
    ver_mean(i)
