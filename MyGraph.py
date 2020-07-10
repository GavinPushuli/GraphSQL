import matplotlib.pyplot as plt
import numpy as np
import pymysql
    
db = pymysql.connect(user='root', password='Qq123456', host='127.0.0.1',database='store')
cursor = db.cursor()
sql = "SELECT * FROM store.product"
cursor.execute(sql)
products = cursor.fetchall()
product_name = []
product_available = []
for product in products:
    product_name.append(product[1])
    product_available.append(product[3])

y_pos = np.arange(len(product_name))
plt.figure(figsize=(12, 8))
plt.bar(y_pos, product_available, align='center', alpha=0.5)
plt.xticks(y_pos, product_name, rotation=90)
plt.ylabel('Quantity')
plt.xlabel('Products')
plt.title('Bar Graph of Products and Quantity')
plt.show()
db.close()