# 命名规范与路径迁移 / Naming and path migration

本次将 106 个旧路径规范化，保留原有 109 个文件。只调整名称、归类和必需的引用，不调整历史程序的业务逻辑，不执行旧脚本或驱动。

This migration normalises 106 paths while retaining all 109 original files. Changes are limited to names, grouping, and required references. Historical programs and driver binaries were not executed.

## 规则 / Rules

| 对象 / Item | 规范 / Convention | 示例 / Example |
| :--- | :--- | :--- |
| 目录 / Directories | 英文小写，短横线分词 / English `kebab-case` | `text-processing/txt-tools/` |
| Python 模块 / Python modules | 小写下划线 / `snake_case.py` | `merge_txt.py`, `read_text.py` |
| 网页、脚本资源、图片与数据 / Web assets and data | 小写，短横线分词，保留必要版本后缀 / Lowercase, descriptive names, meaningful version suffixes | `china-map.js`, `captcha-crop.png` |
| 工具约定名称 / Tool-defined names | 保留以避免破坏工具识别 / Preserve required conventions | `README.md`, `README.en.md`, `.gitignore`, `.idea/inspectionProfiles/`, `Project_Default.xml`, `dataSources.xml` |
| 第三方驱动 / Driver executables | 保留工具要求的程序名 / Preserve the executable's conventional name | `chromedriver.exe` |

不修改界面中文、数据库表名、远端网址、账号信息或 Python 标准库导入名称。部分历史脚本仍有本机路径、旧接口和缺失依赖，这些并未被重命名工作顺带修复。

Chinese UI strings, database table names, remote URLs, account configuration, and standard-library imports are not renamed. Existing hardcoded machine paths, obsolete integrations, and missing dependencies remain separate maintenance concerns.

## 目录分类 / Structure

```text
PythonCreation/
├── text-processing/          # TXT、编码、Base64、文字朗读
├── utilities/                # 翻译、图片坐标
├── data-visualization/       # 历史可视化项目
├── browser-automation/       # Selenium 基础与旧站点示例
├── web-scraping/             # 页面解析与历史采集练习
├── creative-demos/           # 图形、终端与创意演示
├── troubleshooting/          # 编码、HTTP、XPath 学习记录
├── network-experiments/      # 未执行的历史网络实验
├── docs/                     # 文档与迁移对照
└── tests/                    # 只读静态检查
```

## 查找旧文件 / Find a renamed file

- [CSV 旧名 → 新名对照表 / CSV path map](path-migration.csv)
- [结构化迁移记录 / Structured migration manifest](rename-map.json)

对照表保留旧路径用于查找，不代表旧目录仍存在。Git 历史也保留重命名前版本。

Old paths remain in the migration records for lookup; they are not active aliases. Git history retains the pre-migration revision.

## 已同步的引用 / Updated references

- 中英文 README 的链接、运行示例和输入 / 输出文件名。
- Flask 的本地 `database` 模块、模板与图表资源引用。
- 已存在图片、TXT 文件、保存网页资源和 IDE 模块文件的相对路径。
- PyInstaller 示例的入口脚本、构建名称和图标位置。

Both READMEs, local module imports, templates, static assets, known-existing file references, IDE module references, and PyInstaller naming references were updated together.

既有缺失文件不会被伪造出来。例如 Steam 示例仍需自行准备 `steamdb.html`；其命名已同步，但仓库并未新增该输入文件。不要将路径检查通过理解为历史业务已经可以运行。

Missing historical inputs are not fabricated. For example, the Steam parser still requires a user-supplied `steamdb.html`. Passing path checks does not prove that historical integrations run successfully.

## 静态验证 / Static verification

```bash
python -m unittest discover -s tests -v
```

检查覆盖命名唯一性、目标文件存在、Python 语法树结构、原二进制和文本数据哈希、本地资源引用、远端网址保持不变以及 README 链接。测试只解析或读取文件，不导入或运行历史程序。

Checks cover unique paths, destination existence, Python AST structure, binary/data integrity, local resource references, unchanged remote URLs, and README links. Historical programs are never imported or executed by these checks.

## 回退 / Rollback

重命名前的提交为 `075c9da563a966fa310621ecbd90e4a46bf7b502`。需要整批恢复时，先保存自己的未提交工作，再使用 `git revert` 撤销命名迁移提交；不要用强制推送覆盖后续工作。

The pre-migration revision is `075c9da563a966fa310621ecbd90e4a46bf7b502`. To undo the batch, save uncommitted work first and revert the naming-migration commit. Do not force-push over later work.
