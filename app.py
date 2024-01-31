from flask import Flask

# Create our flask app. Static files are served from 'static' directory
app = Flask(__name__, static_url_path='')

 # this route simply serves 'static/index.html'
@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__": app.run(debug=True)

'''
Instructions that you did!!
PS C:\Users\sushi\OneDrive\Desktop\Flask_app> git init
Initialized empty Git repository in C:/Users/sushi/OneDrive/Desktop/Flask_app/.git/
PS C:\Users\sushi\OneDrive\Desktop\Flask_app> git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py
        static/

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\sushi\OneDrive\Desktop\Flask_app> git add .
PS C:\Users\sushi\OneDrive\Desktop\Flask_app> git commit -m "First commit for flask app"
[master (root-commit) 672ba6e] First commit for flask app
 2 files changed, 17 insertions(+)
 create mode 100644 app.py
 create mode 100644 static/index.html
PS C:\Users\sushi\OneDrive\Desktop\Flask_app> git remote add origin git@github.com:jmacap/flask.git
>> git branch -M main
>> git push -u origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 565 bytes | 188.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:jmacap/flask.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
PS C:\Users\sushi\OneDrive\Desktop\Flask_app> '''