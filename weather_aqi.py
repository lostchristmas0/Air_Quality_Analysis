import pandas as pd
# import numpy as np
# from collections import Counter
# from typing import NamedTuple, List
import datetime
import matplotlib.pyplot as plt

INDEX_POLLUTANT = {5: 'PM2.5', 6: 'PM10', 7: 'SO2', 8: 'NO2', 9: 'CO', 10: 'O3'}
IAQI_PM25 = {0: 0, 50: 35, 100: 75, 150: 115, 200: 150, 300: 250, 400: 350, 500: 500}
IAQI_PM10 = {0: 0, 50: 50, 100: 150, 150: 250, 200: 350, 300: 420, 400: 500, 500: 600}
IAQI_SO2 = {0: 0, 50: 50, 100: 150, 150: 475, 200: 800, 300: 1600, 400: 2100, 500: 2620}
IAQI_NO2 = {0: 0, 50: 40, 100: 80, 150: 180, 200: 280, 300: 565, 400: 750, 500: 940}
IAQI_CO = {0: 0, 50: 2000, 100: 4000, 150: 14000, 200: 24000, 300: 36000, 400: 48000, 500: 60000}


def daily(table):
    """
    Separate the original table into daily tables
    :param table: original dataFrame table
    :return: a dictionary of date: sub dataFrame table
    """
    first_day = datetime.date(table.iloc[0, 1], table.iloc[0, 2], table.iloc[0, 3])
    current = first_day
    start = 0
    daily_dict = {}
    for r in range(1, len(table)):
        if table.iloc[r, 3] != table.iloc[r - 1, 3]:
            daily_dict[current] = table.iloc[start:r, :]
            start = r
            current = datetime.date(table.iloc[r, 1], table.iloc[r, 2], table.iloc[r, 3])
    daily_dict[current] = table.iloc[start:, :]
    return daily_dict


def calculate_iaqi(value, relation):
    """
    Calculate the iaqi based on one of the pollutant
    :param value: the average pollutant concentration
    :param relation: the dictionary to calculate the iaqi
    :return: iaqi value
    """
    bpl = min(relation.values())
    bph = max(relation.values())
    iaqil = min(relation.keys())
    iaqih = max(relation.keys())
    if value <= relation[50]:
        bph = relation[50]
        iaqih = 50
    elif relation[50] < value <= relation[100]:
        bpl = relation[50]
        bph = relation[100]
        iaqil = 50
        iaqih = 100
    elif relation[100] < value <= relation[150]:
        bpl = relation[100]
        bph = relation[150]
        iaqil = 100
        iaqih = 150
    elif relation[150] < value <= relation[200]:
        bpl = relation[150]
        bph = relation[200]
        iaqil = 150
        iaqih = 200
    elif relation[200] < value <= relation[300]:
        bpl = relation[200]
        bph = relation[300]
        iaqil = 200
        iaqih = 300
    elif relation[300] < value <= relation[400]:
        bpl = relation[300]
        bph = relation[400]
        iaqil = 300
        iaqih = 400
    elif value > relation[400]:
        bpl = relation[400]
        iaqil = 400
    return (iaqih - iaqil) * (value - bpl) / (bph - bpl) + iaqil


def aqi(table):
    """
    Calculate the real AQI value
    :param table: daily sub-framework
    :return: the AQI value (1~6)
    """
    pm25 = []
    pm10 = []
    so2 = []
    no2 = []
    co = []
    iaqi = []
    for i in range(len(table)):
        if not pd.isnull(table.iloc[i, 5]):
            pm25.append(table.iloc[i, 5])
        if not pd.isnull(table.iloc[i, 6]):
            pm10.append(table.iloc[i, 6])
        if not pd.isnull(table.iloc[i, 7]):
            so2.append(table.iloc[i, 7])
        if not pd.isnull(table.iloc[i, 8]):
            no2.append(table.iloc[i, 8])
        if not pd.isnull(table.iloc[i, 9]):
            co.append(table.iloc[i, 9])
    if len(pm25) == 0:
        iaqi.append(0)
    else:
        iaqi.append(calculate_iaqi(sum(pm25) / len(pm25), IAQI_PM25))
    if len(pm10) == 0:
        iaqi.append(0)
    else:
        iaqi.append(calculate_iaqi(sum(pm10) / len(pm10), IAQI_PM10))
    if len(so2) == 0:
        iaqi.append(0)
    else:
        iaqi.append(calculate_iaqi(sum(so2) / len(so2), IAQI_SO2))
    if len(no2) == 0:
        iaqi.append(0)
    else:
        iaqi.append(calculate_iaqi(sum(no2) / len(no2), IAQI_NO2))
    if len(co) == 0:
        iaqi.append(0)
    else:
        iaqi.append(calculate_iaqi(sum(co) / len(co), IAQI_CO))
    maxaqi = max(iaqi)
    if 0 <= maxaqi < 50:
        return 1
    elif 50 <= maxaqi < 100:
        return 2
    elif 100 <= maxaqi < 150:
        return 3
    elif 150 <= maxaqi < 200:
        return 4
    elif 200 <= maxaqi < 300:
        return 5
    elif maxaqi >= 300:
        return 6
    else:
        return 0


