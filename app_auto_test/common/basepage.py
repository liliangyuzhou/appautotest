
from common import my_logger
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from common.useful_dir import output_screenshoots_dir
import datetime
import time


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

logger=my_logger.my_logger(__name__)
class BasePage:

    #此层可以封装pageobjects层所有用到selenium中的底层方法
    #还可以包含一些元素的通用操作，如alert，windows，iframe等
    #还可以封装一些额外的web断言
    #实现日志记录，实现失败截图
    #封装的关键字函数可以相互套用

    def __init__(self,driver):
        # self.driver=webdriver.Chrome()
        self.driver=driver



    def save_web_screenshot(self,loc_msg='1234566'):
        """
        封装的自己截图方法，方便日志输出，以及其他共呢个调用
        :function:页面截图
        :param loc_msg:功能页面page的描述
        :return:
        """

        now=time.strftime("%Y-%m-%d %H_%M_%S")
        filepath="{0}_{1}.png".format(loc_msg,now)
        print(filepath)

        try:
            self.driver.save_screenshot(output_screenshoots_dir + '/' + filepath)
            logger.info("{} 失败截图成功,图片存放在 {} 目录下".format(loc_msg, output_screenshoots_dir))
        except:
            logger.exception("截取网页截图失败")
            raise


    def visible_element(self,loc,loc_msg="",timeout=30,frequency=0.5):
        """
        封装自己的等待元素可见方法，方便日志输出以及等待失败页面截图
        :function:等待元素可见
        :param loc: 元素定位表达式
        :param timeout: 设置超时时间
        :param frequency: 设置刷新频率
        :param loc_msg: 功能页面page的描述
        :return:
        """
        logger.info("等待元素 {} 可见".format(loc_msg))
        try:
            # start=datetime.datetime.now()
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
            # end=datetime.datetime.now()

            # logger.info("等待元素开始时间为{},结束时间为{},等待元素{}可见共耗时{}".format(start,end,loc,start-end))

        except:
            logger.exception(" {} 等待元素可见失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise



    def get_element(self,loc,loc_msg=""):
        """
        :function:获取元素定位的对象
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return: ele，返回一个定位到的元素对象
        """
        logger.info("获取 {} 的元素定位{}".format(loc_msg,loc))
        try:
            ele=self.driver.find_element(*loc)
            logger.info(" {} 元素定位成功".format(loc_msg))
            return ele
        except:
            logger.exception(" {} 元素定位失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise


    def input_text(self,loc,loc_msg="",*args):


        """
        :function:输入框输入文本
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :param args: 动态参数
        :return:
        """
        #1.等待元素可见
        self.visible_element(loc,loc_msg)
        #2.获取元素定位
        ele=self.get_element(loc,loc_msg)
        #3.发送文本
        try:
            ele.send_keys(args)
            logger.info(" {} 输入文本成功".format(loc_msg))

        except:
            logger.exception(" {} 输入文本失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise


    def button_click(self,loc,loc_msg=""):
        """
        :funcation:点击元素操作
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        self.visible_element(loc,loc_msg)
        ele=self.get_element(loc,loc_msg)

        try:
            ele.click()
            logger.info(" {} 元素点击成功".format(loc_msg))
        except:
            logger.exception(" {} 元素点击操作失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise

    def get_element_text(self,loc,loc_msg=""):
        """

        :funcation:获取元素文本
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        #等待元素可见
        self.visible_element(loc,loc_msg)
        #获取定位元素
        ele=self.get_element(loc,loc_msg)
        #获取所定位元素的文本内容
        try:
            text=ele.text
            logger.info(" {} 元素成功获取文本".format(loc_msg))
            return text
        except:
            logger.exception(" {} 元素获取文本失败}".format(loc_msg))
            self.save_web_screenshot(loc_msg)
            raise



    def get_attribute_value(self,attribute_name,loc,loc_msg=""):
        """

        :funcation:获取元素的属性值
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        self.visible_element(loc,loc_msg)
        ele=self.get_element(loc,loc_msg)
        try:
            attribute_value=ele.get_attribute(attribute_name)
            logger.info(" {} 属性值获取成功".format(attribute_name))
            return attribute_name
        except:
            logger.exception(" {} 获取元素属性值失败".format(attribute_name))
            self.save_web_screenshot(loc_msg)
            raise

    def switch_to_windows(self):
        pass

    def switch_to_iframe(self,loc,loc_msg=""):
        """
        :funcation:html切换到内嵌的iframe中
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        try:
            WebDriverWait(self.driver,30,0.5).until(EC.frame_to_be_available_and_switch_to_it(loc))
            logger.info(" {} 成功切换到此iframe中".format(loc_msg))
        except:
            logger.exception(" {} 切入alert弹框失败".format(loc_msg))
            self.save_web_screenshot(loc_msg)


    def switch_to_alert(self,loc,loc_msg):
        """

        :funcation:切换并关闭alert弹框
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        """
        #1.点击某个按钮，使弹框出现
        self.button_click(loc,loc_msg)
        try:
            #2.等待alert弹框可见
            WebDriverWait(self.driver,30,0.1).until(EC.alert_is_present())
            #3.切换到alert弹框中
            alert=self.driver.switch_to.alert()
            logger.info("alert弹框的文本内容是 {} ".format(alert.text))
            #4.处理alert弹框，是弹框消失
            alert.accept()
            logger.info(" {} 中的alert弹框成功处理结束")

        except:
            logger.exception(" {} 中的alert弹框处理失败")
            self.save_web_screenshot(loc_msg)
            raise


    #app专属操作


    #滑屏
    def swipe_screen(self,loc,loc_msg="",x1=0.1,y1=0.5,x2=0.9,y2=0.5):
        """

        :param loc:元素定位表达式
        :param loc_msg:功能页面page的描述
        :param x1:坐标倍数，范围（0-1），默认坐标从左向右滑动
        :param y1:坐标倍数，范围（0-1），默认坐标从左向右滑动
        :param x2:坐标倍数，范围（0-1），默认坐标从左向右滑动
        :param y2:坐标倍数，范围（0-1），默认坐标从左向右滑动
        :return:
        """
        # 等待
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
        # 滑屏操作
        # 获取 设备的大小
        try:
            logger.info("获取当前设备的大小")
            time.sleep(1)
            size = self.driver.get_window_size()

            logger.info("滑屏操作开始，根据x1,y1和x2,y2参数的值来确定滑动的方向，默认从左向右滑屏")
            self.driver.swipe(size["width"] * x1, size["height"] * y1, size["width"] * x2, size["height"] * y2)
        except:
            logger.exception("滑屏失败")
            self.save_web_screenshot(loc_msg)

    def swipe_screen_control_dirction(self,loc,loc_msg="",direction="LR"):
        """
        :param loc:元素定位表达式
        :param loc_msg:功能页面page的描述
        :param direction:代表滑动的方向（U-->UP,D-->DOWN,R-->RIGHT,L-->LEFT
        :return:
        """
        # 等待
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))
        # 滑屏操作
        # 获取 设备的大小
        try:
            time.sleep(1)
            logger.info("获取当前设备的大小")
            size = self.driver.get_window_size()

            if direction.upper() =='LR':
                logger.info("从左往右滑动")
                self.driver.swipe(size["width"] * 0.1, size["height"] * 0.5, size["width"] * 0.9, size["height"] * 0.5)
            elif direction.upper() =='RL':
                logger.info("从右往左滑动")
                self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5)
            elif direction.upper() =='UD':
                logger.info("从上往下滑动")
                self.driver.swipe(size["width"] * 0.5, size["height"] * 0.2, size["width"] * 0.5, size["height"] * 0.9)
            elif direction.upper() == 'UD':
                logger.info("从下往上滑动")
                self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.2)
        except:
            logger.exception("滑屏失败")
            self.save_web_screenshot(loc_msg)


    def app_list_swipe(self,loc,log_msg="",target_text=None):

        """
        app中列表滑动操作查找某个元素
        :param loc:元素定位表达式
        :param log_msg:功能页面page的描述
        :param target_text:需要查找的滑动列表中的元素的文本内容
        :return:
        """
        try:

            logger.info("等待要切换的滑动列表元素可见")
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc))

            logger.info("点击切换到滑动列表元素")
            self.driver.find_element(*loc).click()
            time.sleep(4)
            # 滑动一次查一次。
            # 滑动的距离要控制，要确保页面内容没有过度滑掉。
            # 如何确认已经滑到了底部。如果滑到了底部，再滑一次，两次内容一致。
            # 内容比对。滑动前的内容，和滑动后的内容比较。
            # 滑动前的内容 - old
            # 滑动后的内容 - new_src
            old = self.driver.page_source
            new_src = ""
            size = self.driver.get_window_size()

            while old != new_src:
                # 重新给old赋值。因为new马就要更新了。
                old = new_src
                # 滑动一次
                self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.2, 200)
                time.sleep(2)
                # 获取滑动之后的页面内容
                new_src = self.driver.page_source
                # 其它的需求：滑一次找一次的内容
                if new_src.find(target_text) != -1:
                    logger.info("{}元素已经找到".format(target_text))
                    break
        except Exception as e:
            logger.exception("滑屏列表操作失败")
            self.save_web_screenshot(log_msg)
            raise e


    #app处理toast
    def get_toast_text(self,loc,loc_msg=""):
        """
        获取 toast信息
        :param loc:元素定位表达式
        :param loc_msg:功能页面page的描述
        :return:
        """
        try:
            logger.info("获取toast信息")
            WebDriverWait(self.driver, 30, 0.01).until(EC.presence_of_all_elements_located(loc))
            ele=self.driver.find_element(*loc).text
            return ele
        except:
            logger.exception("获取toast信息失败")
            self.save_web_screenshot(loc_msg)




    def touch_action(self,loc,loc_msg=""):
        """
        九宫格操作
        :param loc: 元素定位表达式
        :param loc_msg: 功能页面page的描述
        :return:
        """
        try:
            # 手势设置 页面
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc))
            ele = self.driver.find_element(*loc)

            # 元素大小
            ele_size = ele.size
            # 起始坐标点
            start = ele.location
            # 步长
            step = ele_size["height"] / 6
            # 九宫格的五个坐标点
            point1 = (start["x"] + step, start["y"] + step)
            point2 = (point1[0] + 2 * step, point1[1])
            point3 = (point2[0] + 2 * step, point2[1])
            point4 = (point3[0] - 2 * step, point3[1] + 2 * step)
            point5 = (point4[0], point4[1] + 2 * step)

            tc = TouchAction(self.driver)
            # 步骤：先按住第一个点不松，移动到第五个点，然后释放。
            tc.press(x=point1[0], y=point1[1]).wait(200).move_to(x=point2[0], y=point2[1]). \
                wait(200).move_to(x=point3[0], y=point3[1]).wait(200).move_to(x=point4[0], y=point4[1]) \
                .wait(200).move_to(x=point5[0], y=point5[1]).wait(200).release().perform()

        except:
            logger.exception("九宫格操作失败")
            self.save_web_screenshot(loc_msg)


    # 切换到原生webview（H5页面）
    def switch_to_origin_webview(self,cons,log_msg):
        """
        这里切换到app应用中原生的h5页面中。
        # 2、根据context名字，切换到webview   # WebView_com.lemon.lemonban
        driver.switch_to.context('WEBVIEW_com.lemon.lemonban')

        # 3、已经切换到html，那后续就是web自动化操作。--- 原生webview，chromedriver
        # 3.11 定位元素：uc-devtool  https://dev.ucweb.com/docs/pwa/docs-zh/xy3whu
        # 3.12 定位元素：chrome://inspect  需要科学上网
        # 3.13 定位元素：driver.page_source得到html页面的源码。保存到html并用浏览器打开
        # 3.14 定位元素：找开发人员要html

        # 3.2 chromedriver的环境匹配 = chrome webview ==
        # appium - 会有一专门的目录来存在chromedriver，默认有一个，一般都是比较新。
        # 默认路径:C:/Users/简/AppData/Local/Programs/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/
        # 配置自定义路径: desired_caps["chromedriverExecutable"]='D:\\ChromeDrivers\\chromedriver52.exe'
        :param cons:通过cons = self.driver.contexts，获取app中的上下文，当做参数传入此函数
        :param log_msg:功能页面page的描述
        :return:
        """
        try:
            # cons = self.driver.contexts
            logger.info(cons)
            for con in cons:
                if 'WEBVIEW' in cons:
                    self.driver.switch_to.context(con)
                else:
                    logger.info("没有找到原生的webview")

        except:
            logger.exception("切换到app中的H5页面上失败")
            self.save_web_screenshot(log_msg)


    def switch_to_native_app(self):
        return self.driver.switch_to.context(None)


    # 切换到非原生webview（微信小程序）
    def switch_to_unorigin_webview(self,target_text):
        cons = self.driver.contexts
        print("当前所有的上下文为：", cons)
        for con in cons:
            if 'WEBVIEW_com.tencent.mm:' in con:
                # 切换到小程序webview,eg:'WEBVIEW_com.tencent.mm:appbrand0'
                return self.driver.switch_to.context(con)
        time.sleep(5)
        # 打印当前所有的窗口
        hs = self.driver.window_handles
        logger.info("当前所有的窗口为：", hs)
        # print("当前所在的窗口为：",driver.current_window_handle)
        # 需要找到哪一个窗口有柠檬班信息的窗口，然后再在其下找元素操作。
        # 遍历所有的handles，找到当前页面所在的handle：如果pageSource有包含你想要的元素，就是所要找的handle
        # 小程序的页面来回切换也需要：遍历所有的handles，切换到元素所在的handle
        for handle in hs:
            self.driver.switch_to.window(handle)
            logger.info("切换到窗口：", handle)
            time.sleep(3)
            # print(driver.page_source)
            if self.driver.page_source.find(target_text) != -1:
                break











