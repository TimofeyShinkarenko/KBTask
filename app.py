from flask import Flask, request, render_template_string
import os

app = Flask(__name__)


os.makedirs('public_docs', exist_ok=True)
with open('public_docs/hello.txt', 'w', encoding='utf-8') as f:
    f.write("Hello World!")
with open('public_docs/about.txt', 'w', encoding='utf-8') as f:
    f.write("Just do it! (Кто понял, тот понял)")

with open('flag.txt', 'w', encoding='utf-8') as f:
    f.write("Flag: Shia LaBeouf\n"
            "https://www.youtube.com/watch?v=0B4vt9apNTM")

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>File Reader</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #ffffff; color: #333; }
        .menu { margin-bottom: 20px; }
        .menu a { margin-right: 15px; text-decoration: none; color: #0066cc; border-bottom: 1px solid #0066cc; }
        .content-box { border: 1px solid #ccc; padding: 20px; background-color: #f9f9f9; min-height: 100px; white-space: pre-wrap; font-family: monospace; }
        .error { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <h2>Просмотрщик документов</h2>
    <div class="menu">
        <!-- Ссылки передают имя файла через GET-параметр "file" -->
        <a href="/?file=hello.txt">Читать hello.txt</a>
        <a href="/?file=about.txt">Читать about.txt</a>
    </div>

    <h3>Содержимое файла:</h3>
    <div class="content-box">{% if error %}<span class="error">{{ error }}</span>{% else %}{{ content }}{% endif %}</div>
</body>
</html>
'''


@app.route('/')
def read_file():
    filename = request.args.get('file', 'hello.txt')
    filepath = os.path.join('public_docs', filename)

    content = ""
    error = ""

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        error = f"Файл '{filepath}' не найден"
    except Exception as e:
        error = f"Системная ошибка: {str(e)}"

    return render_template_string(HTML_TEMPLATE, content=content, error=error)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)