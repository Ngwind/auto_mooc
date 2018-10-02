# coding=utf-8
"""
实现自动刷慕课
1.打开浏览器，输入网址：
2.考虑cookies登陆
3.
"""
from selenium import webdriver
from time import sleep


def study(s_driver, s_session_list):
    h = s_driver.window_handles
    s_driver.switch_to.window(h[2])
    print("当前页面：", s_driver.title)
    sleep(3)
    session = s_driver.find_element_by_xpath("//*[@id='mainid']/h1").text
    print("当前选课：", session)
    iframe_total = s_driver.find_element_by_xpath('//*[@id="iframe"]')
    s_driver.switch_to.frame(iframe_total)
    iframe_player = s_driver.find_element_by_xpath('//iframe')  # 1042meikanguo  1039kanguo
    s_driver.switch_to.frame(iframe_player)
    # 点击开始播放
    s_driver.find_element_by_xpath('//*[@id="video"]/button').click()
    print("开始播放：", session)
    while True:
        sleep(10)
        end_time = s_driver.find_element_by_xpath('//*[@id="video"]/div[4]/div[4]/span[2]').text
        now_time = s_driver.find_element_by_xpath('//*[@id="video"]/div[4]/div[2]/span[2]').text
        print("总长：", end_time, "已观看：", now_time)
        if end_time == now_time:
            print("播放完成：", session)
            break
        else:
            continue
    # 点击下一集
    if s_session_list.index(session) != -1: # 这里有个bug，最后会报错，未修复
        session = s_session_list[s_session_list.index(session) + 1]
        print("下一集：", session)
        s_driver.switch_to.default_content()
        s_driver.find_element_by_xpath('//a[@title="' + session + '"]').click()
        s_driver.implicitly_wait(30)
        print("播放下一集:", session)
    else:
        print("woc！你居然学完了！")
        s_driver.quit()


session_list = ['工程管理公选概论', '工程管理的经济学基础', '资产', '货币的时间价值', '利息和利率', '名义利率与实际利率', '资金等值原理', '静态投资指标', '动态投资指标', '项目的多方案比选', '不确定性和风险', '盈亏平衡分析', '敏感性分析', '风险分析', '决策树分析法', '蒙特卡罗模拟方法', '收入、成本、利润的估算', '项目的盈利能力分析', '项目的偿债能力分析', '项目和工程项目', '项目可行性研究', '招投标', '建设工程施工合同', '建筑工程项目进度计划的编制方法', '建筑工程项目进度管理', '工程项目质量体系', '工程项目质量控制', '工程项目质量管理分析方法', '工程项目质量验收', '质量问题案例分析', '绿色建筑与发展', '绿色建筑“四节”技术', '绿色环境设计技术', '绿色建造技术体系', '可持续发展与绿色产业链', '绿色建筑实际案例介绍']

driver = webdriver.Chrome()
driver.get("http://passport2.chaoxing.com/login?fid=378&refer=http://gdut.benke.chaoxing.com")
driver.implicitly_wait(30)
driver.find_element_by_class_name("zl_input").send_keys("3115001441")
driver.find_element_by_class_name("zl_input2").send_keys("123456")
login = input("请在页面中自行登陆，登陆成功后，输入1提交:")
if login != "1":
    print("error! bye")
    driver.quit()
else:
    driver.find_element_by_class_name("Btn_blue_2").click()  # 点击"学习空间"
    driver.implicitly_wait(30)
    handle = driver.window_handles
    driver.switch_to.window(handle[1])
    print("当前页面：", driver.title)
    sleep(5)
    driver.switch_to.frame("frame_content")
    driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/ul/li[1]/div[2]/h3/a").click()
    driver.implicitly_wait(30)
    print("在列表中点开你还没学的课程，会从该课程一直往下学.")
    input("如果网页成功转跳，输入1提交:")
    if login != "1":
        print("error! bye")
        driver.quit()
    else:
        while True:
            sleep(3)
            study(driver, session_list)
