from flask import Flask, render_template_string
import json

app = Flask(__name__)

# بيانات رؤية عمان 2040
vision_data = {
    "sectors": [
        {
            "name": "الحوسبة السحابية",
            "name_en": "Cloud Computing",
            "progress": 75,
            "color": "#00D4FF",
            "icon": "☁️",
            "initiatives": [
                "مراكز البيانات الذكية",
                "الخدمات السحابية الحكومية", 
                "الأمن السيبراني المتقدم"
            ]
        },
        {
            "name": "الذكاء الاصطناعي",
            "name_en": "Artificial Intelligence",
            "progress": 65,
            "color": "#FF6B35",
            "icon": "🤖",
            "initiatives": [
                "منصات الذكاء الاصطناعي",
                "التعلم الآلي في الصناعة",
                "الروبوتات الذكية"
            ]
        },
        {
            "name": "إنترنت الأشياء",
            "name_en": "Internet of Things",
            "progress": 70,
            "color": "#4CAF50",
            "icon": "🌐",
            "initiatives": [
                "المدن الذكية",
                "النقل الذكي",
                "الزراعة الذكية"
            ]
        },
        {
            "name": "البلوك تشين",
            "name_en": "Blockchain",
            "progress": 55,
            "color": "#9C27B0",
            "icon": "⛓️",
            "initiatives": [
                "العملات الرقمية",
                "الهوية الرقمية",
                "العقود الذكية"
            ]
        },
        {
            "name": "الطاقة المتجددة",
            "name_en": "Renewable Energy",
            "progress": 80,
            "color": "#FFEB3B",
            "icon": "⚡",
            "initiatives": [
                "الطاقة الشمسية",
                "طاقة الرياح",
                "الهيدروجين الأخضر"
            ]
        },
        {
            "name": "التجارة الرقمية",
            "name_en": "Digital Commerce",
            "progress": 68,
            "color": "#FF5722",
            "icon": "💳",
            "initiatives": [
                "المدفوعات الرقمية",
                "التجارة الإلكترونية",
                "الخدمات المصرفية الرقمية"
            ]
        }
    ],
    "stats": {
        "digital_transformation": 72,
        "innovation_index": 68,
        "tech_adoption": 75,
        "cloud_readiness": 70
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>رؤية عمان 2040 - التحول الرقمي</title>
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
            color: white;
            overflow-x: hidden;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            padding: 40px 0;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
            animation: fadeInDown 1s ease-out;
        }

        .header h1 {
            font-size: 3rem;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            background: linear-gradient(45deg, #FFD700, #FFA500);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.15);
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: fadeInUp 1s ease-out;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .stat-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }

        .stat-value {
            font-size: 2.5rem;
            font-weight: bold;
            color: #FFD700;
            margin-bottom: 10px;
        }

        .sectors-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }

        .sector-card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 30px;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: slideIn 1s ease-out;
            transition: all 0.3s ease;
        }

        .sector-card:hover {
            transform: scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }

        .sector-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }

        .sector-icon {
            font-size: 2.5rem;
            margin-left: 15px;
        }

        .sector-title {
            flex: 1;
        }

        .sector-title h3 {
            font-size: 1.5rem;
            margin-bottom: 5px;
        }

        .sector-title p {
            opacity: 0.8;
            font-size: 0.9rem;
        }

        .progress-container {
            margin: 20px 0;
        }

        .progress-label {
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }

        .progress-bar {
            width: 100%;
            height: 12px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 6px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            border-radius: 6px;
            animation: progressFill 2s ease-out;
            transition: width 0.5s ease;
        }

        .initiatives-list {
            list-style: none;
            margin-top: 15px;
        }

        .initiatives-list li {
            padding: 8px 0;
            padding-right: 20px;
            position: relative;
            opacity: 0;
            animation: fadeInRight 1s ease-out forwards;
        }

        .initiatives-list li:before {
            content: "✓";
            position: absolute;
            right: 0;
            color: #4CAF50;
            font-weight: bold;
        }

        .cloud-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
            z-index: -1;
        }

        .cloud {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50px;
            opacity: 0.6;
            animation: float 20s infinite linear;
        }

        .cloud:before, .cloud:after {
            content: '';
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50px;
        }

        .footer {
            text-align: center;
            padding: 40px 0;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 15px;
            margin-top: 40px;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes fadeInRight {
            from {
                opacity: 0;
                transform: translateX(20px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes progressFill {
            from {
                width: 0%;
            }
        }

        @keyframes float {
            from {
                transform: translateX(-100px);
            }
            to {
                transform: translateX(calc(100vw + 100px));
            }
        }

        @keyframes pulse {
            0%, 100% {
                transform: scale(1);
            }
            50% {
                transform: scale(1.05);
            }
        }

        .pulse {
            animation: pulse 2s infinite;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2rem;
            }
            
            .sectors-grid {
                grid-template-columns: 1fr;
            }
            
            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="cloud-animation">
        <div class="cloud" style="width: 100px; height: 60px; top: 20%; animation-delay: 0s;"></div>
        <div class="cloud" style="width: 80px; height: 50px; top: 60%; animation-delay: -5s;"></div>
        <div class="cloud" style="width: 120px; height: 70px; top: 40%; animation-delay: -10s;"></div>
    </div>

    <div class="container">
        <div class="header">
            <h1>🇴🇲 رؤية عمان 2040</h1>
            <p>التحول الرقمي والحوسبة السحابية لمستقبل مزدهر</p>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{{ stats.digital_transformation }}%</div>
                <div>التحول الرقمي</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ stats.innovation_index }}%</div>
                <div>مؤشر الابتكار</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ stats.tech_adoption }}%</div>
                <div>تبني التكنولوجيا</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{{ stats.cloud_readiness }}%</div>
                <div>جاهزية الحوسبة السحابية</div>
            </div>
        </div>

        <div class="sectors-grid">
            {% for sector in sectors %}
            <div class="sector-card">
                <div class="sector-header">
                    <div class="sector-icon">{{ sector.icon }}</div>
                    <div class="sector-title">
                        <h3>{{ sector.name }}</h3>
                        <p>{{ sector.name_en }}</p>
                    </div>
                </div>
                
                <div class="progress-container">
                    <div class="progress-label">
                        <span>التقدم</span>
                        <span>{{ sector.progress }}%</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" 
                             style="width: {{ sector.progress }}%; background: {{ sector.color }};">
                        </div>
                    </div>
                </div>

                <ul class="initiatives-list">
                    {% for initiative in sector.initiatives %}
                    <li style="animation-delay: {{ loop.index * 0.2 }}s;">{{ initiative }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endfor %}
        </div>

        <div class="footer">
            <h3>🚀 نحو مستقبل رقمي مزدهر</h3>
            <p>رؤية عمان 2040 - تقنيات المستقبل اليوم</p>
            <p style="margin-top: 10px; opacity: 0.7;">Built for Microsoft Azure Cloud Platform</p>
            
            <div style="margin-top: 25px; padding-top: 20px; border-top: 1px solid rgba(255,255,255,0.2);">
                <p style="font-size: 0.9rem; opacity: 0.8; margin-bottom: 8px;">
                    💻 تم تطوير هذا الموقع بواسطة: <strong style="color: #FFD700;">محمد أشرف</strong>
                </p>
                <p style="font-size: 0.9rem; opacity: 0.8;">
                    🎓 بالتعاون مع: <strong style="color: #FFD700;">الدكتور عبدالخالق</strong>
                </p>
                <p style="font-size: 0.8rem; opacity: 0.6; margin-top: 10px;">
                    ⚡ Powered by Python Flask & Microsoft Azure
                </p>
            </div>
        </div>
    </div>

    <script>
        // إضافة تأثيرات تفاعلية
        document.addEventListener('DOMContentLoaded', function() {
            // تحديث أشرطة التقدم بشكل تفاعلي
            const progressBars = document.querySelectorAll('.progress-fill');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const progressBar = entry.target;
                        const width = progressBar.style.width;
                        progressBar.style.width = '0%';
                        setTimeout(() => {
                            progressBar.style.width = width;
                        }, 200);
                    }
                });
            });

            progressBars.forEach(bar => observer.observe(bar));

            // تأثير تحريك العناصر عند التمرير
            const cards = document.querySelectorAll('.sector-card, .stat-card');
            
            const cardObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }
                });
            });

            cards.forEach(card => {
                card.style.opacity = '0';
                card.style.transform = 'translateY(30px)';
                card.style.transition = 'all 0.6s ease';
                cardObserver.observe(card);
            });

            // إضافة المزيد من السحب المتحركة
            function createCloud() {
                const cloud = document.createElement('div');
                cloud.className = 'cloud';
                cloud.style.width = Math.random() * 100 + 80 + 'px';
                cloud.style.height = Math.random() * 40 + 50 + 'px';
                cloud.style.top = Math.random() * 100 + '%';
                cloud.style.animationDuration = (Math.random() * 10 + 15) + 's';
                cloud.style.animationDelay = Math.random() * 5 + 's';
                
                document.querySelector('.cloud-animation').appendChild(cloud);
                
                setTimeout(() => {
                    cloud.remove();
                }, 25000);
            }

            setInterval(createCloud, 3000);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def dashboard():
    return render_template_string(HTML_TEMPLATE, 
                                sectors=vision_data['sectors'],
                                stats=vision_data['stats'])

@app.route('/api/data')
def api_data():
    return json.dumps(vision_data, ensure_ascii=False)

@app.route('/health')
def health_check():
    return {"status": "healthy", "service": "Oman Vision 2040 Dashboard"}

if __name__ == '__main__':
    # للتطوير المحلي
    app.run(debug=True, host='0.0.0.0', port=5000)

# للنشر على Azure App Service
# يمكنك استخدام Gunicorn كخادم WSGI
# pip install gunicorn
# gunicorn --bind 0.0.0.0:8000 app:app
