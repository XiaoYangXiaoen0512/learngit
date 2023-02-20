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
    ]
                               )
    def test_001(self, a, username, b, expectedalert1, expectedalert2):
        alerttext = TestCase.Role_03.submit.submittest(a, username, b)
        expectedalert = [expectedalert1, expectedalert2]
        assert alerttext == expectedalert

    @pytest.mark.appsubmittest
    def test_002(self):
        TestCase.Role_03.submit.submit()
# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    pytest()