# coding=utf-8
from Base.base_page import BasePage
import time


# 登录页面
class LoginHomepage(BasePage):
    # 用户名输入框
    username = "id=>user"
    # 密码输入框
    password = "id=>pwd"
    # 登陆按钮
    button_login = "xpath=>/html/body/div[2]/div/div[2]/form/div[3]/button"

    # 用户名输入
    def input_username(self, text):
        self.send_keys(self.username, text)
    # 密码输入
    def input_password(self, text):
        self.send_keys(self.password, text)
    # 点击登录按钮
    def click_button_login(self):
        self.click(self.button_login)


# index页面
class IndexHomepage(BasePage):
    # 商品管理菜单
    list_good_manage = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[8]/div/span[2]'
    # 订单管理菜单
    list_order_manage = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[5]/div/span[2]'
    # 企业管理菜单
    list_enterprise_manage = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[4]/div/span[2]'
    # 品牌管理菜单
    list_brand_manage = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[1]/div/span[2]'
    # 供应商管理菜单
    list_supplier_manage = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[9]/div/span[2]'
    # 品类管理菜单
    list_category_manage = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[10]/div/span[2]'
    # 文章管理菜单
    list_article_manage = 'xpath=>/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[2]/div/span[2]'
    # 首页打开的第一个iframe页
    frame_first_open = 'xpath=>/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/iframe'
    def click_list_good_manage(self):
        self.click(self.list_good_manage)
    def click_list_order_manage(self):
        self.click(self.list_order_manage)
    def click_list_enterprise_manage(self):
        self.click(self.list_enterprise_manage)
    def click_list_brand_manage(self):
        self.click(self.list_brand_manage)
    def click_list_supplier_manage(self):
        self.click(self.list_supplier_manage)
    def click_list_category_manage(self):
        self.click(self.list_category_manage)
    def click_list_article_manage(self):
        self.click(self.list_article_manage)
    def switch_first_iframe(self):
        self.switch_to_frame(self.frame_first_open)


# 商品管理页面
class GoodsManager(BasePage):
    # 添加商品按钮
    button_insert_good = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button[1]'
    # 查询 -- 商品名称输入框
    input_select_good_name = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[5]/div[2]/input'
    # 查询 -- 查询按钮
    button_select = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/button'
    # 表单页签
    page_size = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div[2]/div/div/table/tr/td[6]/span'


    def input_button_insert_good(self, text):
        self.send_keys(self.input_select_good_name, text)
    def click_button_select(self):
        self.click(self.button_select)
    def return_page_size(self):
        self.get_text(self.page_size)


