from flask import Flask, Response




app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        # games_files / scores.txt

        with open('C:\\Users\\דפנה זיגמן\\PycharmProjects\\world_of_games_3\\games_files\\scores.txt', 'r') as f:
            score = f.read()

        html = """
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
        return Response(html, mimetype='text/html')
    except Exception as e:
        html = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
            <h1><div id="score" style="color:red">{str(e)}</div></h1>
        </body>
        </html>
        """
        return Response(html, mimetype='text/html')

if __name__ == '__main__':
    app.run(port=5000)

