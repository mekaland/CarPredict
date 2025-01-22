# -*- coding: utf-8 -*-
"""CarPredict

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BE_bnbUX2yWA7jVX57eu6rn9Z6lJBW6z

car prediction
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.compose import ColumnTransformer #sütun dönüşüm işlemleri için
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline #veri işleme hattı

!pip install xldr #excel dosyaalrını okumak için

import pandas as pd

# Excel dosyasını oku
df = pd.read_excel("/content/sample_data/cars.xls")

df

#veri ön işleme
X = df.drop('Price',axis=1)
y =df["Price"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

"""veri ön işleme ve standartlaştırma one-hot encoding işlemlerini otomatikleştiriyoruz Artık preprocess kullanarak kullanıcıdan arayüz aracılığıyla gelen veriyi modelimize uygun hale çevirebilriz

"""

preprocess = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Mileage', 'Cylinder', 'Liter', 'Doors']),
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Make', 'Model', 'Type'])
    ]
)

model = LinearRegression()

#pipeline ı tanımla veri işleme adımlarını tanımlıyosun
pipe = Pipeline(steps=[('preprocess',preprocess),('model',model)])

#pipeline fit
pipe.fit(X_train,y_train)

print(X_train.columns)

y_pred = pipe.predict(X_test)
print('MSE',mean_squared_error(y_test,y_pred)**0.5)
print('R2',r2_score(y_test,y_pred))

"""Streamlit ile modeli yayma / deploy etme / Kullanıma sunma"""

!pip install streamlit

import streamlit as st
#price tahmin fonksiyonu tanımla
def price_predict(make,model,year,mileage,car_type,cylinder,liter,doors,cruise,sound,leather):
    input_data =pd.dataFrame({'Make':[make],
                              'Model':[model],
                              'Year':[year],
                              'Mileage':[mileage],
                              'Type':[car_type],
                              'Cylinder':[cylinder],
                              'Liter':[liter],
                              'Doors':[doors],
                              'Cruise':[cruise],
                              'Sound':[sound],
                              'Leather':[leather]
                              })
    prediction = pipe.predict(input_data)[0]
    return prediction
st.title("2. el araba fiyat tahmini:red_car:@kadirdagli")
st.write("Arabanın özelliklerini seçiniz")
make= st.selectbox('Marka',df['Make'].unique())
model = st.selectbox('Model',df[df['Make']==make]['Model'].unique)
trim = st.selectbox('Trim',df[(df['Make']==make) & (df['Model']==model)]['Trim'].unique())
mileage = st.number_input('Kilometre',100,20000)
car_type= st.selectbox('Araç Tipi',df[(df['Make']==make) & (df['Model']==model)&(df['Trim']==trim)]['Type'].unique())
cylinder = st.selectbox('Cylinder',df['Cylinder'].unique())
liter = st.number_input('Yakıt Hacmi',1,10)
doors = st.selectbox('Kapı Sayısı',df['Doors'].unique())
cruise = st.selectbox('Hız Sbt.',[True,False])
sound = st.selectbox('Sesli Arac.',[True,False])
leather =st.selectbox('Koltuk Koloru',[True,False])
if st.button('Tahmin'):
  pred=price_predict(make,model,trim,mileage,car_type,cylinder,liter,doors,cruise,sound,leather)
  st.write(f'Tahmini fiyat:{pred}')

!pip install pyngrok

