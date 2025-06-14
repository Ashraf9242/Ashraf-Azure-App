from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>From Dreams to Code - The Journey of Alex</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .hero {
            text-align: center;
            padding: 60px 0;
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            margin-bottom: 40px;
            animation: fadeInUp 1s ease-out;
        }

        .hero h1 {
            font-size: 3.5rem;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 20px;
            animation: glow 2s ease-in-out infinite alternate;
        }

        .hero p {
            font-size: 1.3rem;
            color: white;
            opacity: 0.9;
        }

        .story-section {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 40px;
            margin: 30px 0;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            animation: slideInLeft 0.8s ease-out;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .story-section:nth-child(even) {
            animation: slideInRight 0.8s ease-out;
        }

        .story-section:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }

        .story-section h2 {
            font-size: 2.2rem;
            color: #2c3e50;
            margin-bottom: 20px;
            position: relative;
            display: inline-block;
        }

        .story-section h2::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 3px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            animation: underlineGrow 2s ease-out forwards;
        }

        .story-section p {
            font-size: 1.1rem;
            line-height: 1.8;
            color: #555;
            margin-bottom: 15px;
        }

        .code-block {
            background: #1e1e1e;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            font-family: 'Courier New', monospace;
            overflow-x: auto;
            animation: typewriter 3s steps(40, end) forwards;
            white-space: nowrap;
            overflow: hidden;
            border-left: 4px solid #4ecdc4;
        }

        .phone-icon {
            display: inline-block;
            width: 60px;
            height: 60px;
            background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
            border-radius: 15px;
            margin: 0 10px;
            position: relative;
            animation: phoneFloat 3s ease-in-out infinite;
        }

        .phone-icon::before {
            content: '📱';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 30px;
            opacity: 0.3;
            animation: fadeInOut 2s ease-in-out infinite;
        }

        .laptop-icon {
            display: inline-block;
            width: 80px;
            height: 60px;
            background: linear-gradient(45deg, #4ecdc4, #44a08d);
            border-radius: 10px;
            margin: 0 10px;
            position: relative;
            animation: laptopGlow 2s ease-in-out infinite alternate;
        }

        .laptop-icon::before {
            content: '💻';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 35px;
        }

        .progress-bar {
            width: 100%;
            height: 10px;
            background: #e0e0e0;
            border-radius: 5px;
            overflow: hidden;
            margin: 20px 0;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border-radius: 5px;
            animation: progressFill 3s ease-out forwards;
            width: 0;
        }

        .achievement {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin: 20px 0;
            text-align: center;
            animation: bounce 2s ease-in-out infinite;
        }

        .floating-elements {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: -1;
        }

        .floating-element {
            position: absolute;
            opacity: 0.1;
            animation: float 6s ease-in-out infinite;
        }

        .floating-element:nth-child(1) {
            top: 10%;
            left: 10%;
            animation-delay: 0s;
        }

        .floating-element:nth-child(2) {
            top: 20%;
            right: 10%;
            animation-delay: 1s;
        }

        .floating-element:nth-child(3) {
            top: 60%;
            left: 20%;
            animation-delay: 2s;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes glow {
            from {
                text-shadow: 0 0 10px rgba(255, 107, 107, 0.5);
            }
            to {
                text-shadow: 0 0 20px rgba(78, 205, 196, 0.5);
            }
        }

        @keyframes underlineGrow {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }

        @keyframes typewriter {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }

        @keyframes phoneFloat {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }

        @keyframes fadeInOut {
            0%, 100% {
                opacity: 0.3;
            }
            50% {
                opacity: 0.1;
            }
        }

        @keyframes laptopGlow {
            from {
                box-shadow: 0 0 10px rgba(78, 205, 196, 0.3);
            }
            to {
                box-shadow: 0 0 25px rgba(78, 205, 196, 0.6);
            }
        }

        @keyframes progressFill {
            from {
                width: 0;
            }
            to {
                width: 100%;
            }
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-10px);
            }
            60% {
                transform: translateY(-5px);
            }
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) rotate(0deg);
            }
            50% {
                transform: translateY(-20px) rotate(180deg);
            }
        }

        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .story-section {
                padding: 20px;
            }
            
            .story-section h2 {
                font-size: 1.8rem;
            }
        }
    </style>
