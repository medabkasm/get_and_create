from types import GeneratorType
CRED    = "\33[31m"
CGREEN  = "\33[32m"
CYELLOW = '\33[33m'
CEND = "\033[0m"

class Save:

    def __new__(Save,data):
        if not isinstance(data, GeneratorType):
            print(CYELLOW+"Warning :: the data must be with type generator."+CEND)
            print(CRED+"this object will be a NoneType object."+CEND)
            return None
        else:
            return object.__new__(Save)

    def __init__(self,data):
        self.data = data

    def to_json(self,fileName = ''):
        import json
        fileName = self.__check_fileName(fileName,"json_data.json","json")
        try:
            if isinstance(self.data , GeneratorType):
                    self.data = list(self.data)
            with open(fileName,"w") as file:
                json.dump(self.data,file)
                print(CGREEN+"{} was created successfuly.".format(fileName)+CEND)
                return True
        except Exception as err:
            print(CRED+"Error :: in to_json : {}".format(str(err))+CEND)
            return False

    def to_csv(self,fileName = ''):
        import csv
        fileName = self.__check_fileName(fileName,"csv_data.csv","csv")
        try:
            if isinstance(self.data,GeneratorType):
                self.data = list(self.data)
            with open(fileName,"w") as file:
                csvWriter = csv.writer(file, delimiter='|')
                dataRow = ["title","link","image","price","description","date"]
                csvWriter.writerow(dataRow)
                for page in self.data:
                    for item in page:
                        data = [ item["title"] , item["link"] , item["image"] , item["price"] , item["description"] , item["date"] ]
                        csvWriter.writerow(data)
                print(CGREEN+"{} was created successfuly.".format(fileName)+CEND)
                return True
        except Exception as err:
            print(CRED+"Error :: in to_csv : {}".format(str(err))+CEND)
            return False


    def __check_fileName(self,fileName,setedFileName,extension):
        if not fileName:
            fileName = setedFileName
        else:
            if not self.__check_extension(fileName,extension):
                fileName = fileName + "." + extension
        return fileName

    def __check_extension(self,fileName,extension):
        fileExtension = fileName.split(".")[-1]
        if extension == fileExtension.lower():
            return True
        return False
