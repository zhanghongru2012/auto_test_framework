from Base.base_page import BasePage


class LoginHomepage(BasePage):
    input_user = 'id=>user'
    input_pwd = 'id=>password'
    button_login = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div/form/button'
    def input_input_user(self, text):
        self.send_keys(self.input_user, text)
    def input_input_pwd(self, text):
        self.send_keys(self.input_pwd, text)
    def click_button_login(self):
        self.click(self.button_login)


class IndexHomepage(BasePage):
    # 路政管理tab
    tab_adjust = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[5]/div/span[3]'
    # 路政管理 - 事件上报
    tab_adjust_report_event = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[5]/ul/li[1]/div/span[2]'
    # 路政事案 - 路政事案登记
    tab_adjust_event_register = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[5]/ul/li[3]/ul/li/div/span[2]'
    def click_tab_adjust(self):
        self.click(self.tab_adjust)
    def click_tab_adjust_report_event(self):
        self.click(self.tab_adjust_report_event)
    def click_tab_adjust_event_register(self):
        self.click(self.tab_adjust_event_register)


class AdjustReportEvent(BasePage):
    # 路政管理事件上报iframe
    frame_adjust_report_event = 'xpath=>/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe'
    # 事件细类select
    select_event_type = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[1]/div[2]/div[3]/div/div[2]/input[1]'
    # 事件细类 - 摆摊设点
    select_td_event_type_btsd = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span'
    # 巡查中队 select
    select_check_team = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[1]/div[2]/div[5]/div/div[2]/input[1]'
    select_td_check_team1 = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span'
    # 事件描述输入
    input_event_content = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[1]/div[2]/div[10]/div[2]/textarea'
    # 所在路线select
    select_on_road = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/input[1]'
    select_on_road_x050 = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span'
    # 上下行select
    select_up_down = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/input[1]'
    select_up_down_up = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span'
    # 起止点桩号输入
    input_begin_zh = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/input'
    input_end_zh = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[2]/div[2]/div[4]/div[2]/input'
    # 上传照片
    upload_pic = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div[2]/input'
    # 开始上传按钮
    button_begin_upload_pic = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[2]/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div[2]'
    # 上传成功 - 知道了
    button_known_upload_pic = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 保存按钮
    button_save = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div/div[1]/button[2]'
    # 保存成功 知道了
    button_save_success_known = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 提交并发起流程按钮
    button_submit = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div/div[1]/button[3]'

    def switch_to_frame_adjust_report_event(self):
        self.switch_to_frame(self.frame_adjust_report_event)
    def click_select_event_type(self):
        self.click(self.select_event_type)
    def click_select_td_event_type_btsd(self):
        self.click(self.select_td_event_type_btsd)
    def click_select_check_team(self):
        self.click(self.select_check_team)
    def click_select_td_check_team1(self):
        self.click(self.select_td_check_team1)
    def input_input_event_content(self, text):
        self.send_keys(self.input_event_content, text)
    def click_select_on_road(self):
        self.click(self.select_on_road)
    def click_select_on_road_x050(self):
        self.click(self.select_on_road_x050)
    def click_select_up_down(self):
        self.click(self.select_up_down)
    def click_select_up_down_up(self):
        self.click(self.select_up_down_up)
    def input_input_begin_zh(self, text):
        self.send_keys(self.input_begin_zh, text)
    def input_input_end_zh(self, text):
        self.send_keys(self.input_end_zh, text)
    def input_upload_pic(self, text):
        self.send_keys(self.upload_pic, text)
    def click_button_begin_upload_pic(self):
        self.click(self.button_begin_upload_pic)
    def click_button_known_upload_pic(self):
        self.click(self.button_known_upload_pic)
    def click_button_save(self):
        self.click(self.button_save)
    def click_button_save_success_known(self):
        self.click(self.button_save_success_known)
    def click_button_submit(self):
        self.click(self.button_submit)