def meteorology_daily(table):
    """
    Find the desired meteorological data
    :param table: daily sub-framework
    :return: a list of meteorological data
    """
    data = []
    temp = []
    pres = []
    dewp = []
    rain = []
    for i in range(len(table)):
        if not pd.isnull(table.iloc[i, 11]):
            temp.append(table.iloc[i, 11])
        if not pd.isnull(table.iloc[i, 12]):
            pres.append(table.iloc[i, 12])
        if not pd.isnull(table.iloc[i, 13]):
            dewp.append(table.iloc[i, 13])
        if not pd.isnull(table.iloc[i, 14]):
            rain.append(table.iloc[i, 14])
    data.append(sum(temp) / len(temp))
    data.append(sum(pres) / len(pres))
    data.append(sum(dewp) / len(dewp))
    data.append(sum(rain))
    return data


def get_plot(location):
    """
    Get the plot data for displaying
    :param location: the original csv file address
    :return: a list of plot data
    """
    data = []
    table = pd.read_csv(location)
    daily_table = daily(table)
    for key, value in daily_table.items():
        current = [key, aqi(value), meteorology_daily(value)]
        data.append(current)
    return data


def main():
    date_aqi_meteorology = get_plot("datasheets/Air_Quality/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    aqi1_t = []
    aqi1_p = []
    aqi1_d = []
    aqi1_r = []
    aqi2_t = []
    aqi2_p = []
    aqi2_d = []
    aqi2_r = []
    aqi3_t = []
    aqi3_p = []
    aqi3_d = []
    aqi3_r = []
    aqi4_t = []
    aqi4_p = []
    aqi4_d = []
    aqi4_r = []
    aqi5_t = []
    aqi5_p = []
    aqi5_d = []
    aqi5_r = []
    aqi6_t = []
    aqi6_p = []
    aqi6_d = []
    aqi6_r = []
    for x in date_aqi_meteorology:
        if x[1] == 1:
            aqi1_t.append(x[2][0])
            aqi1_p.append(x[2][1])
            aqi1_d.append(x[2][2])
            aqi1_r.append(x[2][3])
        elif x[1] == 2:
            aqi2_t.append(x[2][0])
            aqi2_p.append(x[2][1])
            aqi2_d.append(x[2][2])
            aqi2_r.append(x[2][3])
        elif x[1] == 3:
            aqi3_t.append(x[2][0])
            aqi3_p.append(x[2][1])
            aqi3_d.append(x[2][2])
            aqi3_r.append(x[2][3])
        elif x[1] == 4:
            aqi4_t.append(x[2][0])
            aqi4_p.append(x[2][1])
            aqi4_d.append(x[2][2])
            aqi4_r.append(x[2][3])
        elif x[1] == 5:
            aqi5_t.append(x[2][0])
            aqi5_p.append(x[2][1])
            aqi5_d.append(x[2][2])
            aqi5_r.append(x[2][3])
        elif x[1] == 6:
            aqi6_t.append(x[2][0])
            aqi6_p.append(x[2][1])
            aqi6_d.append(x[2][2])
            aqi6_r.append(x[2][3])

    # # temp_pres:
    # plt.scatter(aqi1_t, aqi1_p, color='green', marker='.', label='AQI = 1')
    # plt.scatter(aqi2_t, aqi2_p, color='yellow', marker='.', label='AQI = 2')
    # plt.scatter(aqi3_t, aqi3_p, color='orange', marker='.', label='AQI = 3')
    # plt.scatter(aqi4_t, aqi4_p, color='red', marker='.', label='AQI = 4')
    # plt.scatter(aqi5_t, aqi5_p, color='purple', marker='.', label='AQI = 5')
    # plt.scatter(aqi6_t, aqi6_p, color='brown', marker='.', label='AQI = 6')
    # # plt.title("Influence of meteorological parameters on AQI")
    # plt.ylabel("pressure (hPa)")
    # plt.xlabel("temperature (Celsius)")

    # temp_dewp (possible trend):
    plt.scatter(aqi1_t, aqi1_d, color='green', marker='.', label='AQI = 1')
    plt.scatter(aqi2_t, aqi2_d, color='yellow', marker='.', label='AQI = 2')
    plt.scatter(aqi3_t, aqi3_d, color='orange', marker='.', label='AQI = 3')
    plt.scatter(aqi4_t, aqi4_d, color='red', marker='.', label='AQI = 4')
    plt.scatter(aqi5_t, aqi5_d, color='purple', marker='.', label='AQI = 5')
    plt.scatter(aqi6_t, aqi6_d, color='brown', marker='.', label='AQI = 6')
    # plt.title("Influence of meteorological parameters on AQI")
    plt.ylabel("dew point (Celsius)")
    plt.xlabel("temperature (Celsius)")

    # # temp_rain:
    # plt.scatter(aqi1_t, aqi1_r, color='green', marker='.', label='AQI = 1')
    # plt.scatter(aqi2_t, aqi2_r, color='yellow', marker='.', label='AQI = 2')
    # plt.scatter(aqi3_t, aqi3_r, color='orange', marker='.', label='AQI = 3')
    # plt.scatter(aqi4_t, aqi4_r, color='red', marker='.', label='AQI = 4')
    # plt.scatter(aqi5_t, aqi5_r, color='purple', marker='.', label='AQI = 5')
    # plt.scatter(aqi6_t, aqi6_r, color='brown', marker='.', label='AQI = 6')
    # # plt.title("Influence of meteorological parameters on AQI")
    # plt.ylabel("rain (mm)")
    # plt.xlabel("temperature (Celsius)")

    # # pres_dewp:
    # plt.scatter(aqi1_p, aqi1_d, color='green', marker='.', label='AQI = 1')
    # plt.scatter(aqi2_p, aqi2_d, color='yellow', marker='.', label='AQI = 2')
    # plt.scatter(aqi3_p, aqi3_d, color='orange', marker='.', label='AQI = 3')
    # plt.scatter(aqi4_p, aqi4_d, color='red', marker='.', label='AQI = 4')
    # plt.scatter(aqi5_p, aqi5_d, color='purple', marker='.', label='AQI = 5')
    # plt.scatter(aqi6_p, aqi6_d, color='brown', marker='.', label='AQI = 6')
    # # plt.title("Influence of meteorological parameters on AQI")
    # plt.ylabel("dew point (Celsius)")
    # plt.xlabel("pressure (hPa)")

    # # pres_rain:
    # plt.scatter(aqi1_p, aqi1_r, color='green', marker='.', label='AQI = 1')
    # plt.scatter(aqi2_p, aqi2_r, color='yellow', marker='.', label='AQI = 2')
    # plt.scatter(aqi3_p, aqi3_r, color='orange', marker='.', label='AQI = 3')
    # plt.scatter(aqi4_p, aqi4_r, color='red', marker='.', label='AQI = 4')
    # plt.scatter(aqi5_p, aqi5_r, color='purple', marker='.', label='AQI = 5')
    # plt.scatter(aqi6_p, aqi6_r, color='brown', marker='.', label='AQI = 6')
    # # plt.title("Influence of meteorological parameters on AQI")
    # plt.ylabel("rain (mm)")
    # plt.xlabel("pressure (hPa)")

    # # dewp_rain:
    # plt.scatter(aqi1_d, aqi1_r, color='green', marker='.', label='AQI = 1')
    # plt.scatter(aqi2_d, aqi2_r, color='yellow', marker='.', label='AQI = 2')
    # plt.scatter(aqi3_d, aqi3_r, color='orange', marker='.', label='AQI = 3')
    # plt.scatter(aqi4_d, aqi4_r, color='red', marker='.', label='AQI = 4')
    # plt.scatter(aqi5_d, aqi5_r, color='purple', marker='.', label='AQI = 5')
    # plt.scatter(aqi6_d, aqi6_r, color='brown', marker='.', label='AQI = 6')
    # # plt.title("Influence of meteorological parameters on AQI")
    # plt.ylabel("rain (mm)")
    # plt.xlabel("dew point (Celsius)")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()