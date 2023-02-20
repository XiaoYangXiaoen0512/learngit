class adminfunc:
    def adminFunc(self):
        return '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/ul/div/label[7]/li/div'
class accout:
    def Accout(self):
        return '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/ul/div/label[7]/li/ul/label/div/label[1]/li/div/div'
    def addButton(self):
        return '//*[@id="app"]/div[1]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[2]/button'
    def buildButton(self):
        return 'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > div > form > div > div > div.form-item-wrapper.form-item-wrapper-width12.form-item-wrapper-height1.form-item-wrapper-alignundefined.form-item-wrapper-button-widthundefined.null.edit.FormWidgetSonTable > div > div.table-header > div.table-option-titile > button:nth-child(5)'
    def nameInput(self):
        return '//*[@class="vxe-table--main-wrapper"]/div[2]/table/tbody/tr/td[2]/div/div/div/div/div/div/div/div/div/input'
    def accoutInput(self):
        return '//*[@class="vxe-table--main-wrapper"]/div[2]/table/tbody/tr/td[3]/div/div/div/div/div/div/div/div/div/input'
    def departInput(self):
        return 'body > div.el-dialog__wrapper > div > div.el-dialog__body > div > div > div > form > div > div > div.form-item-wrapper.form-item-wrapper-width12.form-item-wrapper-height1.form-item-wrapper-alignundefined.form-item-wrapper-button-widthundefined.is-selected.edit.FormWidgetSonTable.validate-error > div > div.el-form-item.is-error > div > form > div > div.vxe-table.tid_28.border--full.show--head.fixed--left.t--animat.scroll--x > div.vxe-table--main-wrapper > div.vxe-table--body-wrapper.body--wrapper > table > tbody > tr > td.vxe-body--column.col_35.col--ellipsis > div > div > div > div > div > div > div > div > div > div.selected-block'
    def departSelect(self):
        return '/html/body/div[12]/div/div[2]/div/div[1]/div/div/input'
    def confirmButton(self):
        return '/html/body/div[8]/div/div[2]/div/div[3]/div/button[2]'
    def submitButton(self):
        return '/html/body/div[5]/div/div[3]/div/button[3]'