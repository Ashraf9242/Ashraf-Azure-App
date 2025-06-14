import http.server
import socketserver
from urllib.parse import urlparse

class StoryHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alex's Coding Journey</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        h1 {
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }

        h2 {
            color: #27ae60;
            margin-top: 30px;
        }

        p {
            color: #333;
            margin-bottom: 15px;
        }

        .highlight {
            background: #ecf0f1;
            padding: 15px;
            border-left: 4px solid #3498db;
            margin: 20px 0;
            border-radius: 5px;
        }

        .code {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            font-family: monospace;
            margin: 15px 0;
        }

        .achievement {
            background: #27ae60;
            color: white;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            margin: 20px 0;
        }

        .phone-no {
            text-align: center;
            font-size: 50px;
            color: #e74c3c;
            margin: 20px 0;
        }

        .laptop-yes {
            text-align: center;
            font-size: 50px;
            color: #27ae60;
            margin: 20px 0;
        }

        ul {
            margin-left: 20px;
        }

        li {
            margin-bottom: 8px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>From No Phone to Full Stack Developer</h1>
        <p style="text-align: center; font-size: 18px; color: #7f8c8d;">The inspiring story of Alex</p>

        <h2>The Beginning</h2>
        <p>Alex was 15 years old and didn't have a smartphone. While his friends were busy on social media, Alex had a different dream - he wanted to become a programmer.</p>
        
        <div class="phone-no">📵</div>
        <p style="text-align: center;"><em>"No phone, but big dreams!"</em></p>

        <h2>The Discovery</h2>
        <p>Alex found out that the local library had free computers with internet. Every day after school, he would go there and learn programming online.</p>
        
        <div class="highlight">
            <strong>What Alex learned:</strong><br>
            • HTML and CSS basics<br>
            • JavaScript fundamentals<br>
            • Python programming<br>
            • How to use free online resources
        </div>

        <h2>First Code</h2>
        <p>After two weeks of learning, Alex wrote his first program:</p>
        
        <div class="code">
            print("Hello World! I'm Alex and I will be a developer!")
        </div>

        <h2>Building Projects</h2>
        <p>Alex didn't stop there. He started building simple projects:</p>
        <ul>
            <li>A personal website</li>
            <li>A calculator app</li>
            <li>A simple game</li>
            <li>A to-do list application</li>
        </ul>

        <div class="laptop-yes">💻</div>

        <h2>The Breakthrough</h2>
        <div class="achievement">
            <h3>First Job Offer!</h3>
            <p>After 8 months of learning, Alex got his first job as a junior developer</p>
        </div>

        <p>A local company saw Alex's projects online and offered him a part-time job. Alex proved that you don't need expensive gadgets to succeed in programming.</p>

        <h2>Today</h2>
        <p>Alex is now a successful full-stack developer. He works remotely, earns good money, and helps other young people learn coding.</p>

        <div class="highlight">
            <strong>Alex's advice:</strong><br>
            "You don't need a phone to become a developer. You just need dedication, curiosity, and access to a computer. Start today, start simple, and never give up!"
        </div>

        <h2>Your Turn</h2>
        <p>Like Alex, you can start your coding journey today. All you need is:</p>
        <ul>
            <li>Access to a computer</li>
            <li>Internet connection</li>
            <li>Willingness to learn</li>
            <li>Patience and practice</li>
        </ul>

        <div class="achievement">
            <h3>🚀 Start Your Journey Now!</h3>
            <p>The next success story could be yours!</p>
        </div>
    </div>
</body>
</html>
            """
            self.wfile.write(html_content.encode())
        else:
            self.send_error(404)

if __name__ == '__main__':
    PORT = 8000
    with socketserver.TCPServer(("", PORT), StoryHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}")
        httpd.serve_forever()
