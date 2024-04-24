#dependencies
from zipfile import *
import pandas as pd


class solution:
    def __init__(self):
        pass

    def fileReader(self,name:str) -> int: #1st task
        try :
            with open(name,'r') as file:
                data=file.read().strip().split()
                return len(data)
        except FileNotFoundError:
            print("Enter the correct filename.")
    
    def zipWorker(self,name:str): #2nd task
        try:
            with ZipFile(name) as zipFile:
                with open('hra_resultant_data.csv','a') as outputFile:
                    flag = True
                    for i in zipFile.namelist():
                        if "HRA" in i and i.endswith(".csv"):
                            with zipFile.open(i,'r') as inputFile:
                                if flag:
                                    start = 0
                                    flag = False
                                else:
                                    start = 1
                                dataset = inputFile.read().decode().strip().split("\n")[start:]
                                for data in dataset:
                                    outputFile.write(data+"\n")


                    return self.zipWorkerHelper(outputFile.name)
        except Exception as e:
            print(e)

    def zipWorkerHelper(self,name): #task 3 and 4
        df = pd.read_csv(name)
        df = df[["Age","Gender","JobRole"]]
        df.to_csv('job_roles.csv.zip',index=False,compression='zip')

    def lastLinesofFile(self,name,n): #task 5
        try:
            with open(name,'r') as file:
                lines = file.read().strip().split('\n')
                if len(lines) < n:
                    raise ValueError
                else:
                    for i in lines[-n:]:
                        print(i)
        except ValueError:
            print(f"You've entered n: {n} but there are only {len(lines)} lines in the file.")
        except FileNotFoundError:
            print("File dosen't exits.")

    def wordOccurences(self,filename,word): #task 6
        try:
            with open(filename,'r') as file:
                lines = file.read().strip().split('\n')
                occur = 0
                for i in lines:
                    occur += i.split().count(word)
            return occur
        except FileNotFoundError:
            print("File dosen't exists.")

    def sizeOfImage(self,imgName): #task 7
        try:
            with open(imgName,'rb') as img:
                return len(img.read())
        except FileNotFoundError:
            print("Write correct name.")
        except IOError:
            print("Not able to process file.")

    def fileWriter(self,filename='log.txt'): #task 8
        try :
            data = input(f"Everything that you'll type will be appended into the {filename} file.\nType: ")
            with open(filename,'a') as file:
                file.write(data)
        
        except FileNotFoundError:
            print('Invalid Filename.')



if __name__ == "__main__" :
    sol = solution()
    '''
        From here You can try by calling the member functions.
    '''
    sol.zipWorker('test_data.zip')