# 添加商品 iframe
class InsertGoods(BasePage):
    # 商品管理页面iframe
    frame_goods_manager = 'xpath=>/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/iframe'
    # 添加商品按钮
    button_insert_good = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button[1]'
    # 添加商品iframe1
    frame_insert_good_step1 = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    # 输入商品名称
    input_goods_name = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[1]/div[2]/input'
    # 上传商品缩略图
    upload_goods_main_pic = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[3]/div[2]/div/div/div[3]/div/div[2]/input'
    # 商品缩略图开始上传按钮
    begin_upload_goods_main_pic = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[3]/div[2]/div/div/div[1]/div/div[2]'
    # 上传商品缩略图   上传成功知道了按钮
    known_upload_goods_main_pic = 'xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 上传商品轮播图
    upload_goods_many_pic = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[4]/div[2]/div/div/div[3]/div/div[2]/input'
    # 商品轮播图开始上传按钮
    begin_upload_goods_many_pic = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[4]/div[2]/div/div/div[1]/div/div[2]'
    # 上传商品轮播图   上传成功知道了按钮
    known_upload_goods_many_pic = 'xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 点击品类下拉
    select_category = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[5]/div/div[2]'
    # 品类选择高铁材料
    select_category_highway = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span'
    # 型号选择测试型号
    select_model_zhr = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[6]/div[2]/div[13]/label'
    # 输入包装方式
    input_packing_method = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[7]/div[2]/input'
    # 输入产地
    input_place_of_origin = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[8]/div[2]/input'
    # 输入单位
    input_company = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[9]/div[2]/input'
    # 输入试验指标
    input_test_index = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[10]/div[2]/input'
    # 输入保质期
    input_shelf_life = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[11]/div[2]/input'
    # 选择是进口
    choose_if_import = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[12]/div[2]/div[1]'
    # 选择上架
    choose_if_on_shelf = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/form/div/div/div[13]/div[2]/div[1]'
    # iframe1点击下一步
    button_next_step_to_step2 = 'xpath=>/html/body/div[2]/div/div[2]/div/div/button'
    # 添加商品iframe2
    frame_insert_good_step2 = 'xpath=>/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'
    # 点击品牌选择下拉
    select_brand = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/form/div/div[2]/div[2]/div/div[2]/input[1]'
    # 选择zhr测试品牌
    select_brand_choose_zhr = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[3]/span'
    # 点击选择供应商下拉
    select_supplier = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/form/div/div[2]/div[3]/div/div[2]'
    # 选择zhr测试供应商
    select_supplier_choose_zhr = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div[1]/div/div/label/span[3]'
    # 选择zhr测试供应商后关闭
    button_select_supplier_choose_zhr_close = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div[2]/a[2]/span'
    # 输入价格
    input_price = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/form/div/div[2]/div[4]/div[2]/input'
    # 输入库存
    input_stock = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/form/div/div[2]/div[5]/div[2]/input'
    # 上传型号图片
    upload_model_pic = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/form/div/div[2]/div[7]/div/div[3]/div/div[2]/input'
    # 上传型号图片点击确认上传
    begin_upload_model_pic = 'xpath=>/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/form/div/div[2]/div[7]/div/div[1]/div/div[2]'
    # 上传型号图片点击确认上传 上传后点击知道了
    known_upload_model_pic = 'xpath=>/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    # 点击第二步上传商品完成按钮
    button_over_insert_good = 'xpath=>/html/body/div[2]/div/div[2]/div/div/button[2]'

    # 获取保存成功提示文案
    success_text = 'xpath=>/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td'

    # list area of goods
    list_area_of_goods = 'xpath=>/html/body/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[4]/div'

    def switch_to_frame_goods_manager(self):
        self.switch_to_frame(self.frame_goods_manager)
    def click_button_insert_good(self):
        self.click(self.button_insert_good)
    def switch_to_frame_insert_good_step1(self):
        self.switch_to_frame(self.frame_insert_good_step1)
    def input_input_goods_name(self, text):
        self.send_keys(self.input_goods_name, text)
    def input_upload_goods_main_pic(self, text):
        self.send_keys(self.upload_goods_main_pic, text)
    def click_begin_upload_goods_main_pic(self):
        self.click(self.begin_upload_goods_main_pic)
    def click_known_upload_goods_main_pic(self):
        self.click(self.known_upload_goods_main_pic)
    def input_upload_goods_many_pic(self, text):
        self.send_keys(self.upload_goods_many_pic, text)
    def click_begin_upload_goods_many_pic(self):
        self.click(self.begin_upload_goods_many_pic)
    def click_known_upload_goods_many_pic(self):
        self.click(self.known_upload_goods_many_pic)
    def click_select_category(self):
        self.click(self.select_category)
    def click_select_category_highway(self):
        self.click(self.select_category_highway)
    def click_select_model_zhr(self):
        self.click(self.select_model_zhr)
    def input_input_packing_method(self, text):
        self.excute_jindutiao_down()
        self.excute_jindutiao_down()
        self.excute_jindutiao_down()
        self.send_keys(self.input_packing_method, text)
    def input_input_place_of_origin(self, text):
        self.send_keys(self.input_place_of_origin, text)
    def input_input_company(self, text):
        self.send_keys(self.input_company, text)
    def input_input_test_index(self, text):
        self.send_keys(self.input_test_index, text)
    def input_input_shelf_life(self, text):
        self.send_keys(self.input_shelf_life, text)
    def click_choose_if_import(self):
        self.click(self.choose_if_import)
    def click_choose_if_on_shelf(self):
        self.click(self.choose_if_on_shelf)
    def click_button_next_step_to_step2(self):
        self.click(self.button_next_step_to_step2)
    def switch_to_frame_insert_good_step2(self):
        self.switch_to_frame(self.frame_insert_good_step2)
    def click_select_brand(self):
        self.click(self.select_brand)
    def click_select_brand_choose_zhr(self):
        self.click(self.select_brand_choose_zhr)
    def click_select_supplier(self):
        self.click(self.select_supplier)
    def click_select_supplier_choose_zhr(self):
        self.click(self.select_supplier_choose_zhr)
    def click_select_supplier_choose_zhr_close(self):
        self.click(self.button_select_supplier_choose_zhr_close)
    def input_input_price(self, text):
        self.send_keys(self.input_price, text)
    def input_input_stock(self, text):
        self.send_keys(self.input_stock, text)
    def input_upload_model_pic(self, text):
        self.send_keys(self.upload_model_pic, text)
    def click_begin_upload_model_pic(self):
        self.click(self.begin_upload_model_pic)
    def click_known_upload_model_pic(self):
        self.click(self.known_upload_model_pic)
    def click_button_over_insert_good(self):
        self.click(self.button_over_insert_good)

    def get_text_success_text(self):
        self.get_text(self.success_text)

    def get_attribute_success_text(self):
        self.get_attribute(self.success_text)

    def click_list_area_of_goods(self):
        self.click(self.list_area_of_goods)


