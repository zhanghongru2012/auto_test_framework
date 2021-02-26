# coding=utf-8
from Base.base_page import BasePage


# /login    登录页面
class LoginHomePage(BasePage):
    # 输入用户名
    input_username = "id=>user"
    input_password = "id=>password"
    button_login = "class_name=>btn-default"
    user_info = "class_name=>account"

    def input_user(self, text):
        self.send_keys(self.input_username, text)

    def input_passwd(self, text):
        self.send_keys(self.input_password, text)

    def submit_login(self):
        self.click(self.button_login)

    def get_user(self):
        return self.get_text(self.user_info)

    def submit(self):
        pass


# /index
class IndexHomePage(BasePage):
    # 首页用户信息-鼠标悬停 .perform()
    user_info = 'id=>user-info'
    # 用户信息中的我的工单入口 worksheet
    to_do_list = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'
    # 我的工单 - 最大化
    max_to_do_list = 'xpath=>/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'
    # 工单表单嵌套
    frame_to_do_list = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    # 工单名称输入框
    input_to_do_name = '/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'
    # 巡查管理tab
    tab_inspection_manager = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[4]/div/span[3]'
    # 巡查管理 - 事件上报tab
    tab_inspection_manager_event_report = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[4]/ul/li[1]/div/span[2]'
    # 点击处理按钮
    button_deal_to_do = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span'

    def hover_user_info(self):
        self.move_to_element(self.user_info)

    def click_to_do_list(self):
        self.click(self.to_do_list)

    def click_max_to_do_list(self):
        self.click(self.max_to_do_list)

    def switch_frame_to_do_list(self):
        self.switch_to_frame(self.frame_to_do_list)

    def input_input_to_do_name(self,text):
        self.send_keys(self.input_to_do_name, text)

    def click_tab_inspection_manager(self):
        self.click(self.tab_inspection_manager)

    def click_tab_inspection_manager_event_report(self):
        self.click(self.tab_inspection_manager_event_report)

    def click_button_deal_to_do(self):
        self.click(self.button_deal_to_do)