class DealTask(BasePage):
    hover_user_info = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]'
    my_task = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[3]/ul/li[6]/span[2]'
    frame_my_task = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    max_my_task_frame = 'xpath=>/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    close_my_task_frame = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div[1]/a[3]'
    # 事件上报流程
    # 监察中队长审批
    button_deal_task_jczdzsp = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[9]/div/a[1]/span/i'
    frame_deal_task_jczdzsp = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'
    button_pass_jczdzsp = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div/div/button[1]'
    # 路政业内派工
    button_deal_task_lzynpg = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[9]/div/a[1]/span/i'
    frame_deal_task_lzynpg = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'
    button_do_lzynpg = 'xpath=>/html/body/div[2]/div[1]/div[2]/div[1]/div/div/button[1]'
    button_save_lzynpg = 'xpath=>/html/body/div[2]/div[1]/div[2]/div[1]/div/div/button[2]'
    button_pass_lzynpg = 'xpath=>/html/body/div[2]/div[1]/div[2]/div[1]/div/div/button[3]'
    button_give_deal_member = 'xpath=>/html/body/div[2]/div[1]/div[2]/div[1]/div/div/button[6]'
    button_if_pass_lzynpg_yes = 'xpath=>/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]'
    frame_give_deal_member = 'xpath=>/html/body/div[1]/div/div[3]/div[11]/div[2]/iframe'
    input_give_deal_member_search = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[2]/div[2]/input'
    radio_give_deal_member_select_zytest = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/label/span'
    button_give_deal_member_select_yes = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button'
    # 事件处理
    button_deal_task_sjcl = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[9]/div/a[1]/span/i'
    frame_deal_task_sjcl = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'
    button_do_sjcl = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[2]/div[1]/div/div/button[1]'
    button_over_sjcl = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/button[3]'

    # 路政事案登记流程
    # ----事案登记
    frame_lzsadj = 'xpath=>/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe'
    radio_shian_type = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/div[1]/label/span[1]'
    select_xunchazhongdui = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]/input[1]'
    select_xunchazhongdui_choose_1 = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span'
    select_zhifarenyuan1 = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[4]/div/div[2]/input[1]'
    select_zhifarenyuan1_choose_1 = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div/span'
    select_zhifarenyuan2 = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[5]/div/div[2]/input[1]'
    select_zhifarenyuan2_choose_1 = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div/span'
    # 现场状况
    input_weather = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[5]/div[2]/input'
    select_road = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[6]/div/div[2]/input[1]'
    select_road_hc_cd = 'xpaht=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[11]/span'
    select_up_down = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[7]/div/div[2]/input[1]'
    select_up_down_up = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span'
    input_begin_zh = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[8]/div[2]/input'
    input_over_zh = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[9]/div[2]/input'
    select_drive_deriction = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[10]/div/div[2]/input[1]'
    select_drive_direction_west_to_north = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span'
    select_yanzhongchengdu = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[11]/div/div[2]/input[1]'
    select_yanzhongchengdu_most = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[5]/span'
    select_to_frame_youyu = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[12]/div[2]/input'

    select_daozhi = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div[2]/div[13]/div/div[2]/input[1]'
    select_dapzhi_choose_zybc = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[7]/span'
    # 车辆信息
    input_car_card = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/input'
    select_car_type = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[2]/div/div[2]/input[1]'
    select_car_type_choose_yueyeche = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[7]/span'
    input_changpaixinghao = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[3]/div[2]/div[4]/div[2]/input'
    # 驾驶员信息
    input_driver_name = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[1]/div[2]/input'
    select_yucheliangguanxi = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[2]/div/div[2]/input[1]'
    select_yucheliangguanxi_benren = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[2]/span'
    input_driver_card_num = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[3]/div[2]/input'
    input_driver_age = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[3]/div[2]/input'
    input_driver_address = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[7]/div[2]/input'
    select_driver_zhiye = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[8]/div/div[2]/input[1]'
    select_driver_zhiye_choose_jiashiuan = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span'
    input_driver_tel = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[9]/div[2]/input'
    input_driver_company = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[4]/div[2]/div[10]/div[2]/input'
    input_driver_name_name = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[5]/div[2]/div[11]/div[2]/input'
    # 案件描述
    input_event_description = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div[6]/div[2]/div[1]/div[2]/textarea'

    # ----收费项目
    button_tab_shoufeixiangmu = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[1]/div[1]/div[1]/ul/li[2]/span'
    button_insert_shoufeixiangmu = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/button[1]'
    frame_insert_shoufeixiangmu =  'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'

    button_save_event = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div[1]/button[2]'
