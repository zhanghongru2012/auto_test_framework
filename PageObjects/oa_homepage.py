# coding=utf-8
from Base.base_page import BasePage
import time


# /login    登录页面
class LoginHomePage(BasePage):
    # 输入用户名
    input_username = "id=>user"
    input_password = "id=>password"
    button_login = "xpath=>/html/body/div[2]/div/div[2]/div/form/div/div[3]/button"
    user_text = "class_name=>account"

    def input_user(self, text):
        self.send_keys(self.input_username, text)

    def input_passwd(self, text):
        self.send_keys(self.input_password, text)

    def submit_login(self):
        self.click(self.button_login)

    def get_user(self):
        return self.get_text(self.user_text)

    def submit(self):
        pass


# /index
class IndexHomePage(BasePage):
    # 首页用户信息-鼠标悬停 .perform()
    user_info = 'class_name=>account'
    # 退出登录按钮
    button_quit = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/ul/li[9]/button'
    # 用户信息中的我的工单入口 worksheet
    work_sheet = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/ul/li[7]/span[2]'
    max_work_sheet = 'xpath=>/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    # 工单表单嵌套
    frame_work_sheet = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    # 导航 - 收发文管理
    recv_send_manager = \
        'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[2]/div/span[3]/i'
    # 导航 - 收发文管理 - 收文办理
    recv_manager = \
        'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[2]/ul/li[1]/div/span[2]'
    # 查看user_info中我的工单
    to_do = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/ul/li[7]/span[2]'
    # 我的工单 - 关闭按钮
    exit_to_do = 'xpath=>/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[3]'
    def click_recv_send_manager(self):
        self.click(self.recv_send_manager)

    # 点击收文办理
    def click_recv_manager(self):
        self.click(self.recv_manager)

    # 鼠标hover到用户信息位置
    def hover_user_info(self):
        self.move_to_element(self.user_info)

    # 点击退出登录按钮
    def click_button_quit(self):
        self.click(self.button_quit)

    # 点击user_info中的我的工单
    def click_to_do(self):
        self.click(self.to_do)

    # 点击我的工单嵌套关闭
    def click_exit_to_do(self):
        self.click(self.exit_to_do)


# 收文办理页
class RecvPage(BasePage):
    # iframe
    recv_iframe = 'xpath=>/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe'
    # 正文按钮
    button_body = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[1]'
    # 附件按钮
    button_attachment = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[2]'
    # 保存按钮
    button_save = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[3]'
    # 传递按钮
    button_pass = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[4]'
    # 打印按钮
    button_print = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[2]'
    # 选择工单名头
    # select_head = 'id=>institutionId'
    select_head = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[1]/select'
    # 输入来文单位
    # input_recv_comp = 'id=>comeOrgName'
    input_recv_comp = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[1]/td[4]/textarea'
    # 输入文件编号
    # input_recv_sort = 'id=>sortNumber'
    input_recv_sort = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[1]/td[6]/textarea'
    # 输入来文份数
    # input_recv_num = 'id=>comNum'
    input_recv_num = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[1]/td[8]/textarea'
    # 输入文件名称
    input_file_name = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[2]/td[2]/div/textarea'
    # 输入拟办意见
    # input_comment = 'id=>proposedComments'
    input_comment = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[4]/td[2]/div[1]/pre/textarea'
    # 上传附件 - input
    upload_file = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[3]/td[2]/input'
    # 自动签名按钮
    button_signature = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[4]/td[2]/div[2]'
    # 点击保存后的知道了按钮
    button_saved_known = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 点击传递后的正文为空是否传递 确定按钮
    button_pass_known = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]'
    # 选择传递人员frame
    choose_member_frame = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    # 下一环节- 主任
    liushaodong = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[3]/ul/li'
    # 选择传递人员 - 确定
    button_choose_member_ok = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[4]/button'
    # 选择人员确定后二次确认执行传递
    button_pass_again_ok = 'xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]'
    # 选择人员确定后二次确认执行传递后  传递成功后的知道了按钮
    button_pass_again_ok_known = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 选择人员确定后二次确认执行传递后  传递结果 '传递成功'
    pass_result = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p'

    # 收文办理iframe
    def switch_to_recv_iframe(self):
        self.switch_to_frame(self.recv_iframe)

    # 输入来文单位
    def send_keys_input_recv_comp(self, text):
        self.send_keys(self.input_recv_comp, text)

    # 输入文件编号
    def send_keys_input_recv_sort(self, text):
        self.send_keys(self.input_recv_sort, text)

    # 输入来文份数
    def send_keys_input_recv_num(self, text):
        self.send_keys(self.input_recv_num, text)

    # 输入文件名称
    def send_keys_input_file_name(self, text):
        self.send_keys(self.input_file_name, text)

    # 输入拟办意见
    def send_keys_input_comment(self, text):
        self.send_keys(self.input_comment, text)

    # 上传附件
    def send_keys_upload_file(self, text):
        self.send_keys(self.upload_file, text)

    # 点击自动签名
    def click_button_signature(self):
        self.click(self.button_signature)

    # 点击保存
    def click_button_save(self):
        self.click(self.button_save)

    # 点击传递
    def click_button_pass(self):
        self.click(self.button_pass)

    def switch_default_frame(self):
        self.switch_to_default_content()

    # 保存后点击知道了按钮
    def click_button_saved_known(self):
        self.click(self.button_saved_known)

    # 传递后点击知道了按钮
    def click_button_pass_known(self):
        self.click(self.button_pass_known)

    # 切入传递人员选择嵌套
    def switch_to_choose_member_frame(self):
        self.switch_to_frame(self.choose_member_frame)

    # 下一环节 - 主任 - 选择刘绍东
    def click_liushaodong(self):
        self.click(self.liushaodong)

    # 选择传递人员后点击确定按钮
    def click_button_choose_member_ok(self):
        self.click(self.button_choose_member_ok)

    # 下一环节 - 主任 - 选择刘绍东 - 确定 - 二次确认
    def click_button_pass_again_ok(self):
        self.click(self.button_pass_again_ok)

    # 获取传递结果提示信息
    def get_pass_result_text(self):
        self.get_attribute(self.pass_result)

    # 点击传递成功提示框的知道了
    def click_button_pass_again_ok_known(self):
        self.click(self.button_pass_again_ok_known)


