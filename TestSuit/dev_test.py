import pytest
import TestCase.Role_03.maintain_Func
import TestCase.Role_03.alaRecord_Func
import TestCase.Role_03.devView_func
import TestCase.Role_03.runStat_Func
import TestCase.Role_03.submit
import TestCase.Role_03.quit


class Test_test:
    @pytest.mark.appdevtest
    def test_005(self):
        alsettext2 = TestCase.Role_03.devView_func.devview()
        functest = '设备查看-维修保养-功能测试'
        print(functest + alsettext2)
        assert alsettext2 == '测试通过'


    @pytest.mark.appappdevtest
    def test_007(self):
        alsettext3 = TestCase.Role_03.devView_func.devviewtest()
        assert alsettext3 == ['测试通过', '测试通过']


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest()