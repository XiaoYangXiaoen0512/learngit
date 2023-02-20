import pytest
import TestCase.Role_03.maintain_Func
import TestCase.Role_03.alaRecord_Func
import TestCase.Role_03.devView_func
import TestCase.Role_03.runStat_Func
import TestCase.Role_03.submit
import TestCase.Role_03.quit


class Test_test:
    @pytest.mark.appalatest
    def test_004(self):
        alsettext1 = TestCase.Role_03.alaRecord_Func.alarecord()
        functest = '报警记录-功能测试'
        print(functest + alsettext1)
        assert alsettext1 == '测试通过'


    @pytest.mark.appalatest
    def test_007(self):
        alsettext3 = TestCase.Role_03.alaRecord_Func.alarecordtest2()
        assert alsettext3 == '测试通过'


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest()