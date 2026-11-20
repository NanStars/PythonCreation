<div align="center">

**简体中文** · [English](README.en.md)

<img src="docs/assets/overview.svg" width="100%" alt="PythonCreation — Python 学习脚本与创意实验档案" />

### 把零散尝试，留成可以回看的学习笔记。
Small experiments. Useful notes. Learning by doing.

[按用途找内容](#按用途找内容) · [先看这几个](#先看这几个) · [运行前先确认](#运行前先确认) · [个人网站](https://www.worldai.fun)

</div>

## 这是什么

**PythonCreation 是一份个人 Python 学习与实验档案**，收录日常小脚本、创意演示、数据可视化练习，以及较早的自动化与页面解析尝试。

它**不是一个统一应用、可安装的 Python 包，也不是一键即用的工具箱**。各目录相互独立，按统一英文命名归类；先按用途找到示例，再查看它需要什么输入、依赖，以及运行后会做什么。

> 如果想找结构更完整、带独立启动和部署文档的项目，可以看 [Practical Toolbox](https://github.com/NanStars/practical-toolbox)。

## 按用途找内容

| 类别 | 目录入口 | 主要内容 |
| :--- | :--- | :--- |
| **文本与编码** | [TXT 文本处理](text-processing/txt-tools/) · [Base64](text-processing/base64-tools/) · [文字阅读](text-processing/text-to-speech/) | TXT 合并、编码识别与转换、图片数据解码、文字转语音。 |
| **便利小工具** | [便利工具](utilities/) | 翻译练习、使用 OpenCV 点击图片并获取坐标。 |
| **数据可视化** | [历史可视化项目](data-visualization/epidemic-dashboard/) | Flask 路由、MySQL 数据查询与 ECharts 图表的组合练习。 |
| **浏览器自动化** | [Selenium 练习](browser-automation/) | 浏览器交互、文件上传等历史示例，使用前需检查版本与页面适配。 |
| **创意与演示** | [创意演示](creative-demos/) | 代码雨、Turtle 圣诞树、烟花 HTML、倒计时与终端进度输出。 |
| **历史解析与排错** | [STEAM](web-scraping/steam-packages/) · [历史采集](web-scraping/novel-examples/) · [问题记录](troubleshooting/) | HTML 解析、历史采集流程，以及中文编码和请求错误的学习记录。 |

## 先看这几个

这些示例的用途比较明确，适合先从小处阅读。下表经过本次**静态阅读核对**，不代表已执行全部脚本或完成兼容性测试。

| 示例 | 依赖 | 输入与运行效果 |
| :--- | :--- | :--- |
| [十秒倒计时](creative-demos/countdown.py) | Python 标准库 | 在终端打印倒计时。 |
| [进度条](creative-demos/progress_bar.py) | Python 标准库 | 演示终端刷新输出，不会真的下载文件。 |
| [图片数据解码](text-processing/base64-tools/decode_image.py) | Python 标准库 | 输入带逗号分隔的图片 data URL；写入 `decoded-image.jpeg`，会覆盖同名文件。 |
| [图像坐标定位](utilities/image-coordinates/select_coordinates.py) | `opencv-python` · `numpy` | 打开本地图片并记录点击位置；需要桌面环境，且至少点击一次。 |
| [代码雨](creative-demos/code_rain.py) | `pygame` | 图形动画练习，窗口尺寸固定为 1920 × 1080。 |
| [圣诞树](creative-demos/christmas_tree.py) | `turtle` / Tk 支持 | 绘图练习，需要可用的图形桌面。 |

### 一个最小的终端示例

克隆仓库并进入目录后，倒计时和进度条示例只使用 Python 标准库：

```bash
git clone https://github.com/NanStars/PythonCreation.git
cd PythonCreation

python "creative-demos/countdown.py"
python "creative-demos/progress_bar.py"
```

请确认 `python` 指向自己的 Python 3 解释器。进度条中的 “Download progress” 只是演示文案，并不是实际下载任务。

## 运行前先确认

1. **先读单个脚本，再决定是否运行。** 部分文件导入时就会执行代码，不要批量运行整个仓库。
2. **第三方依赖放到独立环境。** 仓库没有统一依赖锁文件，也没有经过验证的统一 Python 版本目标；只为选中的示例安装实际需要的依赖。
3. **检查路径和工作目录。** 旧示例包含本机绝对路径；`sample.txt` 等相对文件通常从当前工作目录读取，不一定从脚本所在目录读取。
4. **文件处理先用副本。** 编码转换会重写源文件；TXT 合并会追加到 `merged.txt`，重复运行可能产生重复内容。
5. **网页相关示例需要重新适配。** 旧网址、选择器、接口、登录流程和浏览器驱动不一定仍与当时一致。

## 较大项目与历史示例说明

<details>
<summary><strong>TXT 处理与文字朗读</strong></summary>

- [TXT 合并](text-processing/txt-tools/merge_txt.py) 使用写死的输入目录并追加输出，没有显式排序目录中的文件。
- [编码查看](text-processing/txt-tools/detect_encoding.py) 和 [编码转换](text-processing/txt-tools/convert_encoding.py) 使用 `chardet`；转换前先备份原文件。
- [文字朗读示例](text-processing/text-to-speech/) 使用 `pyttsx3` 和系统语音。示例从当前工作目录读取 `sample.txt`，可用语音受操作系统影响。

</details>

<details>
<summary><strong>历史数据可视化项目</strong></summary>

主要入口是 [app.py](data-visualization/epidemic-dashboard/app.py)、[database.py](data-visualization/epidemic-dashboard/database.py)、[data_collector.py](data-visualization/epidemic-dashboard/data_collector.py)，以及模板和静态图表资源。

项目组合了 Flask、PyMySQL、requests、MySQL 与 ECharts。仅启动 Flask 并不会自动提供数据库、表结构、连接配置和有效数据。历史上游数据接口未重新验证，适合作为可视化学习材料，**不应当作当前疫情统计服务**。

</details>

<details>
<summary><strong>Selenium 与历史解析练习</strong></summary>

Selenium 目录包含浏览器交互和早期站点适配示例，部分代码使用旧式 Selenium API。不要假定附带的 `chromedriver.exe` 与本机浏览器兼容，也不要直接把旧登录示例当作可用集成。

[STEAM 解析示例](web-scraping/steam-packages/parse_packages.py) 需要本地 `steamdb.html` 输入，但仓库没有提供该文件。历史采集示例可能依赖已改变的网页结构或外部服务；改写前先确认访问权限、请求频率和内容使用授权。

</details>

## 安全、维护与使用边界

- 真实密码、API Key、Cookie、数据库导出和账号状态不应进入公开提交。运行旧脚本前先检查并脱敏硬编码配置；曾用于真实环境的凭据应先轮换。
- 部分高风险网络实验未列入推荐上手入口。不要对不属于自己、也未获得明确授权的系统运行相关网络代码。
- 仓库还保留了历史 IDE 配置、网页存档、文本输出和驱动程序；它们不构成完整的依赖或部署包。
- 当前没有统一 `LICENSE`。公开可见不等于获得任意再分发或商业使用授权，复用前应核对来源与第三方许可证。

**命名规范化只变更目录、文件名及必需的路径引用，不调整业务逻辑。** 历史程序和二进制驱动仍未执行，也不宣称所有示例现在都能直接运行。

---

<div align="center">

**先读懂一个小例子，再把它改成适合自己的工具。**

[PΛV](https://github.com/NanStars) · [个人网站](https://www.worldai.fun) · [实用工具箱](https://github.com/NanStars/practical-toolbox)

</div>


## 命名与旧路径迁移

目录采用英文 `kebab-case`，Python 模块采用 `snake_case.py`。查看[命名规范](docs/naming-conventions.md)和[旧名 → 新名对照表](docs/path-migration.csv)。