# 订单管理
class OrderManagerHomepage(BasePage):
    input_order_number = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/div[3]/div[2]/input'
    button_select_order = 'xpath=>/html/body/div[2]/div/div[1]/div/div/form/button'
    # 滚动条和js
    scrollbar = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div'
    scrollbar_area = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]'
    js_code_scrollbar = "arguments[0].style.setProperty('transform','translate3d(919.304px, 0px, 0px)');"
    js_code_scrollbar_area = "arguments[0].style.setProperty('transform','translate3d(-2006px, 0px, 0px)');"
    # 审核订单按钮 -
    button_check_order = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[28]/div/div/label[1]'
    def input_input_order_number(self, text):
        self.send_keys(self.input_order_number, text)
    def click_button_select_order(self):
        self.click(self.button_select_order)
    def drag_to_right(self):
        self.move_jindutiao_js(js_code=self.js_code_scrollbar, locator=self.scrollbar)
    def drag_to_right_list(self):
        self.move_jindutiao_js(js_code=self.js_code_scrollbar_area, locator=self.scrollbar_area)
    def click_button_check_order(self):
        self.click(self.button_check_order)


# 品类管理
class CategoryManageHomepage(BasePage):
    button_insert_model = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[4]/div[6]/div/a[2]/span'
    frame_insert_model = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    input_model_name = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[1]/div[2]/input'
    radio_if_open_country_level = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[2]/div[2]/div[2]/label'
    upload_pic_country_level = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[4]/div[2]/div/div/div[3]/div/div[2]/input'
    begin_upload_pic_country_level = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[4]/div[2]/div/div/div[1]/div/div[2]'
    known_upload_pic_country_level = 'xpath=>/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'
    button_save_category = 'xpath=>/html/body/div[2]/div/div[1]/div/div/button'
    def click_button_insert_model(self):
        self.click(self.button_insert_model)
    def switch_to_frame_insert_model(self):
        self.switch_to_frame(self.frame_insert_model)
    def input_input_model_name(self, text):
        self.send_keys(self.input_model_name, text)
    def click_radio_if_open_country_level(self):
        self.click(self.radio_if_open_country_level)
    def input_upload_pic_country_level(self, text):
        self.send_keys(self.upload_pic_country_level, text)
    def click_begin_upload_pic_country_level(self):
        self.click(self.begin_upload_pic_country_level)
    def click_known_upload_pic_country_level(self):
        self.click(self.known_upload_pic_country_level)
    def click_button_save_category(self):
        self.click(self.button_save_category)


