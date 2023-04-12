#!/usr/bin/env python
# coding: utf-8

# # Water Quality Prediction

# #### Dataset Description
# 
# #### Context
# Access to safe drinking-water is essential to health, a basic human right and a component of effective policy for health protection. This is important as a health and development issue at a national, regional and local level. In some regions, it has been shown that investments in water supply and sanitation can yield a net economic benefit, since the reductions in adverse health effects and health care costs outweigh the costs of undertaking the interventions.
# 
# #### Content
# The water_potability.csv file contains water quality metrics for 3276 different water bodies.
# 
# ##### 1. pH value:
# PH is an important parameter in evaluating the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5. The current investigation ranges were 6.52–6.83 which are in the range of WHO standards.
# 
# ##### 2. Hardness:
# Hardness is mainly caused by calcium and magnesium salts. These salts are dissolved from geologic deposits through which water travels. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium.
# 
# ##### 3. Solids (Total dissolved solids - TDS):
# Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and diluted color in appearance of water. This is the important parameter for the use of water. The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l which prescribed for drinking purpose.
# 
# ##### 4. Chloramines:
# Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.
# 
# ##### 5. Sulfate:
# Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. The principal commercial use of sulfate is in the chemical industry. Sulfate concentration in seawater is about 2,700 milligrams per liter (mg/L). It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.
# 
# ##### 6. Conductivity:
# Pure water is not a good conductor of electric current rather’s a good insulator. Increase in ions concentration enhances the electrical conductivity of water. Generally, the amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.
# 
# ##### 7. Organic_carbon:
# Total Organic Carbon (TOC) in source waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment.
# 
# ##### 8. Trihalomethanes:
# THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water that is being treated. THM levels up to 80 ppm is considered safe in drinking water.
# 
# ##### 9. Turbidity:
# The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.
# 
# ##### 10. Potability:
# Indicates if water is safe for human consumption where 1 means Potable and 0 means Not potable.
# (0) Water is not safe to drink and (1) Water is safe to drink

# # Data Gathering

# In[1]:


import pandas as pd # Data Processing
import numpy as np # Linear Algebra
import seaborn as sns # Stastistical Visualization
import matplotlib.pyplot as plt # Visualization for Numpy and Pandas
import warnings
warnings.filterwarnings("ignore") # Ignore the warnings


# In[2]:


data = pd.read_csv(r"D:\DS projects\water quality analysis\water_potability.csv")
data.head()


# In[3]:


data.shape # No of Rows and No of Columns


# In[4]:


data.isnull().sum() # Missing Counts


# In[5]:


data.describe() # Stats for each column


# 
# ####  Missing values handling in this Dataset can be done in 2 ways 
# 
#  1. entire data can be replace with Mean Strategy
#  2. Missing value column as per column strategy
#  
#  It should be done based on statistics values

# In[4]:


data.fillna(data.mean(), inplace =True)

#data["ph"]=data["ph"].fillna(data["ph"].mean())
#data["Sulfate"]=data["Sulfate"].fillna(data["Sulfate"].median())
#data["Trihalomethanes"]=data["Trihalomethanes"].fillna(data["Trihalomethanes"].mean())


# In[5]:


data.isnull().sum()


# ### Data Distribution 
# #### with the visulization we can predict data is Biased distribution

# In[7]:


plt.figure(figsize=(8,5))
sns.countplot(data.Potability)
plt.title("distribution of safe and unsafe water")
plt.show()


# In[8]:


potability_counts = data['Potability'].value_counts()
labels = ['Potable', 'Not Potable']

plt.pie(potability_counts, labels=labels, autopct='%1.1f%%')
plt.title('Potability Distribution')
plt.show()


# In[18]:


# futher level of checking the distribution, in column wise
data.hist(figsize=(10,12))
plt.show()


# In[11]:


# lets check the Histogram using plotly for individual variables
import plotly.express as px


# In[21]:


px.histogram(data, x="ph", color= "Potability", title= "Factors Affecting Water Quality: PH")


# In[11]:


px.histogram(data, x="Hardness", color= "Potability", title= "Factors Affecting Water Quality: Hardness")


# In[12]:


px.histogram(data, x="Solids", color= "Potability", title= "Factors Affecting Water Quality: Solids")


# In[14]:


# lets visualize with KDE plot for futher Analysis
not_potable= data.query("Potability==0")
potable= data.query("Potability==1")

plt.figure(figsize=(15,15))
for i, col in enumerate(data.columns[:9]):
    plt.subplot(3,3,i+1)
    plt.title(col)
    sns.kdeplot(x= not_potable[col], label= "not potable")
    sns.kdeplot(x=potable[col], label = "potable")
    plt.legend()
    


# In[15]:


corr= round(data.corr(),2)
corr


# In[16]:


plt.figure(figsize=(10,8))
sns.heatmap(data=corr, cmap="coolwarm", annot=True, linewidths=0.8)


# # pip install pycaret
# 
# PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows. It is an end-to-end machine learning and model management tool that speeds up the experiment cycle exponentially and makes you more productive.
# 
# In comparison with the other open-source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few words only. This makes experiments exponentially fast and efficient.

# In[18]:


from pycaret.classification import *
clf= setup(data, target= "Potability", session_id= 786)
compare_models()


# In[19]:


# Lets create model with Extra Trees Classifier, as it gave top results in many aspects
model= create_model("et")
predict= predict_model(model, data=data)
predict


# In[20]:


# Lets try with Random Forest Classifier and model Accuracy
model_rf= create_model("rf")
predict_rf= predict_model(model_rf, data=data)
predict_rf


# In[ ]:




