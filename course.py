import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://eams.shanghaitech.edu.cn/eams/stdElectCourse!defaultPage.action?')
# TODO: add your egate username here
driver.find_element('id', 'username').send_keys('')
# TODO: add your egate password here
driver.find_element('id', 'password').send_keys('')
driver.find_element('id', 'login_submit').click()

# 创建 CSV 文件并写入表头
with open('lesson_records.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['课程序号', '课程代码', '课程名称', '课程类别', '学分', '教师姓名', '建议修读对象', '开课院系', '选课说明', '同类课程', '已选/上限', '选课比', '课程安排', '操作'])
    current_cycle = 1
    # TODO: 手动输入可选课程列表的最后一页页码
    end_cycle = 19
    while current_cycle <= end_cycle:
        if current_cycle == 1:
            # TODO: 请将网址更换为带有id的选课界面
            driver.get(
                'https://eams.shanghaitech.edu.cn/eams/stdElectCourse!defaultPage.action?electionProfile.id=****')
        else:
            next_btns = driver.find_elements(By.CLASS_NAME, 'pgNextBtn') # 切换到下一页
            if next_btns:
                next_btns[0].click()
            else:
                print("已到达最后一页,无需点击下一页按钮。")  # 谁知道学校的网站从十七页开始就没有下一页了
        current_cycle += 1
        html_content = driver.page_source
        # 使用 BeautifulSoup 解析 HTML 内容,并指定 HTML 解析器为 'html.parser'
        soup = BeautifulSoup(html_content, 'html.parser')
        # 找到包含课程信息的表格
        course_table = soup.find('tbody', {'id': 'electableLessonList_data'})
        # 找到所有的课程记录 <tr> 标签
        lesson_rows = course_table.find_all('tr', class_='electGridTr')
        # 遍历每一个课程记录,提取所需的信息并写入 CSV 文件
        for row in lesson_rows:
            cells = row.find_all('td')
            course_num = cells[0].text.strip()
            course_code = cells[1].text.strip()
            course_name = cells[2].text.strip()
            course_type = cells[3].text.strip()
            credit = cells[4].text.strip()
            teacher = cells[5].text.strip()
            target_students = cells[6].text.strip()
            department = cells[7].text.strip()
            enrollment_info = cells[8].text.strip()
            similar_courses = cells[9].text.strip()
            enrollment = cells[10].text.strip()
            numerator, denominator = map(int, enrollment.split('/'))
            decimal_value = round(numerator / denominator, 4)  # 选课人数占比
            schedule = cells[11].text.strip()
            action = cells[12].text.strip()
            writer.writerow([course_num, course_code, course_name, course_type, credit, teacher, target_students, department, enrollment_info, similar_courses, enrollment, decimal_value, schedule, action])
print('CSV 文件已成功保存: lesson_records.csv')
driver.quit()
