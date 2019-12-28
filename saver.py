CRED    = "\33[31m"
CGREEN  = "\33[32m"
CYELLOW = '\33[33m'
CEND = "\033[0m"

class Save:

    def __init__(self,data):
        from types import GeneratorType
        if not isinstance(data,GeneratorType):
            print(CYELLOW+"Warning :: the data must be with type generator for more efficiency."+CEND)

        self.data = data

    def to_json(self,fileName = ''):
        import json
        if not fileName:
            fileName = "json_data.json"
        if not self.__check_extension(fileName,"json"):
            fileName = fileName + ".json"
        try:
            self.data = list(self.data)
            with open(fileName,"w") as file:
                json.dump(self.data,file)
                print(CGREEN+"file saved successfuly with name : {}.".format(fileName)+CEND)
                return True
        except Exception as err:
            print(CRED+"Error :: in to_json : {}".format(str(err))+CEND)
            return False




    def __check_extension(self,fileName,extension):
        if extension == "json":
            fileName ,fileExtension = fileName.split(".")[1],fileName.split(".")[-1]
            if extension == fileExtension.lower():
                return True
            else:
                return False
