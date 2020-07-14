import matplotlib.pyplot as plt
import numpy as np
import pymysql
    
db = pymysql.connect(user='root', password='380@MySQL', host='127.0.0.1',database='store')
cursor = db.cursor()
sql = "SELECT * FROM store.product"
cursor.execute(sql)
products = cursor.fetchall()
ItemNames = []
ItemsAvailable = []
for products:
    ItemNames.append(product[1])
    ItemsAvailable.append(product[3])

y_pos = np.arange(len(product_name))
plt.figure(figsize=(12, 8))
plt.bar(y_pos, ItemsAvailable, align='center', alpha=0.5)
plt.xticks(y_pos, ItemNames, rotation=90)
plt.ylabel('Quantity')
plt.xlabel('Products')
plt.title('Production Bar Graph')
plt.show()
db.close()
