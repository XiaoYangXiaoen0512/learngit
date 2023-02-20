# 这是一个示例 Python 脚本。
# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。5
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 ⌘F8 切换断点。
import pytest
import TestCase.Role_03.maintain_Func
import TestCase.Role_03.alaRecord_Func
import TestCase.Role_03.devView_func
import TestCase.Role_03.runStat_Func
import TestCase.Role_03.submit
import TestCase.Role_03.quit


class Test_test:
    @pytest.mark.parametrize('a, username, b, expectedalert1, expectedalert2', [
        ('是', '17752821932', '2', '已发送验证码至尾号1932的手机,请查收', '验证码错误!'),
        ('否', '122', '0', '手机号格式有误,请重新输入', '请勾选同意隐私和用户协议后再登录'),
        ('否', '17752821932', '0', '已发送验证码至尾号1932的手机,请查收', '请勾选同意隐私和用户协议后再登录'),
        ('是', '122', '0', '手机号格式有误,请重新输入', '手机号格式有误,请重新输入'),
        ('是', '17752821932', '1', '已发送验证码至尾号1932的手机,请查收', '验证码长度有误,请检查'),
        ('是', '122', '0', '手机号格式有误,请重新输入', '手机号格式有误,请重新输入'),
        ('是', '13548937820', '0', '您不属于智慧电梯用户，无法登录', '验证码长度有误,请检查'),
    ]
                               )
    def test_001(self, a, username, b, expectedalert1, expectedalert2):
        alerttext = TestCase.Role_03.submit.submittest(a, username, b)
        expectedalert = [expectedalert1, expectedalert2]
        assert alerttext == expectedalert

    @pytest.mark.appsubmittest
    def test_002(self):
        TestCase.Role_03.submit.submit()

    @pytest.mark.appmaintest
    def test_003(self):
        alsettext = TestCase.Role_03.maintain_Func.applytest1()
        functest = '维保管理页面-功能测试'
        print(functest + alsettext)
        assert alsettext == '测试通过'

    @pytest.mark.appalatest
    def test_004(self):
        alsettext1 = TestCase.Role_03.alaRecord_Func.alarecord()
        functest = '报警记录-功能测试'
        print(functest + alsettext1)
        assert alsettext1 == '测试通过'

    @pytest.mark.appdevtest
    def test_005(self):
        alsettext2 = TestCase.Role_03.devView_func.devview()
        functest = '设备查看-维修保养-功能测试'
        print(functest + alsettext2)
        assert alsettext2 == '测试通过'

    @pytest.mark.appruntest
    def test_006(self):
        alsettext3 = TestCase.Role_03.runStat_Func.runstat()
        functest = '设备查看-运行统计-功能测试'
        print(functest + alsettext3)
        assert alsettext3 == '测试通过'

    @pytest.mark.appalatest
    def test_007(self):
        alsettext3 = TestCase.Role_03.alaRecord_Func.alarecordtest2()
        assert alsettext3 == '测试通过'

    @pytest.mark.appappdevtest
    def test_007(self):
        alsettext3 = TestCase.Role_03.devView_func.devviewtest()
        assert alsettext3 == ['测试通过', '测试通过']

    # @pytest.mark.apptest
    # def test_007(self):
    #     TestCase.Role_03.quit.appquit()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest.main()