# 事件上报iframe页面
class InspectionManagerEventReport(BasePage):
    # 事件上报frame
    frame_event_report = 'xpath=>/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe'
    # 事件上报 - 事件细类下拉
    event_report_unit = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[3]/div/div[2]/input[1]'
    # 事件类型
    # 严重程度
    # 选择路基
    click_lj_xz = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span'
    # 选择巡查中队
    inspection_squadron = "xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[6]/div/div[2]/input[1]"
    # 选择一中队
    inspection_squadron_1 = "xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span"
    # 选择上报人员下拉
    report_members = "xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[9]/div/div[2]/input[1]"
    # 选择禹城测试
    report_members_yctest = "xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[12]/span"
    # 事件描述输入 ).send_keys("事件描述")
    event_describe = "xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[10]/div[2]/textarea"
    # 应急措施输入  .send_keys("应急措施")
    emergency_measure = "xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[11]/div[2]/textarea"
    # 维修建议输入.send_keys("维修建议")
    maintenance_advice = "/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[12]/div[2]/textarea"
    # 所在路线下拉
    on_route = "xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/input[1]"
    # 选择济南到德州
    on_route_jn_dz = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span'
    # 选择上下行
    up_down_direction = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/input[1]'
    # 选择上行
    up_direction = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span'
    # 输入起点桩号
    start_coordinate_num = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/input'
    # 输入止点桩号
    end_coordinate_num = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div[2]/input'
    # 输入偏移量
    offset = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[5]/div[2]/input'
    # 上传图片(需要传参 图片路径)
    upload_pic = 'xpath=>//input[@name="file"]'
    # 确认上传按钮
    button_upload_pic_yes = 'xpath=>//*[@id="event-uploader_uploader"]/div[1]/div/div[2]'
    # 知道了按钮
    button_upload_pic_known = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 添加路产损坏按钮
    button_insert_road_property_damage = 'xpath=>/html/body/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/form/button[1]'
    # 路产损坏iframe
    frame_insert_road_property_damage = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    # 选择边沟
    road_property_accuracy_side_ditch = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/ul/li/ul/li/ul/li[1]/div'
    # 选择土质边沟
    road_property_accuracy_side_ditch_soil = 'xpath=>/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div/span'
    # 选择压毁
    road_property_accuracy_side_ditch_soil_crush = 'xpath=>/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[4]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/label/span'
    # 路产损坏 确定按钮
    button_road_property_damage_ok = 'xpath=>/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/button'
    # 事件上报保存
    button_event_report_save = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[1]/button[2]'
    # 找到提示信息并打印, 点击知道了
    event_report_save_text = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p'
    button_event_report_save_known = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p'
    # 点击提交流程
    button_submit_process = 'xpath=>/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[1]/button[3]'

    #  切入事件上报frame
    def switch_to_frame_event_report(self):
        self.switch_to_frame(self.frame_event_report)
    # 点击事件细类下拉
    def click_event_report_unit(self):
        self.click(self.event_report_unit)
    # 点击路基
    def click_click_lj_xz(self):
        self.click(self.click_lj_xz)
    # 点击选择巡查中队下拉
    def click_inspection_squadron(self):
        self.click(self.inspection_squadron)
    # 点击选择一中队
    def click_inspection_squadron_1(self):
        self.click(self.inspection_squadron_1)
    # 点击选择上报人员下拉
    def click_report_members(self):
        self.click(self.report_members)
    # 点击选择禹城测试
    def click_report_members_yctest(self):
        self.click(self.report_members_yctest)
    # 事件描述输入
    def input_event_describe(self, text):
        self.send_keys(self.event_describe, text)
    # 应急措施输入
    def input_emergency_measure(self, text):
        self.send_keys(self.emergency_measure, text)
    # 维修建议输入
    def input_maintenance_advice(self, text):
        self.send_keys(self.maintenance_advice, text)
    # 点击所在路线下拉
    def click_on_route(self):
        self.click(self.on_route)
    # 点击选择济南到德州
    def click_on_route_jn_dz(self):
        self.click(self.on_route_jn_dz)
    # 点击上下行
    def click_up_down_direction(self):
        self.click(self.up_down_direction)
    # 选择上行
    def click_up_direction(self):
        self.click(self.up_direction)
    # 输入起点桩号
    def input_start_coordinate_num(self, text):
        self.send_keys(self.start_coordinate_num, text)
    # 输入止点桩号
    def input_end_coordinate_num(self, text):
        self.send_keys(self.end_coordinate_num, text)
    # 输入偏移量
    def input_offset(self, text):
        self.send_keys(self.offset, text)
    # 上传图片
    def input_upload_pic(self, text):
        self.send_keys(self.upload_pic, text)
    # 点击确认上传按钮
    def click_button_upload_pic_yes(self):
        self.click(self.button_upload_pic_yes)
    # 上传图片后点击知道了按钮
    def click_button_upload_pic_known(self):
        self.click(self.button_upload_pic_known)
    # 点击添加路产损坏按钮
    def click_button_insert_road_property_damage(self):
        self.click(self.button_insert_road_property_damage)
    # 切入路产损坏iframe
    def switch_to_frame_insert_road_property_damage(self):
        self.switch_to_frame(self.frame_insert_road_property_damage)
    # 选择边沟
    def click_road_property_accuracy_side_ditch(self):
        self.click(self.road_property_accuracy_side_ditch)
    # 选择土质边沟
    def click_road_property_accuracy_side_ditch_soil(self):
        self.click(self.road_property_accuracy_side_ditch_soil)
    # 选择压毁
    def click_road_property_accuracy_side_ditch_soil_crush(self):
        self.click(self.road_property_accuracy_side_ditch_soil_crush)
    # 点击路产损坏的确定按钮
    def click_button_road_property_damage_ok(self):
        self.click(self.button_road_property_damage_ok)
    # 点击事件上报保存按钮
    def click_button_event_report_save(self):
        self.click(self.button_event_report_save)
    # 找到提示信息并打印, 点击知道了
    def get_text_event_report_save_text(self):
        self.get_attribute(self.event_report_save_text)
    def click_button_event_report_save_known(self):
        self.click(self.button_event_report_save_known)
    # 点击提交流程
    def click_button_submit_process(self):
        self.click(self.button_submit_process)


# 事件上报流程处理iframe
class HandleIncidentReporting(BasePage):
    # 点击办理按钮
    click_bl = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[2]/div[1]/div/div/button[1]'
    # 点击审批处理
    click_spcl = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/form/button[1]'
    # 审批处理嵌套
    frame_spcl = 'xpath=>/html/body/div[1]/div/div[3]/div[11]/div[2]/iframe'
    # 转应急小修/转专项小修/点击处理完成
    click_zyjxx = 'xpath=>/html/body/div[2]/div/div[1]/div/div/button[1]'
    click_zzxxx = 'xpath=>/html/body/div[2]/div/div[1]/div/div/button[2]'
    click_clwc = 'xpath=>/html/body/div[2]/div/div[1]/div/div/button[3]'
    # 处理完成的提示信息
    text_tips = 'xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p'

    pass