class LSDToDoHomePage(BasePage):
    # 我的工单iframe
    frame_to_do = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    # 我的工单 - 最大化按钮
    max_to_do_frame = 'xpath=>/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    # 工单号输入框
    to_do_num = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[1]/div/input'
    # 工单类型输入
    to_do_type = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'
    # 工单任务名称输入
    to_do_name = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input'
    # 点击工单中的处理按钮
    button_to_do_solve = \
        'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[9]/div/a[1]/span'
    # 处理嵌套
    frame_task_deal = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'
    # 进入工单详情嵌套
    frame_task_detail = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div/div/iframe'
    # 工单详情嵌套最大化按钮
    button_max_frame_task_detail = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    # 工单详情 - 拟办意见输入框
    input_comment = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[4]/td[2]/div[1]/div/pre/textarea'
    # 正文按钮
    button_body = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[1]'
    # 附件按钮
    button_attachment = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[2]'
    # 保存按钮
    button_save = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[3]'
    # 传递按钮
    button_pass = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[4]'
    # 打印按钮
    button_print = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[5]'
    # 自动签名按钮
    button_signature = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[4]/td[2]/div[2]'
    # 点击保存后的知道了按钮
    button_saved_known = 'xpath=>/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 选择传递人员frame
    choose_member_frame = 'xpath=>/html/body/div[1]/div/div[3]/div[11]/div[2]/iframe'
    # 下一环节- 办理审签 - 张振博
    zhangzhenbo = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[3]/ul[1]/li[1]/div[2]'
    # 选择传递人员 - 确定
    button_choose_member_ok = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[4]/button'
    # 选择人员确定后二次确认执行传递
    button_pass_again_ok = 'xpath=>/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]'
    # 选择人员确定后二次确认执行传递后  传递成功后的知道了按钮
    button_pass_again_ok_known = 'xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 选择人员确定后二次确认执行传递后  传递结果 '传递成功'
    pass_result = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p'

    # 切入我的工单嵌套
    def switch_to_to_do_frame(self):
        self.switch_to_frame(self.frame_to_do)
    # 点击我的工单的最大化按钮
    def click_max_to_do_frame(self):
        self.click(self.max_to_do_frame)
    # 切出嵌套 - 公共
    def switch_default_frame(self):
        self.switch_to_default_content()
    # 点击我的工单列表中处理按钮
    def click_button_to_do_solve(self):
        self.click(self.button_to_do_solve)
    # 点击工单详情最大化按钮
    def click_button_max_frame_task_detail(self):
        self.click(self.button_max_frame_task_detail)
    # 切入工单详情嵌套
    def switch_frame_task_deal(self):
        self.switch_to_frame(self.frame_task_deal)
    def switch_frame_task_detail(self):
        self.switch_to_frame(self.frame_task_detail)
    # 输入拟办意见
    def send_keys_input_comment(self, text):
        self.send_keys(self.input_comment, text)
    # 点击自动签名
    def click_button_signature(self):
        self.click(self.button_signature)
    # 点击保存
    def click_button_save(self):
        self.click(self.button_save)
    # 点击传递
    def click_button_pass(self):
        self.click(self.button_pass)
    # 保存后点击知道了按钮
    def click_button_saved_known(self):
        self.click(self.button_saved_known)
    # 切入传递人员选择嵌套
    def switch_to_choose_member_frame(self):
        self.switch_to_frame(self.choose_member_frame)
    # 下一环节 - 办理审签 - 选择张振博
    def click_zhangzhenbo(self):
        self.click(self.zhangzhenbo)
    # 选择传递人员后点击确定按钮
    def click_button_choose_member_ok(self):
        self.click(self.button_choose_member_ok)
    # 下一环节 - 办理审签 - 选择张振博 - 确定 - 二次确认
    def click_button_pass_again_ok(self):
        self.click(self.button_pass_again_ok)
    # 获取传递结果提示信息
    def get_pass_result_text(self):
        self.get_attribute(self.pass_result)
    # 点击传递成功提示框的知道了
    def click_button_pass_again_ok_known(self):
        self.click(self.button_pass_again_ok_known)


