各文件夹含义：
1. training:训练数据，包含10月10日及以前数据，数据格式和官方提供datasets中的training文件夹一致

2. testing_phase1:预测数据，包含10月11日至10月17日每天6点-8点；15点到17点数据，数据格式和官方提供datasets中的testing_phase1文件夹一致

3.testing_actual_results:所需预测时段的真实统计数据，包含10月11日至10月17日每天8点到10点；17点到19点的真实统计数据，两个文件分别对应travel time和volume的预测

4.testing_prediction:用于放入预测结果，目前文件夹状态为空，travel time的预测结果请命名为travel_time.csv，volume的预测结果请命名为volume.csv，格式按照官方要求格式

5.travel_time_evaluation.py：用于计算travel time的预测指标MAPE的文件

6.volume_evaluation.py:用于计算volume的预测指标MAPE的文件

****************************************************************************************

使用方式
1. 将所需预测的文件travel_time.csv(或volume.csv)放入文件夹testing_prediction中

2. 运行文件travel_time_evaluation.py(或volume.py)，无需参数

3. 代码输出MAPE值