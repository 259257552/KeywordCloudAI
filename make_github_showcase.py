import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# ======================
project_name = "KeywordCloudAI"
developer_name = "丁学郅"
github_username = "你的GitHub用户名"
# ======================

os.makedirs("screenshots", exist_ok=True)

# ----------------------
# 1. 生成三张“产品演示图”
text = "人工智能 正在 改变 世界 深度学习 自然语言处理 计算机视觉 医疗 金融 教育 数据 分析"

wc = WordCloud(width=800, height=500, background_color="white", font_path="C:/Windows/Fonts/simhei.ttf")
img1 = wc.generate(text).to_image()
img1.save("screenshots/step1.png")

wc2 = WordCloud(width=800, height=500, background_color="black", colormap="cool", font_path="C:/Windows/Fonts/simhei.ttf")
img2 = wc2.generate(text).to_image()
img2.save("screenshots/step2.png")

wc3 = WordCloud(width=800, height=500, background_color="white", colormap="viridis", font_path="C:/Windows/Fonts/simhei.ttf")
img3 = wc3.generate(text).to_image()
img3.save("screenshots/step3.png")

# ----------------------
# 2. 合成 demo.gif
frames = [Image.open("screenshots/step1.png"), Image.open("screenshots/step2.png"), Image.open("screenshots/step3.png")]
frames[0].save("screenshots/demo.gif", save_all=True, append_images=frames[1:], duration=800, loop=0)

# ----------------------
# 3. 生成 README.md
readme = f"""
# {project_name}

**AI 可视化关键词云创作平台**

---

## 项目简介
这是一个基于 Python + NLP 的关键词云生成系统，支持中文文本分析、关键词提取和词云可视化。
用户可自定义配色方案，并将生成的词云用于 PPT 和报告。

> 本项目由人工智能专业本科生 {developer_name} 独立完成

---

## 项目演示

![Demo](screenshots/demo.gif)

---

## 技术栈
- Python
- NLP
- WordCloud
- 可视化分析

---

## GitHub
https://github.com/{github_username}/{project_name}
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme.strip())

# ----------------------
# 4. 生成简历项目文本
resume = f"""
项目：{project_name}
描述：开发 AI 关键词云可视化平台，实现中文关键词提取与词云生成，支持多种配色方案并导出图片，用于文本分析与可视化呈现。
技术栈：Python, NLP, WordCloud
GitHub：https://github.com/{github_username}/{project_name}
"""

with open("resume_project.txt", "w", encoding="utf-8") as f:
    f.write(resume.strip())

print("✅ demo.gif + README.md + resume_project.txt 已全部生成")
