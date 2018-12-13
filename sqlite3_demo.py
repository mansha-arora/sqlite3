# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 23:39:14 2018

@author: M
"""

import sqlite3
conn = sqlite3.connect('employee.db')
c=conn.cursor()
#c.execute("""CREATE TABLE employees (
#            first text,
#            last text,
#            pay integer
#            )""")
#conn.commit()
c.execute("INSERT INTO employees VALUES ('Masoud','Kheradmandi',50000)")
c.execute("SELECT * FROM employees WHERE last='Kheradmandi'")
print(c.fetchone())
conn.commit()

conn.close()
