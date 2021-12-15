#место для твоtu
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance .csv')
df.info()

print(df['gender'].value_counts())
print('гипотза: у кого(парней или девушек) результаты экзаменов выше')
result_math_female = df[df['gender']=='female']['math score'].mean()
result_math_male = df[df['gender']=='male']['math score'].mean()
result_reading_female = df[df['gender']=='female']['reading score'].mean()
result_reading_male = df[df['gender']=='male']['reading score'].mean()
result_writing_female = df[df['gender']=='female']['writing score'].mean()
result_writing_male = df[df['gender']=='male']['writing score'].mean()

print('результат девушек по математике', round(result_math_female, 2))
print('результат парней по математике', round(result_math_male, 2))
print('результат девушек по чтению', round(result_reading_female, 2))
print('результат парней по чтению', round(result_reading_male, 2))
print('результат девушек по письму', round(result_writing_female, 2))
print('результат парней по письму', round(result_writing_male, 2))
print('у девушек выше результаты по письму и чтению, у парней выше результат по математике ')





print(df['lunch'].value_counts())
print('гипотиза: если человек ест в школе, то его результаты выше')
result_math_standart = df[df['lunch']=='standard']['math score'].mean()
result_math_free = df[df['lunch']=='free/reduced']['math score'].mean()
result_reading_standart = df[df['lunch']=='standard']['reading score'].mean()
result_reading_free = df[df['lunch']=='free/reduced']['reading score'].mean()
result_writing_standart = df[df['lunch']=='standard']['writing score'].mean()
result_writing_free = df[df['lunch']=='free/reduced']['writing score'].mean()

print('результат с едой по математике', round(result_math_standart, 2))
print('результат с едой по чтению', round(result_reading_standart, 2))
print('результат с едой по письму', round(result_writing_standart, 2))
print('результат без еды по математике', round(result_math_free, 2))
print('результат без еды по чтению', round(result_reading_free, 2))
print('результат без еды по письму', round(result_writing_free, 2))
print("данная гипотиза верна")








print(df['parental level of education'].value_counts())
print('гипотза: если у родителей есть степень магистра, то результаты выше, а если колледж,то ниже')
result_math_masters_degree =df [df["parental level of education"]=="master's degree"]['math score'].mean()
result_math_some_college =df [df["parental level of education"]=="some college"]['math score'].mean()
result_reading_masters_degree =df [df["parental level of education"]=="master's degree"]['reading score'].mean()
result_reading_some_college =df [df["parental level of education"]=="some college"]['reading score'].mean()
result_writing_masters_degree =df [df["parental level of education"]=="master's degree"]['writing score'].mean()
result_writing_some_college =df [df["parental level of education"]=="some college"]['writing score'].mean()

print('результат, со степенью магистра, по математике', round(result_math_masters_degree, 2))
print('результат, со степенью магистра, по чтению', round(result_reading_masters_degree, 2))
print('результат, со степенью магистра, по письму', round(result_writing_masters_degree, 2))
print('результат, с окончанием родителей колледжа, по математике', round(result_math_some_college, 2))
print('результат, с окончанием родителей колледжа, по чтению', round(result_reading_some_college, 2))
print('результат, с окончанием родителей колледжа, по письму', round(result_writing_some_college, 2))
print("данная гипотиза верна")








print(df['test preparation course'].value_counts())
print("гипотза: если дети проходили курс подготовки к тесту, то результаты выше")
result_math_none =df [df["test preparation course"]=="none"]['math score'].mean()
result_math_completed =df [df["test preparation course"]=="completed"]['math score'].mean()
result_reading_none =df [df["test preparation course"]=="none"]['reading score'].mean()
result_reading_completed =df [df["test preparation course"]=="completed"]['reading score'].mean()
result_writing_none =df [df["test preparation course"]=="none"]['writing score'].mean()
result_writing_completed =df [df["test preparation course"]=="completed"]['writing score'].mean()

print('результат с подготовкой по математике', round(result_math_none, 2))
print('результат с подготовкой по чтению', round(result_reading_none, 2))
print('результат с подготовкой по письму', round(result_writing_none, 2))
print('результат без подготовки по математике', round(result_math_completed, 2))
print('результат без подготовки по чтению', round(result_reading_completed, 2))
print('результат без подготовки по письму', round(result_writing_completed, 2))
print("данная гипотиза верна")








a = df['gender'].value_counts() 
a.plot(kind = 'pie') 
plt.show() 

b = pd.Series(data = [result_math_female, result_math_male, result_reading_female, result_reading_male, result_writing_female, result_writing_male], index = ['Математика девочек', 'Математика мальчиков', 'Чтение девочек', 'Чтение мальчиков', 'Письмо девочек', 'Письмо мальчиков']) 
b.plot(kind = 'barh') 
plt.show()

c = pd.Series(data = [result_math_masters_degree, result_math_some_college, result_reading_masters_degree, result_reading_some_college, result_writing_masters_degree, result_writing_some_college], index = ['Математика со степенью магистра родителей', 'Математика с окончанием родителей колледжа', 'Чтение со степенью магистра родителей', 'Чтение с окончанием родителей колледжа', 'Письмо со степенью магистра родителей', 'Письмо с окончанием родителей колледжа']) 
c.plot(kind = 'barh') 
plt.show()

d = pd.Series(data = [result_math_none, result_math_completed, result_reading_none, result_reading_completed, result_writing_none, result_writing_completed], index = ['Математика девочек', 'Математика мальчиков', 'Чтение девочек', 'Чтение мальчиков', 'Письмо девочек', 'Письмо мальчиков'])
d.plot(kind = 'barh')
plt.show()




