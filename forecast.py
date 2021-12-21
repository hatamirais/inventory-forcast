'''
Buat line plot menggunakan Pandas
Data menggunakan Google Sheets
'''

# Grant access python ke akun google
from google.colab import auth
auth.authenticate_user()

# Grant acccess python ke spreadsheet
import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())

# Buka spreadsheet dan simpan sebagai variabel
csv = gc.open_by_url('https://docs.google.com/spreadsheets/d/1gsbJGZarZBCErqLCuGZH703Z-CtBtYlY6sGlZGnE_Ek/edit#gid=0')

# Ubah variable csv jadi dictionary
sheet = csv.worksheet('data')
data = sheet.get_all_records()

# Import panda dan matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Buat variabel yang bisa di gunakan pandas sebagai dataframe
df = pd.DataFrame(data)

# Buat plot dengan lline

ax = plt.gca()

# Triwulan 1 2020
df.plot(kind='line',
        figsize=(50,25),
        x='Nama',
        y='Triwulan_1_2020',
        color='blue',ax = ax)

# Triwulan 2 2020
df.plot(kind='line',
        figsize=(50,25),
        x='Nama',
        y='Triwulan_2_2020',
        color='green',ax = ax)

# Triwulan 3 2020
df.plot(kind='line',
        figsize=(50,25),
        x='Nama',
        y='Triwulan_3_2020',
        color='yellow',ax = ax)

# Triwulan 4 2020
df.plot(kind='line',
        figsize=(50,25),
        x='Nama',
        y='Triwulan_4_2020',
        color='black',ax = ax)

plt.show()
