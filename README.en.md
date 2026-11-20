<div align="center">

[简体中文](README.md) · **English**

<img src="docs/assets/overview.svg" width="100%" alt="PythonCreation — a personal archive of Python scripts and creative experiments" />

### Small experiments. Useful notes. A record of learning by doing.

[Browse by purpose](#browse-by-purpose) · [Start here](#start-here) · [Before running](#before-running) · [PΛV's website](https://www.worldai.fun)

</div>

## What this repository is

**PythonCreation is a personal learning archive**, collecting small Python utilities, creative demos, data-visualisation exercises, and older automation / parsing experiments.

It is **not a single application, an installable Python package, or a ready-to-run toolkit**. Folders are independent and now use consistent English names. Use the index below to find a relevant example, then review that script's inputs, dependencies, and side effects.

> Looking for more structured projects with dedicated setup documentation? See [Practical Toolbox](https://github.com/NanStars/practical-toolbox).

## Browse by purpose

| Area | Directory | What to expect |
| :--- | :--- | :--- |
| **Text & encoding** | [TXT processing](text-processing/txt-tools/) · [Base64](text-processing/base64-tools/) · [Text to speech](text-processing/text-to-speech/) | Merge TXT files, inspect / convert encodings, decode image data, and read local text aloud. |
| **Small utilities** | [Utilities](utilities/) | Translation experiments and image-coordinate selection with OpenCV. |
| **Data visualisation** | [Historical dashboard](data-visualization/epidemic-dashboard/) | An exercise connecting Flask routes, MySQL queries, and ECharts visualisations. |
| **Browser automation** | [Selenium exercises](browser-automation/) | Legacy examples of browser interaction and file-upload workflows; review compatibility first. |
| **Creative experiments** | [Visual & terminal demos](creative-demos/) | Code rain, a Turtle Christmas tree, fireworks HTML, countdowns, and progress output. |
| **Parsing & troubleshooting** | [STEAM](web-scraping/steam-packages/) · [Historical scraping](web-scraping/novel-examples/) · [Troubleshooting notes](troubleshooting/) | HTML parsing, historical data-collection exercises, and notes on encoding / request errors. |

## Start here

These entries have a relatively clear purpose. They were **reviewed statically for this documentation**, not executed as part of a complete compatibility test.

| Entry | Dependencies | Inputs / effects |
| :--- | :--- | :--- |
| [Ten-second countdown](creative-demos/countdown.py) | Standard library | Prints a countdown in the terminal. |
| [Progress-bar output](creative-demos/progress_bar.py) | Standard library | Demonstrates terminal progress output; it does not download anything. |
| [Image data-URL decoding](text-processing/base64-tools/decode_image.py) | Standard library | Expects a comma-separated image data URL and writes `decoded-image.jpeg`, replacing an existing file. |
| [Select image coordinates](utilities/image-coordinates/select_coordinates.py) | `opencv-python` · `numpy` | Opens a local image and records clicked coordinates; requires a desktop session and at least one click. |
| [Code rain](creative-demos/code_rain.py) | `pygame` | A graphical code-rain experiment with a fixed 1920 × 1080 window. |
| [Christmas tree](creative-demos/christmas_tree.py) | `turtle` / Tk support | A drawing exercise; requires a graphical desktop. |

### A minimal terminal example

After cloning and entering the repository, the countdown and progress examples use only the Python standard library:

```bash
git clone https://github.com/NanStars/PythonCreation.git
cd PythonCreation

python "creative-demos/countdown.py"
python "creative-demos/progress_bar.py"
```

`python` must refer to your Python 3 interpreter. The progress example only prints a visual progress bar; its “Download progress” text is not a real network task.

## Before running

1. **Read the selected script first.** Several files run code immediately at import time; do not batch-run the repository.
2. **Use an isolated environment for third-party dependencies.** There is no repository-wide dependency lock or validated single Python-version target. Install only what the selected example requires.
3. **Check paths and the working directory.** Older examples include machine-specific paths. Relative files such as `sample.txt` are resolved from the current working directory, not necessarily beside the script.
4. **Protect your files.** Run file-writing examples on copies. Encoding conversion rewrites source files; TXT merging appends to `merged.txt`, so repeated runs can duplicate output.
5. **Review legacy web integrations.** URLs, selectors, APIs, logins, and browser drivers may no longer match the original environment.

## Notes for larger / historical examples

<details>
<summary><strong>TXT processing & text-to-speech</strong></summary>

- [TXT merging](text-processing/txt-tools/merge_txt.py) uses a hardcoded input folder and appends output; it does not explicitly sort the directory listing.
- [Encoding inspection](text-processing/txt-tools/detect_encoding.py) and [conversion](text-processing/txt-tools/convert_encoding.py) use `chardet`. Back up input files before conversion.
- [Text-to-speech examples](text-processing/text-to-speech/) use `pyttsx3` and local system voices. The examples expect `sample.txt` in the working directory; voice availability depends on the operating system.

</details>

<details>
<summary><strong>Historical visualisation dashboard</strong></summary>

The main pieces are [app.py](data-visualization/epidemic-dashboard/app.py), [database.py](data-visualization/epidemic-dashboard/database.py), [data_collector.py](data-visualization/epidemic-dashboard/data_collector.py), templates, and static chart assets.

The example uses Flask, PyMySQL, requests, MySQL, and ECharts. Running the Flask process alone does not supply the required database, tables, connection configuration, or valid data. Historical upstream data interfaces have not been revalidated. Treat this as a visualisation-learning example, **not a current epidemic-statistics service**.

</details>

<details>
<summary><strong>Selenium & historical parsing exercises</strong></summary>

The Selenium folder contains browser-interaction exercises and older site-specific workflows. Some files use legacy Selenium APIs. Do not assume the bundled `chromedriver.exe` files are compatible with your browser or treat old login examples as ready-to-run integrations.

[The STEAM parsing example](web-scraping/steam-packages/parse_packages.py) expects a local `steamdb.html` input that is not included in the repository. Historical scraping examples may depend on changed markup or external services. Review access permissions, request volume, and content rights before adapting any collection workflow.

</details>

## Safety, maintenance & scope

- Keep real passwords, API keys, cookies, database exports, and account state out of public commits. Review and sanitise hardcoded configuration before reuse; rotate any value that was a real credential.
- Some high-risk network experiments are intentionally excluded from the recommended starting points. Do not run network code against systems you do not own or have explicit permission to test.
- The repository also contains historical IDE settings, saved pages, text output, and driver binaries. They are not a complete dependency or deployment package.
- No unified `LICENSE` is currently present. Public visibility does not itself grant unrestricted redistribution or commercial-use rights; check authorship and third-party licences before reuse.

**This naming refresh changes paths and their required references, not program logic.** Historical programs and driver binaries were not executed; compatibility limitations still apply.

---

<div align="center">

**Read one example. Understand it. Adapt it carefully.**

[PΛV](https://github.com/NanStars) · [Personal website](https://www.worldai.fun) · [Practical Toolbox](https://github.com/NanStars/practical-toolbox)

</div>


## Naming and path migration

Directories use English `kebab-case`; Python modules use `snake_case.py`. See the [naming guide](docs/naming-conventions.md) and [old → new path map](docs/path-migration.csv).