# 品牌管理
class BrandManageHomepage(BasePage):
    button_insert_brand = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button'
    frame_insert_brand = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    input_brand_name = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div[2]/input'
    radio_select_category = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div[2]/div[5]/label/span[3]'
    select_model = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[3]/div/div[2]'
    select_model_zhr = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div[1]/div/div[13]/label/span[3]'
    select_model_close = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div[2]/a[2]/span'
    button_save_brand = 'xpath=>/html/body/div[2]/div/div[1]/div/div/button'
    def click_button_insert_brand(self):
        self.click(self.button_insert_brand)
    def switch_to_frame_insert_brand(self):
        self.switch_to_frame(self.frame_insert_brand)
    def input_input_brand_name(self, text):
        self.send_keys(self.input_brand_name, text)
    def click_radio_select_category(self):
        self.click(self.radio_select_category)
    def click_select_model(self):
        self.click(self.select_model)
    def click_select_model_zhr(self):
        self.click(self.select_model_zhr)
    def click_select_model_close(self):
        self.click(self.select_model_close)
    def click_button_save_brand(self):
        self.click(self.button_save_brand)


# 供应商管理
class SupplierManageHomepage(BasePage):
    button_insert_supplier = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button'
    frame_insert_supplier = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    input_supplier_name = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div[2]/input'
    input_supplier_address = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div[2]/input'
    radio_select_category_choose_highway_material = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[3]/div[2]/div[5]'
    select_brand = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[4]/div/div[2]'
    select_brand_zhr = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div[1]/div/div[6]/label'
    select_brand_close = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div[2]/a[2]/span'
    input_supplier_person = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[5]/div[2]/input'
    input_supplier_tel = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[6]/div[2]/input'
    button_save_supplier = 'xpath=>/html/body/div[2]/div/div[1]/div/div/button'
    def click_button_insert_supplier(self):
        self.click(self.button_insert_supplier)
    def switch_to_frame_insert_supplier(self):
        self.switch_to_frame(self.frame_insert_supplier)
    def input_input_supplier_name(self, text):
        self.send_keys(self.input_supplier_name, text)
    def input_input_supplier_address(self, text):
        self.send_keys(self.input_supplier_address, text)
    def click_radio_select_category_choose_highway_material(self):
        self.click(self.radio_select_category_choose_highway_material)
    def click_select_brand(self):
        self.click(self.select_brand)
    def click_select_brand_zhr(self):
        self.click(self.select_brand_zhr)
    def click_select_brand_close(self):
        self.click(self.select_brand_close)
    def input_input_supplier_person(self, text):
        self.send_keys(self.input_supplier_person, text)
    def input_input_supplier_tel(self, text):
        self.send_keys(self.input_supplier_tel, text)
    def click_button_save_supplier(self):
        self.click(self.button_save_supplier)


# 文章管理
class ArticleManageHomepage(BasePage):
    frame_insert_article = 'xpath=>/html/body/div[1]/div/div/div[11]/div[2]/iframe'
    insert_publish_content = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button'
    select_article_type = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div[2]/input[1]'
    select_article_type_hot = 'xpath=>/html/body/div[3]/div/div[1]/div[1]/div/div/div[5]/span'
    input_article_title = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[3]/div[2]/input'
    input_article_body = 'xpath=>/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[5]/div[2]/div'
    button_save_article = 'xpath=>/html/body/div[2]/div/div[1]/div/div/button'
    def switch_to_frame_insert_article(self):
        self.switch_to_frame(self.frame_insert_article)
    def click_insert_publish_content(self):
        self.click(self.insert_publish_content)
    def click_select_article_type(self):
        self.click(self.select_article_type)
    def click_select_article_type_hot(self):
        self.click(self.select_article_type_hot)
    def input_input_article_title(self, text):
        self.send_keys(self.input_article_title, text)
    def input_input_article_body(self, text):
        self.send_keys(self.input_article_body, text)
    def click_button_save_article(self):
        self.click(self.button_save_article)


# 企业管理
class EnterpriseManageHomepage(BasePage):
    pass



