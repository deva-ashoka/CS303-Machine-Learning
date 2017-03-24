# Name: Deva Surya Vivek
# Assignment 2
# CS303: Introduction to Machine Learning

import csv
import sys
import numpy as np
import scipy.io
import os


# delimiter in the input file is tab. change the delimiter accordingly

def convert_txt_to_csv(txtFile, csvFile):
    reader = csv.reader(open(txtFile, "rb"), delimiter='\t')
    outputFile = csv.writer(open(csvFile, 'wb'))
    outputFile.writerows(reader)


def convert_csv_to_txt(csvFile, txtFile):
    reader = csv.reader(open(csvFile, 'rb'))
    with open(txtFile, 'wb') as outputFile:
        writer = csv.writer(outputFile, delimiter='\t')
        writer.writerows(reader)


def convert_csv_to_mat(csvFile, matFile):
    dataArray = []
    reader = csv.reader(open(csvFile))
    for eachRow in reader:
        data = [float(eachData) for eachData in eachRow]
        dataArray.append(data)
    writeData = np.array(dataArray)
    scipy.io.savemat(matFile, {'data': writeData})


def convert_mat_to_csv(matFile, csvFile):
    data = scipy.io.loadmat(matFile)
    for eachRow in data:
        if '__' not in eachRow:
            if 'readme' not in eachRow:
                np.savetxt((csvFile), data[eachRow], delimiter='\t')


def convert_csv_to_arff(csvFile, arffFile):
    reader = csv.reader(open(csvFile, 'rb'))
    with open(arffFile, 'wb') as outputFile:
        writer = csv.writer(outputFile, delimiter='\t')
        writer.writerows(reader)



def convert_arff_to_csv(arffFile, csvFile):
    reader = csv.reader(open(arffFile, "rb"), delimiter='\t')
    outputFile = csv.writer(open(csvFile, 'wb'))
    outputFile.writerows(reader)


# -------------------------------------


inputFile = str(sys.argv[1])
inputExt = str(sys.argv[2])
outputExt = str(sys.argv[3])

inputFileSplit = inputFile.split('.')
outputFile = inputFileSplit[0] + "." + outputExt

if (inputExt == "txt" and outputExt == "csv"):
    convert_txt_to_csv(inputFile, outputFile)
    print("Done!")

if (inputExt == "csv" and outputExt == "txt"):
    convert_csv_to_txt(inputFile, outputFile)
    print("Done!")

if (inputExt == "csv" and outputExt == "mat"):
    convert_csv_to_mat(inputFile, outputFile)
    print("Done!")

if (inputExt == "mat" and outputExt == "csv"):
    convert_mat_to_csv(inputFile, outputFile)
    print("Done!")

if (inputExt == "csv" and outputExt == "arff"):
    convert_csv_to_arff(inputFile, outputFile)
    print("Done!")

if (inputExt == "arff" and outputExt == "csv"):
    convert_arff_to_csv(inputFile, outputFile)
    print("Done!")

if (inputExt == "txt" and outputExt == "mat"):
    convert_txt_to_csv(inputFile, "temp" + inputFileSplit[0] + ".csv")
    convert_csv_to_mat("temp" + inputFileSplit[0] + ".csv", outputFile)
    os.remove("temp" + inputFileSplit[0] + ".csv")
    print("Done!")

if (inputExt == "mat" and outputExt == "txt"):
    convert_mat_to_csv(inputFile, "temp" + inputFileSplit[0] + ".csv")
    convert_csv_to_txt("temp" + inputFileSplit[0] + ".csv", outputFile)
    os.remove("temp" + inputFileSplit[0] + ".csv")
    print("Done!")

if (inputExt == "txt" and outputExt == "arff"):
    convert_txt_to_csv(inputFile, "temp" + inputFileSplit[0] + ".csv")
    convert_csv_to_arff("temp" + inputFileSplit[0] + ".csv", outputFile)
    os.remove("temp" + inputFileSplit[0] + ".csv")
    print("Done!")

if (inputExt == "arff" and outputExt == "txt"):
    convert_arff_to_csv(inputFile, "temp" + inputFileSplit[0] + ".csv")
    convert_csv_to_txt("temp" + inputFileSplit[0] + ".csv", outputFile)
    os.remove("temp" + inputFileSplit[0] + ".csv")
    print("Done!")

if (inputExt == "mat" and outputExt == "arff"):
    convert_mat_to_csv(inputFile, "temp" + inputFileSplit[0] + ".csv")
    convert_csv_to_arff("temp" + inputFileSplit[0] + ".csv", outputFile)
    os.remove("temp" + inputFileSplit[0] + ".csv")
    print("Done!")

if (inputExt == "arff" and outputExt == "mat"):
    convert_arff_to_csv(inputFile, "temp" + inputFileSplit[0] + ".csv")
    convert_csv_to_mat("temp" + inputFileSplit[0] + ".csv", outputFile)
    os.remove("temp" + inputFileSplit[0] + ".csv")
    print("Done!")
