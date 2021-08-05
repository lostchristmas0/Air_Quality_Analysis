# Air Quality Analysis

## Description

This project focused on analysing the air quality in Beijing from 2013 to 2017 and looked for the pattern of the spreading of air pollutants and the correlation between pullotion trends and economic progress.

## Overview

### Finished tasks

* Data cleaning
    * We finished cleaning data by remove null value from dataset.
* Data preprocessing
    * We preprocessed the data by detecting and removing the outliers.
* Data management
    * We built the database and loaded our data into the database.
* Data analysis
    * We achieved several data mining and reported the results and discussion.

### Deliverables

* preprocessing.py
* loaddata.py
* industry_pollutant.py
* weather_aqi.py

## Getting Started

### Dependencies

* python3
* pandas
* pymysql
* sqlalchemy
* mysql

### Executing program

* Clean data and load data to database.
```
python loaddata.py
```
* Read some data from database
```
python main.py 
```
* Display the sample analysis on data clustering.
```
python weather_aqi.py
python industry_pollutant.py
```

## Instruction of data mining (for test purpose)
* Modify line 183 in "weather_aqi.py" to change file (weather/pollutant csv) address
* Modify line 240-304 in "weather_aqi.py" to change permutation of weather condition (select which two parameters to use for clustring via commenting out)
* IAQI of O3 was not considered to simplify the mining
* Modify line 239 in "industry_pollutant.py" to change file (weather/pollutant csv) address
* Modify line 241 in "industry_pollutant.py" to change desired industry type and range. Modify the second parameter to change industry type (2: primary industry, 4: secondary industry, 6: tertiary industry, 0: GDP). Modify the third parameter to change quarterly range (recommended 17 as total range)
* Comment out line 254 in "industry_pollutant.py" to hide CO data because of out-range

## Authors

Dongyu Wu

Chenghui Zhu

Tuanzhang Li
