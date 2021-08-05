import pandas as pd
import numpy as np
from collections import Counter
from typing import NamedTuple, List
import matplotlib.pyplot as plt

INDEX_POLLUTANT = {5: 'PM2.5', 6: 'PM10', 7: 'SO2', 8: 'NO2', 9: 'CO', 10: 'O3'}


def average_quarterly(table):
    """
    Get the average pollutant dictionary seperated by quarterly
    :param table: pandas dataFrame. Original pollutant table from column A-Q
    :return: a dictionary of quarterly: list of pollutant
    """
    quarterly_pollutant = {'1Q 2013': [], '2Q 2013': [], '3Q 2013': [], '4Q 2013': [],
                           '1Q 2014': [], '2Q 2014': [], '3Q 2014': [], '4Q 2014': [],
                           '1Q 2015': [], '2Q 2015': [], '3Q 2015': [], '4Q 2015': [],
                           '1Q 2016': [], '2Q 2016': [], '3Q 2016': [], '4Q 2016': [],
                           '1Q 2017': []}
    temp20131 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20132 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20133 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20134 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20141 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20142 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20143 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20144 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20151 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20152 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20153 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20154 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20161 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20162 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20163 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20164 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}
    temp20171 = {'PM2.5': [], 'PM10': [], 'SO2': [], 'NO2': [], 'CO': [], 'O3': []}

    for i in range(len(table)):
        if table.iloc[i, 1] == 2013 and 1 <= table.iloc[i, 2] <= 3:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20131[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2013 and 4 <= table.iloc[i, 2] <= 6:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20132[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2013 and 7 <= table.iloc[i, 2] <= 9:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20133[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2013 and 10 <= table.iloc[i, 2] <= 12:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20134[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2014 and 1 <= table.iloc[i, 2] <= 3:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20141[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2014 and 4 <= table.iloc[i, 2] <= 6:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20142[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2014 and 7 <= table.iloc[i, 2] <= 9:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20143[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2014 and 10 <= table.iloc[i, 2] <= 12:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20144[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2015 and 1 <= table.iloc[i, 2] <= 3:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20151[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2015 and 4 <= table.iloc[i, 2] <= 6:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20152[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2015 and 7 <= table.iloc[i, 2] <= 9:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20153[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2015 and 10 <= table.iloc[i, 2] <= 12:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20154[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2016 and 1 <= table.iloc[i, 2] <= 3:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20161[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2016 and 4 <= table.iloc[i, 2] <= 6:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20162[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2016 and 7 <= table.iloc[i, 2] <= 9:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20163[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2016 and 10 <= table.iloc[i, 2] <= 12:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20164[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
        elif table.iloc[i, 1] == 2017 and 1 <= table.iloc[i, 2] <= 3:
            for x in range(5, 11):
                if not pd.isnull(table.iloc[i, x]):
                    temp20171[INDEX_POLLUTANT[x]].append(table.iloc[i, x])

    # for i in range(len(table)):
    #     for x in range(5, 11):  # pollutant index from original table (PM2.5~O3: 5~10)
    #         if table.iloc[i, 1] == 2013 and 1 <= table.iloc[i, 2] <= 3 and not pd.isnull(table.iloc[i, x]):
    #             temp20131[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2013 and 4 <= table.iloc[i, 2] <= 6 and not pd.isnull(table.iloc[i, x]):
    #             temp20132[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2013 and 7 <= table.iloc[i, 2] <= 9 and not pd.isnull(table.iloc[i, x]):
    #             temp20133[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2013 and 10 <= table.iloc[i, 2] <= 12 and not pd.isnull(table.iloc[i, x]):
    #             temp20134[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2014 and 1 <= table.iloc[i, 2] <= 3 and not pd.isnull(table.iloc[i, x]):
    #             temp20141[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2014 and 4 <= table.iloc[i, 2] <= 6 and not pd.isnull(table.iloc[i, x]):
    #             temp20142[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2014 and 7 <= table.iloc[i, 2] <= 9 and not pd.isnull(table.iloc[i, x]):
    #             temp20143[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2014 and 10 <= table.iloc[i, 2] <= 12 and not pd.isnull(table.iloc[i, x]):
    #             temp20144[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2015 and 1 <= table.iloc[i, 2] <= 3 and not pd.isnull(table.iloc[i, x]):
    #             temp20151[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2015 and 4 <= table.iloc[i, 2] <= 6 and not pd.isnull(table.iloc[i, x]):
    #             temp20152[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2015 and 7 <= table.iloc[i, 2] <= 9 and not pd.isnull(table.iloc[i, x]):
    #             temp20153[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2015 and 10 <= table.iloc[i, 2] <= 12 and not pd.isnull(table.iloc[i, x]):
    #             temp20154[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2016 and 1 <= table.iloc[i, 2] <= 3 and not pd.isnull(table.iloc[i, x]):
    #             temp20161[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2016 and 4 <= table.iloc[i, 2] <= 6 and not pd.isnull(table.iloc[i, x]):
    #             temp20162[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2016 and 7 <= table.iloc[i, 2] <= 9 and not pd.isnull(table.iloc[i, x]):
    #             temp20163[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2016 and 10 <= table.iloc[i, 2] <= 12 and not pd.isnull(table.iloc[i, x]):
    #             temp20164[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    #         elif table.iloc[i, 1] == 2017 and 1 <= table.iloc[i, 2] <= 3 and not pd.isnull(table.iloc[i, x]):
    #             temp20171[INDEX_POLLUTANT[x]].append(table.iloc[i, x])
    for value in temp20131.values():
        quarterly_pollutant['1Q 2013'].append(sum(value)/len(value))
    for value in temp20132.values():
        quarterly_pollutant['2Q 2013'].append(sum(value)/len(value))
    for value in temp20133.values():
        quarterly_pollutant['3Q 2013'].append(sum(value)/len(value))
    for value in temp20134.values():
        quarterly_pollutant['4Q 2013'].append(sum(value)/len(value))
    for value in temp20141.values():
        quarterly_pollutant['1Q 2014'].append(sum(value)/len(value))
    for value in temp20142.values():
        quarterly_pollutant['2Q 2014'].append(sum(value)/len(value))
    for value in temp20143.values():
        quarterly_pollutant['3Q 2014'].append(sum(value)/len(value))
    for value in temp20144.values():
        quarterly_pollutant['4Q 2014'].append(sum(value)/len(value))
    for value in temp20151.values():
        quarterly_pollutant['1Q 2015'].append(sum(value)/len(value))
    for value in temp20152.values():
        quarterly_pollutant['2Q 2015'].append(sum(value)/len(value))
    for value in temp20153.values():
        quarterly_pollutant['3Q 2015'].append(sum(value)/len(value))
    for value in temp20154.values():
        quarterly_pollutant['4Q 2015'].append(sum(value)/len(value))
    for value in temp20161.values():
        quarterly_pollutant['1Q 2016'].append(sum(value)/len(value))
    for value in temp20162.values():
        quarterly_pollutant['2Q 2016'].append(sum(value)/len(value))
    for value in temp20163.values():
        quarterly_pollutant['3Q 2016'].append(sum(value)/len(value))
    for value in temp20164.values():
        quarterly_pollutant['4Q 2016'].append(sum(value)/len(value))
    for value in temp20171.values():
        quarterly_pollutant['1Q 2017'].append(sum(value)/len(value))
    # quarterly_pollutant['1Q 2013'] = [sum(temp20131) / len(temp20131)]
    # quarterly_pollutant['2Q 2013'] = [sum(temp20132) / len(temp20132)]
    # quarterly_pollutant['3Q 2013'] = [sum(temp20133) / len(temp20133)]
    # quarterly_pollutant['4Q 2013'] = [sum(temp20134) / len(temp20134)]
    # quarterly_pollutant['1Q 2014'] = [sum(temp20141) / len(temp20141)]
    # quarterly_pollutant['2Q 2014'] = [sum(temp20142) / len(temp20142)]
    # quarterly_pollutant['3Q 2014'] = [sum(temp20143) / len(temp20143)]
    # quarterly_pollutant['4Q 2014'] = [sum(temp20144) / len(temp20144)]
    # quarterly_pollutant['1Q 2015'] = [sum(temp20151) / len(temp20151)]
    # quarterly_pollutant['2Q 2015'] = [sum(temp20152) / len(temp20152)]
    # quarterly_pollutant['3Q 2015'] = [sum(temp20153) / len(temp20153)]
    # quarterly_pollutant['4Q 2015'] = [sum(temp20154) / len(temp20154)]
    # quarterly_pollutant['1Q 2016'] = [sum(temp20161) / len(temp20161)]
    # quarterly_pollutant['2Q 2016'] = [sum(temp20162) / len(temp20162)]
    # quarterly_pollutant['3Q 2016'] = [sum(temp20163) / len(temp20163)]
    # quarterly_pollutant['4Q 2016'] = [sum(temp20164) / len(temp20164)]
    # quarterly_pollutant['1Q 2017'] = [sum(temp20171) / len(temp20171)]
    return quarterly_pollutant


def get_economic(table, index, length):
    """
    Get the selected industry data
    :param table: economic table
    :param index: row index (which industry value)
    :param length: selected the first "length" values (total 17 quarterly)
    :return: a distionary of selected industry data
    """
    row = [0 if pd.isnull(x) else x for x in table.iloc[index, :].tolist()]
    value = row[::-1][0:length]
    head = table.columns.tolist()[::-1][0:length]
    quarterly_economic = {}
    for i in range(len(head)):
        quarterly_economic[head[i]] = value[i]
    return quarterly_economic


def get_plot(table1, index1, length1, table2):
    """
    Generate the plot data for visualization
    :param table1: raw distributed table (economic table)
    :param table2: column distributed table (pollutant table)
    :return: a list of data: each data is a list of [quarterly, economic value, [pollutant list]]
    """
    pollutant = average_quarterly(table2)
    economic = get_economic(table1, index1, length1)
    if len(pollutant) != len(economic):
        raise ValueError("pollutant and economic data do not match")
    plot_data = []
    for key, value in pollutant.items():
        plot_data.append([key, economic[key], value])
    return plot_data


def main():
    # test = pd.read_csv("proj_data/PRSA_Data_Aotizhongxin_20130301-20170228.csv")
    # q_p = average_quarterly(test)
    # print(q_p)
    # test = pd.read_csv("proj_data/Quarterly_modified.csv")
    # print(get_economic(test, 2, 17))
    pollutant_table = pd.read_csv("datasheets/Air_Quality/PRSA_Data_Changping_20130301-20170228.csv")
    economic_table = pd.read_csv("datasheets/Quarterly_modified.csv")
    plot1 = get_plot(economic_table, 4, 17, pollutant_table)
    ys_PM25 = [x[2][0] for x in plot1]
    ys_PM10 = [x[2][1] for x in plot1]
    ys_SO2 = [x[2][2] for x in plot1]
    ys_NO2 = [x[2][3] for x in plot1]
    ys_CO = [x[2][4] for x in plot1]
    ys_O3 = [x[2][5] for x in plot1]
    xs = [x[1] for x in plot1]

    plt.scatter(xs, ys_PM25,  marker='+', label='PM2.5')
    plt.scatter(xs, ys_PM10, marker='x', label='PM10')
    plt.scatter(xs, ys_SO2, marker='.', label='SO2')
    plt.scatter(xs, ys_NO2, marker='*', label='NO2')
    # plt.scatter(xs, ys_CO, marker='1', label='CO')
    plt.scatter(xs, ys_O3, marker='d', label='O3')
    plt.title("Relationship between Pollutants and Secondary Industry Produce")
    plt.xlabel("Secondary Industry (100 million yuan)")
    plt.ylabel("Pollutant Concentration")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()