########################################################################
#     This code can be edit and extend to make it better and robust
#
#  By      Ayodeji Makinde          Thank you
########################################################################


from dbfread import DBF
from pandas import DataFrame
from glob import glob
from matplotlib.pyplot import plot, show, xlabel, ylabel, legend

# The Iteration start from 1 instead of 0... this is because 0 has been used at the dbfile_data_header() to get the Header name with the data in it
def dbfile_data_frame():
    for i in range(1,60):
        for dbf_file in glob(r'data\Ras_{}.dbf'.format(i)):
            with DBF(dbf_file) as dbf:
                frame = DataFrame(iter(dbf))

                dataframe_csv(frame)


# This was used in order to capture the header name. However, arcpy library could have been the best to use but due to
# license issues with arcgis I decided to do it manually without affecting anything
def dbfile_data_header():
    for dbf_file in glob(r'data\Ras_0.dbf'):
        with DBF(dbf_file) as dbf:
            frame = DataFrame(iter(dbf))

            frame.to_csv('output.csv', sep=',', header=True, mode='a', index=False)


#def month_to_year(data_frame):
#    data_frame = data_frame['FILE']
#    yearly = []
#    for x in range(0, len(data_frame), 12):
#        yearly.append(sum(data_frame[x:x+12])/12)
#
#    return yearly


def dataframe_csv(frame):
    return frame.to_csv('output.csv', sep=',', header=False, mode='a', index=False)


def main():
    print('==================================')
    data_header = dbfile_data_header()
    data_frame = dbfile_data_frame()
    print(data_header)
    print(data_frame)
    print('==================================')
    #month_year = month_to_year(data_frame)
    #print(month_year)


if __name__ == "__main__":
    main()