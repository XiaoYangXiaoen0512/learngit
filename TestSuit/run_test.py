import pytest
import TestCase.Role_03.maintain_Func
import TestCase.Role_03.alaRecord_Func
import TestCase.Role_03.devView_func
import TestCase.Role_03.runStat_Func
import TestCase.Role_03.submit
import TestCase.Role_03.quit


class Test_test:
    @pytest.mark.appruntest
    def test_006(self):
        alsettext3 = TestCase.Role_03.runStat_Func.runstat()
        functest = '设备查看-运行统计-功能测试'
        print(functest + alsettext3)
        assert alsettext3 == '测试通过'

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest()