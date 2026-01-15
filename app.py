import numpy as np
from flask import Flask, render_template, request
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

app = Flask(__name__)

def extract_keywords(text):
    words = " ".join(jieba.cut(text))

    try:
        vectorizer = TfidfVectorizer(max_features=50)
        tfidf = vectorizer.fit_transform([words])
        keywords = vectorizer.get_feature_names_out()
        weights = tfidf.toarray()[0]

        result = dict(zip(keywords, weights))

        if len(result) == 0:
            return {"无有效关键词": 1}

        return result

    except:
        return {"文本过短或无有效内容": 1}


@app.route('/', methods=['GET', 'POST'])
def index():
    cloud_path = None
    if request.method == 'POST':
        text = request.form['text']
        color = request.form['color']
        font = request.form['font']
        shape = request.form['shape']

        keywords = extract_keywords(text)

        if shape == "circle":
            import numpy as np
            x, y = np.ogrid[:400, :400]
            mask = (x - 200) ** 2 + (y - 200) ** 2 > 200 ** 2
            mask = 255 * mask.astype(int)
        else:
            mask = None

        wc = WordCloud(
            font_path=font,
            width=800,
            height=400,
            background_color='white',
            colormap=color,
            mask=mask
        )
        wc.generate_from_frequencies(keywords)
        wc.to_file('static/output.png')

        cloud_path = 'static/output.png'

    return render_template('index.html', cloud=cloud_path)


if __name__ == '__main__':
    app.run(debug=True)

