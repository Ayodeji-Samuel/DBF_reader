########################################################################
# Babe I hope the code should be able to do some justice
# to your dbf files. I make it simple as possible   love you.   Ayodeji
########################################################################

from dbfread import DBF
from pandas import DataFrame
from glob import glob
from matplotlib.pyplot import plot, show, xlabel, ylabel, legend


def dbfile_data_frame():
    for i in range(1,60):
        for dbf_file in glob(r'data\Ras_{}.dbf'.format(i)): # Babe you can extend the pathname from (r'*.dbf') as (r'C:\Anna\*.dbf')...
            with DBF(dbf_file) as dbf:
                frame = DataFrame(iter(dbf))

                dataframe_csv(frame)


def dbfile_data_header():
    for dbf_file in glob(r'data\Ras_59.dbf'): # Babe you can extend the pathname as (r'C:\Anna\*.dbf')...
        with DBF(dbf_file) as dbf:
            frame = DataFrame(iter(dbf))

            frame.to_csv('output.csv', sep=',', header=True, mode='a', index=False)


#def month_to_year(data_frame):
#    data_frame = data_frame['FILE']  # Babe you can replace data_frame['FILE'] with data_frame['your_column_name'] in order to filter the Column you want
#    yearly = []
#    for x in range(0, len(data_frame), 12):
#        yearly.append(sum(data_frame[x:x+12])/12)
#
#    return yearly


#def plot_graph(y):
#    x = range(len(y))
#    plot(x, y, marker='o')
#    xlabel('Year')
#    ylabel('Rainfall')
#    legend(('Rainfall', 'Year'))
#    show()

# Babe I use this to convert the dataframe to CSV...then you can open the CSV in Excel if you like...then off you go
def dataframe_csv(frame):
    return frame.to_csv('output.csv', sep=',', header=False, mode='a', index=False)


def main():
    print('==================================')
    data_header = dbfile_data_header()
    #data_frame = dbfile_data_frame()
    print(data_header)
    #print(data_frame)
    ##print(data_frame['COLUMN_NAME'])   # Babe you can replace print(frame) with print(frame['column_name']) in order to filter the Column you want
    #dataframe_csv(data_frame)
    print('==================================')
    #month_year = month_to_year(data_frame)
    #print(month_year)
    #plot_graph(month_year)


if __name__ == "__main__":
    main()