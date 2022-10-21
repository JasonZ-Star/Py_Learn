# Owner Feng
# Time 2022/10/21 10:18
import json
from data_define import Record


class FileReader():
    def read_data(self) -> list[Record]:
        pass


class TextReader(FileReader):

    def __init__(self, path):
        self.path = path

    # 重写方法
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding='UTF-8')

        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()  # 消除换行符
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1],
                            int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:

        f = open(self.path, "r", encoding='UTF-8')
        record_list: list[Record] = []
        for line in f.readlines():
            data_dic = json.loads(line)
            record = Record(data_dic['date'], data_dic['order_id'],
                            data_dic['money'], data_dic['province'])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text = TextReader('data/2011年1月销售数据.txt')
    text1 = JsonFileReader('data/2011年2月销售数据JSON.txt')
    list1 = text.read_data()
    list2 = text1.read_data()

    for l in list1:
        print(l)

    for l in list2:
        print(l)
