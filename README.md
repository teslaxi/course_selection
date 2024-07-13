# 选课记录+选课人数超上限课程汇总

这是一个使用 Python、Selenium 和 BeautifulSoup 从上海科技大学教务系统中抓取选课信息并保存到 CSV 文件的脚本。

## 解决的痛点

- 对于“跨学院选修”以及“跨学科选修”，学校的选课平台不能直接进行搜索，在本项目导出的csv中可以直接搜索。

  <img src="D:\university\c\Data_science\06_CS173\practice\courseselection\releasecourseselection\README.assets\image-20240713114611889.png" alt="image-20240713114611889" style="zoom:50%;" />

- 可以记录一些超上限选课的课程，方便后续参考。

  <img src="D:\university\c\Data_science\06_CS173\practice\courseselection\releasecourseselection\README.assets\image-20240713114805340.png" alt="image-20240713114805340" style="zoom:50%;" />

- 可以记录一些课程开设的教室，如果后续需要蹭课的话有教室可以去。

  

## 安装依赖

在运行该脚本之前,您需要安装以下依赖库:

1. `csv`: 内置库,无需额外安装。
2. `bs4` (BeautifulSoup): 使用 `pip install beautifulsoup4` 进行安装。
3. `selenium`: 使用 `pip install selenium` 进行安装。
4. `Chrome webdriver`: 需要下载对应版本的 Chrome 浏览器驱动,并将其路径添加到系统环境变量中。您可以在 [ChromeDriver 官网](https://sites.google.com/a/chromium.org/chromedriver/downloads) 下载。

## 使用说明

1. 将您的 egate 用户名和密码填写到相应的 TODO 注释中。
2. 手动输入可选课程列表的最后一页页码到相应的 TODO 注释中。
3. 请将网址更换为带有 `id` 的选课界面,并填写到相应的 TODO 注释中。
4. 运行脚本,它将在当前目录下生成一个名为 `lesson_records.csv` 的 CSV 文件,包含了所有可选课程的详细信息。

## 功能

该脚本主要执行以下功能:

1. 登录上海科技大学教务系统。

2. 遍历可选课程列表的所有页面。

3. 使用 BeautifulSoup 解析每个页面的 HTML 内容,提取课程信息。

   ```python
   # 使用 BeautifulSoup 解析 HTML 内容,并指定 HTML 解析器为 'html.parser'
   soup = BeautifulSoup(html_content, 'html.parser')
   # 找到包含课程信息的表格
   course_table = soup.find('tbody', {'id': 'electableLessonList_data'})
   # 找到所有的课程记录 <tr> 标签
   lesson_rows = course_table.find_all('tr', class_='electGridTr')
   ```

   ![image-20240713115131057](D:\university\c\Data_science\06_CS173\practice\courseselection\releasecourseselection\README.assets\image-20240713115131057.png)

4. 将提取的课程信息写入 CSV 文件。

5. 最后关闭浏览器。

## 注意事项

- 该脚本仅适用于上海科技大学的教务系统,不能保证适用于其他高校。
- 请确保您的 egate 用户名和密码正确,否则无法登录。
- 请确保您已经安装了 Chrome 浏览器和对应版本的 Chrome webdriver。
- 注意：直接用excel打开csv文件可能会出现中文乱码，[解决方式](https://blog.csdn.net/weixin_43848614/article/details/107742922)。
- 如果遇到任何问题或需要帮助,欢迎随时联系我。