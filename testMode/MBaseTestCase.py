__author__ = 'Administrator'

from schematics.models import Model
from schematics.types import StringType,IntType
from schematics.types.compound import ListType,MultiType



class BaseTestCase(Model):
    element_type = StringType() #操作类型。比如点击，下拉，拖动等等，对应common
    element_info = StringType() # (查找类型：name/id/xpah)
    operate_type = StringType() #具体的详情,如xpath:“/android.widget.TextView[contains(@text,'Add note'")）,id等
    msg = StringType() # 输入的内容
    find_type = StringType()

# 用例的基本信息
class getTempCase(Model):
    test_id = StringType()
    test_intr = StringType()
    test_name = StringType()
    test_result =StringType()
    test_reason = StringType()
    test_module = StringType()
