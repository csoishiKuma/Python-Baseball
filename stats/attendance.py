import pandas as pd
import matplotlib.pyplot as plt
from data import games

# print(games.head(n=50))
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance')]
attendance = attendance[['year', 'multi3']]
attendance.columns = ['year', 'attendance']
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])
print(attendance.head(n=20))
attendance.plot(x='year', y='attendance', figsize=(15,7), kind='bar')
plt.xlabel("Year")
plt.ylabel("Attendance")
plt.axhline(y=attendance['attendance'].mean(), label='Mean', linestyle='--', color='green')
plt.show()