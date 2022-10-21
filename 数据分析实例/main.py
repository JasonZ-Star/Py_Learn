# Owner Feng
# Time 2022/10/21 10:19
from file_define import FileReader, TextReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


text_file_reader = TextReader('data/2011年1月销售数据.txt')
json_file_reader = JsonFileReader('data/2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

all_data: list[Record] = jan_data + feb_data

# 开始进行数据处理, 使用字典
data_dict = {}
for record in all_data:
    if record.data in data_dict.keys():
        data_dict[record.data] += record.money
    else:
        data_dict[record.data] = record.money

# 可视化图表开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('consumption', list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title='everyday consumption')
)
bar.render('everyday consumption.html')


