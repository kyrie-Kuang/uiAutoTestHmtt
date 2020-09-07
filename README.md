# uiAutoTestHmtt
UI自动化测试，执行run文件，生成html报告，使用PO模型分层架构（hm实例）

软件架构
软件架构说明
base： 存放selenium定位方法

data： 存放参数化数据

page： 存放页面元素操作方法

report： 存放测试报告

test_case： 存放通过unittest实现业务流程方法

tools： 存放获取driver，获取参数化数据文件


使用说明
base文件编写selenium定位元素方法

page文件编写页面元素操作方法

data编写参数化yaml文件

tools编写获取dirver和获取参数化文件

test_case文件编写unittest业务流程实现方法

执行run_case文件，在report查看生产的HTML报告