</head>
<body>
    <div class="floating-elements">
        <div class="floating-element">⚡</div>
        <div class="floating-element">💡</div>
        <div class="floating-element">🚀</div>
    </div>

    <div class="container">
        <div class="hero">
            <h1>From Dreams to Code</h1>
            <p>The Inspiring Journey of Alex - A Boy Who Became a Developer Without a Phone</p>
        </div>

        <div class="story-section">
            <h2>Chapter 1: The Dream Without a Device</h2>
            <p>Meet Alex, a 14-year-old boy from a small town who dreamed of creating amazing software. While his classmates were busy with their smartphones, Alex had something different - an unbreakable determination and a curious mind.</p>
            <p>Every day, he would walk past the local internet café, watching through the window as people typed away on keyboards. He couldn't afford a phone, but his dreams were bigger than any device.</p>
            <div class="phone-icon"></div>
            <span style="font-size: 2rem; color: #ff6b6b;">❌</span>
            <p><em>"I don't need a phone to change the world with code!"</em> - Alex</p>
        </div>

        <div class="story-section">
            <h2>Chapter 2: The Library Discovery</h2>
            <p>One rainy afternoon, Alex discovered the public library had computers with internet access. His eyes lit up as he sat in front of his first computer. The librarian, Mrs. Chen, noticed his enthusiasm and became his first mentor.</p>
            <p>Alex spent every free hour at the library, learning HTML, CSS, and JavaScript from free online resources. He took notes in an old notebook, creating his own reference guide.</p>
            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
            <p><strong>Skills Acquired:</strong> HTML, CSS, Basic JavaScript</p>
        </div>

        <div class="story-section">
            <h2>Chapter 3: The First Lines of Code</h2>
            <p>After weeks of learning, Alex wrote his first program. His hands trembled with excitement as he typed:</p>
            <div class="code-block">
                console.log("Hello World! I'm Alex, and I'm going to be a developer!");
            </div>
            <p>That simple line of code represented hours of learning, dedication, and unwavering belief in his dreams. The library computer became his gateway to a world of infinite possibilities.</p>
        </div>

        <div class="story-section">
            <h2>Chapter 4: Building Without Boundaries</h2>
            <p>Alex created his first website - a simple portfolio showcasing his journey. He used every free minute to learn new technologies:</p>
            <ul style="margin-left: 20px; margin-top: 15px;">
                <li>Python for backend development</li>
                <li>Flask for web applications</li>
                <li>Git for version control</li>
                <li>Database fundamentals</li>
            </ul>
            <div class="laptop-icon"></div>
            <p>His projects grew more complex each week. Alex proved that creativity and determination matter more than having the latest gadgets.</p>
        </div>

        <div class="story-section">
            <h2>Chapter 5: The Breakthrough</h2>
            <p>After a year of relentless learning, Alex built a web application that helped local businesses manage their inventory. Word spread quickly through his small town.</p>
            <div class="achievement">
                <h3>🏆 First Client Acquired!</h3>
                <p>Alex's first paid project - proving that skills matter more than devices</p>
            </div>
            <p>The local newspaper featured his story: "Local Teen Becomes Developer Using Only Library Computers"</p>
        </div>

        <div class="story-section">
            <h2>Chapter 6: The Future is Bright</h2>
            <p>Today, Alex is a successful full-stack developer working for a tech company. He still doesn't own the latest smartphone, but he owns something more valuable - the knowledge that limitations are just opportunities in disguise.</p>
            <p>He established a coding bootcamp for underprivileged youth, teaching them that:</p>
            <div style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #4ecdc4;">
                <p><strong>"Success in programming isn't about having the best tools - it's about having the best mindset."</strong></p>
            </div>
            <p>Alex's story reminds us that passion, persistence, and resourcefulness can overcome any obstacle. You don't need a phone to become a developer - you just need the determination to start.</p>
        </div>

        <div class="achievement">
            <h2>🚀 Your Journey Starts Now!</h2>
            <p>Like Alex, you can start your coding journey today. All you need is access to a computer and the willingness to learn. The next great developer could be you!</p>
        </div>
    </div>

    <script>
        // Add some interactive elements
        document.addEventListener('DOMContentLoaded', function() {
            // Animate elements on scroll
            const observerOptions = {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            };

            const observer = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.animationPlayState = 'running';
                    }
                });
            }, observerOptions);

            document.querySelectorAll('.story-section').forEach(section => {
                observer.observe(section);
            });

            // Add click effect to achievement boxes
            document.querySelectorAll('.achievement').forEach(achievement => {
                achievement.addEventListener('click', function() {
                    this.style.transform = 'scale(1.05)';
                    setTimeout(() => {
                        this.style.transform = 'scale(1)';
                    }, 200);
                });
            });
        });
    </script>
</body>
</html>
    """)

if __name__ == '__main__':
    app.run()
