import pytest
import TestCase.Role_03.maintain_Func
import TestCase.Role_03.alaRecord_Func
import TestCase.Role_03.devView_func
import TestCase.Role_03.runStat_Func
import TestCase.Role_03.submit
import TestCase.Role_03.quit

class Test_test:
    @pytest.mark.appmaintest
    def test_003(self):
        alsettext = TestCase.Role_03.maintain_Func.apply()
        functest = '维保管理页面-功能测试'
        print(functest + alsettext)
        assert alsettext == '测试通过'


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest()