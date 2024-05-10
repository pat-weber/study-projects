from matplotlib import pyplot as plt


def clean_data(data, columns):
    data.dropna(subset=columns, inplace=True)
    return data


def group_count(data, column1a, column2, column1b=None):
    if column1b is None:
        new_data = data.groupby(column1a)[column2].count().reset_index(name='count')

    else:
        new_data = data.groupby([column1a, column1b])[column2].count().unstack()
    return new_data


def group_sum(data, column1a, column2, column1b=None):
    if column1b is None:
        new_data = data.groupby(column1a)[column2].sum().reset_index(name='count')
        new_data = new_data.sort_values('count', ascending=True)

    else:
        new_data = data.groupby([column1a, column1b])[column2].sum().unstack()
    return new_data


def graph_bar(data, column1, column2):
    plt.figure(figsize=(10, 6))
    return data.plot(kind='bar', x=column1, y=column2, legend=None, rot=45) 
    


def corr(data1, data2):
    correlation = data1.corr(data2)
    return correlation