class ZZBToDoHomePage(BasePage):
    # 我的工单iframe
    frame_to_do = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    # 我的工单 - 最大化按钮
    max_to_do_frame = 'xpath=>/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    # 工单号输入框
    to_do_num = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[1]/div/input'
    # 工单类型输入
    to_do_type = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'
    # 工单任务名称输入
    to_do_name = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input'
    # 点击工单中的处理按钮
    button_to_do_solve = \
        'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[9]/div/a[1]/span'
    # 处理嵌套
    frame_task_deal = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'
    # 进入工单详情嵌套
    frame_task_detail = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div/div/iframe'
    # 工单详情嵌套最大化按钮
    button_max_frame_task_detail = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    # 工单详情 - 拟办意见输入框
    input_comment = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[4]/td[2]/div[1]/div/pre/textarea'
    # 正文按钮
    button_body = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[1]'
    # 附件按钮
    button_attachment = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[2]'
    # 保存按钮
    button_save = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[3]'
    # 传递按钮
    button_pass = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[4]'
    # 打印按钮
    button_print = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[5]'
    # 自动签名按钮
    button_signature = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[4]/td[2]/div[2]'
    # 点击保存后的知道了按钮
    button_saved_known = 'xpath=>/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 点击传递后是否之星传递点击是
    button_pass_yes = 'xpath=>/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]'
    # 传递成功后的知道了按钮
    button_pass_again_ok_known = 'xpath=>/html/body' \
                                 '/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 选择人员确定后二次确认执行传递后  传递结果 '传递成功'
    pass_result = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p'

    # 切入我的工单嵌套
    def switch_to_to_do_frame(self):
        self.switch_to_frame(self.frame_to_do)
    # 点击我的工单的最大化按钮
    def click_max_to_do_frame(self):
        self.click(self.max_to_do_frame)
    # 切出嵌套 - 公共
    def switch_default_frame(self):
        self.switch_to_default_content()
    # 点击我的工单列表中处理按钮
    def click_button_to_do_solve(self):
        self.click(self.button_to_do_solve)
    # 点击工单详情最大化按钮
    def click_button_max_frame_task_detail(self):
        self.click(self.button_max_frame_task_detail)
    # 切入工单详情嵌套
    def switch_frame_task_deal(self):
        self.switch_to_frame(self.frame_task_deal)
    def switch_frame_task_detail(self):
        self.switch_to_frame(self.frame_task_detail)
    # 输入拟办意见
    def send_keys_input_comment(self, text):
        self.send_keys(self.input_comment, text)
    # 点击自动签名
    def click_button_signature(self):
        self.click(self.button_signature)
    # 点击保存
    def click_button_save(self):
        self.click(self.button_save)
    # 点击传递
    def click_button_pass(self):
        self.click(self.button_pass)
    # 保存后点击知道了按钮
    def click_button_saved_known(self):
        self.click(self.button_saved_known)
    # 点击是否进行传递点击是
    def click_button_pass_yes(self):
        self.click(self.button_pass_yes)
    # 获取传递结果提示信息
    def get_pass_result_text(self):
        self.get_attribute(self.pass_result)
    # 点击传递成功提示框的知道了
    def click_button_pass_again_ok_known(self):
        self.click(self.button_pass_again_ok_known)


