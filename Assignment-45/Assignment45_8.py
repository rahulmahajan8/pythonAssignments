import matplotlib.pyplot as plt

plt.hist(df['Math'], bins=5)

plt.xlabel('Math Marks')
plt.ylabel('Number of Students')
plt.title('Distribution of Math Marks')

plt.show()