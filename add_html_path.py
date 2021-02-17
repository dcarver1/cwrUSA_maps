
import csv
import pandas as pd
import glob

# the location of the source data
CSV_FILE="allMetricData2020-03-20_forfigsonly.csv"
# path and regular expression
PATH = "./compiledSummaryDocs/"
MATCH="*/*.html"
# the name of the new path column to be added to the file
PATH_COL="file_path"

def main(csv_file_name,path,match,path_col):
    '''
used to generate a list of html paths
    :param csv_file:
    :param path:
    :return:
    '''
    # get a list of files to match against
    file_list = get_file_list(path+match)
    # print(file_list)

    # open the csv
    csv_data = get_csv(csv_file_name)
    csv_data[path_col] = ""

    # iterate over rows and search for matching html file
    for index, row in csv_data.iterrows():
        # construct a path to match the files beginning
        match_text= path+row['Genus']+"/"+row['Taxon']+"_"
        for file_name in file_list:
            # looking for match_text in file_name
            if file_name.startswith(match_text):
                # save the file path to the row
                csv_data.loc[index, path_col] = file_name

    # update original csv
    csv_data.to_csv(csv_file_name,index=False)

    print("COMPLETE")




# step 1. open a csv file
def get_csv(file_name):
    '''
    :param file_name: the csv file to open
    :return: csv_reader for file
    '''
    file_data = pd.read_csv(file_name)

    return file_data


def get_file_list(path_match):
    '''
    :param path_match: the path regular expression to search for files
    :return: a list of files with extension
    '''
    # takes a file path and generates a list of the files

    return glob.glob(path_match)


# step 2.
def find_matching_path(file_name):
    '''
    :param file_name: the start of the file to be searched for
    :return: the path of the matching html file
    '''

main(CSV_FILE,PATH,MATCH,PATH_COL)