class YLToDoHomePage(BasePage):
    # 我的工单iframe
    frame_to_do = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    # 我的工单 - 最大化按钮
    max_to_do_frame = 'xpath=>/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    # 工单号输入框
    to_do_num = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[1]/div/input'
    # 工单类型输入
    to_do_type = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'
    # 工单任务名称输入
    to_do_name = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input'
    # 点击工单中的处理按钮
    button_to_do_solve = \
        'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[9]/div/a[1]/span'
    # 处理嵌套
    frame_task_deal = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'
    # 进入工单详情嵌套
    frame_task_detail = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div/div/iframe'
    # 工单详情嵌套最大化按钮
    button_max_frame_task_detail = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    # 工单详情 - 拟办意见输入框
    input_comment = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[4]/td[2]/div[1]/div/pre/textarea'
    # 正文按钮
    button_body = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[1]'
    # 附件按钮
    button_attachment = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[2]'
    # 保存按钮
    button_save = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[3]'
    # 传递按钮
    button_pass = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[4]'
    # 打印按钮
    button_print = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[5]'
    # 自动签名按钮
    button_signature = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div[2]/form/table/tbody/tr[4]/td[2]/div[2]'
    # 点击保存后的知道了按钮
    button_saved_known = 'xpath=>/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 选择传递人员frame
    choose_member_frame = 'xpath=>/html/body/div[1]/div/div[3]/div[11]/div[2]/iframe'
    # 下一环节- 办理审签 - 杨磊
    yanglei = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[3]/ul/li/div[2]'
    # 选择传递人员 - 确定
    button_choose_member_ok = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[4]/button'
    # 选择人员确定后二次确认执行传递
    button_pass_again_ok = 'xpath=>/html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]'
    # 选择人员确定后二次确认执行传递后  传递成功后的知道了按钮
    button_pass_again_ok_known = 'xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 选择人员确定后二次确认执行传递后  传递结果 '传递成功'
    pass_result = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p'
    # 归档按钮
    button_on_file = 'xpath=>/html/body/div[2]/div/div/div[1]/div/button[3]'
    # 确认归档按钮
    button_on_file_yes = 'xpath=>/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]'
    # 归档成功 - 知道了
    button_on_file_known = 'xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 切入我的工单嵌套
    def switch_to_to_do_frame(self):
        self.switch_to_frame(self.frame_to_do)
    # 点击我的工单的最大化按钮
    def click_max_to_do_frame(self):
        self.click(self.max_to_do_frame)
    # 切出嵌套 - 公共
    def switch_default_frame(self):
        self.switch_to_default_content()
    # 点击我的工单列表中处理按钮
    def click_button_to_do_solve(self):
        self.click(self.button_to_do_solve)
    # 点击工单详情最大化按钮
    def click_button_max_frame_task_detail(self):
        self.click(self.button_max_frame_task_detail)
    # 切入工单详情嵌套
    def switch_frame_task_deal(self):
        self.switch_to_frame(self.frame_task_deal)
    def switch_frame_task_detail(self):
        self.switch_to_frame(self.frame_task_detail)
    # 输入拟办意见
    def send_keys_input_comment(self, text):
        self.send_keys(self.input_comment, text)
    # 点击自动签名
    def click_button_signature(self):
        self.click(self.button_signature)
    # 点击保存
    def click_button_save(self):
        self.click(self.button_save)
    # 点击传递
    def click_button_pass(self):
        self.click(self.button_pass)
    # 保存后点击知道了按钮
    def click_button_saved_known(self):
        self.click(self.button_saved_known)
    # 切入传递人员选择嵌套
    def switch_to_choose_member_frame(self):
        self.switch_to_frame(self.choose_member_frame)
    # 下一环节 - 归档 - 选择杨磊
    def click_yanglei(self):
        for i in range(5):
            self.excute_jindutiao_down()
        self.click(self.yanglei)
    def move_page_up(self):
        self.excute_jindutiao_up()
        time.sleep(5)
    def move_page_down(self):
        self.excute_jindutiao_down()
        time.sleep(5)

    # 选择传递人员后点击确定按钮
    def click_button_choose_member_ok(self):
        self.click(self.button_choose_member_ok)
    # 下一环节 - 办理审签 - 选择张振博 - 确定 - 二次确认
    def click_button_pass_again_ok(self):
        self.click(self.button_pass_again_ok)
    # 获取传递结果提示信息
    def get_pass_result_text(self):
        self.get_attribute(self.pass_result)
    # 点击传递成功提示框的知道了
    def click_button_pass_again_ok_known(self):
        self.click(self.button_pass_again_ok_known)
    def move_choose_member_jindutiao(self):
        self.move_jindutiao_down()

    def click_button_on_file(self):
        self.click(self.button_on_file)

    def click_button_on_file_yes(self):
        self.click(self.button_on_file_yes)

    def click_button_on_file_known(self):
        self.click(self.button_on_file_known)



