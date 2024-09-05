DB_PATH = "/home/yulduz/P25/TgCloneNew/TgCLone/db/"


class DbService:
    def objects(self):
        file_name = self.__class__.__name__.lower() + "s.txt"
        objects = []
        with open(DB_PATH + file_name, 'r') as f:
            for i in f.readlines():
                objects.append(self.__class__(*list(map(lambda x: x.strip(), i.split(',')))))
        return objects

    def write(self, data: list):
        file_name = self.__class__.__name__.lower() + "s.txt"
        write_data = ""
        for i in data:
            write_data += ",".join(map(str , i.__dict__.values()))+"\n"
        with open(DB_PATH + file_name, 'w') as f:
            return f.write(write_data)
