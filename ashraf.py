from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML Template with embedded CSS and Arabic content
html_template = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>رؤية عُمان 2040 - نحو مستقبل مزدهر</title>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@200;300;400;500;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Tajawal', Arial, sans-serif;
            line-height: 1.8;
            color: #2c3e50;
            background: linear-gradient(135deg, #8B4513 0%, #CD853F 25%, #F4A460 50%, #DEB887 75%, #F5DEB3 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }

        /* Header Styles */
        .header {
            background: linear-gradient(135deg, #8B0000 0%, #DC143C 50%, #B22222 100%);
            color: white;
            padding: 2rem 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }

        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="pattern" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="2" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23pattern)"/></svg>');
            opacity: 0.5;
        }

        .header-content {
            position: relative;
            z-index: 2;
            text-align: center;
        }

        .main-title {
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            animation: fadeInUp 1s ease-out;
        }

        .subtitle {
            font-size: 1.8rem;
            font-weight: 300;
            margin-bottom: 2rem;
            opacity: 0.9;
            animation: fadeInUp 1s ease-out 0.3s both;
        }

        .year-badge {
            display: inline-block;
            background: linear-gradient(45deg, #228B22, #32CD32);
            padding: 1rem 2rem;
            border-radius: 50px;
            font-size: 2rem;
            font-weight: 700;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            animation: fadeInUp 1s ease-out 0.6s both;
        }

        /* Navigation */
        .nav {
            background: rgba(139, 0, 0, 0.95);
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 100;
            backdrop-filter: blur(10px);
        }

        .nav-list {
            display: flex;
            justify-content: center;
            gap: 2rem;
            list-style: none;
            flex-wrap: wrap;
        }

        .nav-item a {
            color: white;
            text-decoration: none;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        .nav-item a:hover {
            background: rgba(255,255,255,0.2);
            transform: translateY(-2px);
        }

        /* Content Sections */
        .section {
            padding: 4rem 0;
            margin: 2rem 0;
            background: rgba(255,255,255,0.95);
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.1);
            backdrop-filter: blur(10px);
            animation: fadeInUp 0.8s ease-out;
        }

        .section-title {
            font-size: 2.5rem;
            font-weight: 700;
            text-align: center;
            margin-bottom: 3rem;
            color: #8B0000;
            position: relative;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            height: 4px;
            background: linear-gradient(45deg, #228B22, #32CD32);
            border-radius: 2px;
        }

        /* Pillars Grid */
        .pillars-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .pillar-card {
            background: linear-gradient(135deg, #FFF8DC 0%, #F5DEB3 100%);
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
        }

        .pillar-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 5px;
            background: linear-gradient(45deg, #8B0000, #DC143C, #228B22);
        }

        .pillar-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.2);
            border-color: #228B22;
        }

        .pillar-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: #8B0000;
        }

        .pillar-title {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: #8B0000;
        }

        .pillar-description {
            color: #444;
            line-height: 1.6;
        }

        /* Statistics */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .stat-item {
            text-align: center;
            background: linear-gradient(135deg, #8B0000 0%, #DC143C 100%);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 900;
            display: block;
        }

        .stat-label {
            font-size: 1.1rem;
            opacity: 0.9;
            margin-top: 0.5rem;
        }

        /* Team Section */
        .team-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .team-card {
            background: linear-gradient(135deg, #228B22 0%, #32CD32 100%);
            color: white;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
            transition: all 0.3s ease;
        }

        .team-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
        }

        .team-name {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }

        .team-role {
            font-size: 1.2rem;
            opacity: 0.9;
            margin-bottom: 1rem;
        }

        .company-info {
            background: rgba(255,255,255,0.2);
            padding: 1rem;
            border-radius: 10px;
            margin-top: 1rem;
        }

        /* Footer */
        .footer {
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            text-align: center;
            padding: 3rem 0;
            margin-top: 3rem;
        }

        /* Animations */
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

        .fade-in {
            animation: fadeInUp 0.8s ease-out;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .main-title {
                font-size: 2.5rem;
            }
            
            .subtitle {
                font-size: 1.4rem;
            }
            
            .nav-list {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }
            
            .section {
                margin: 1rem 0;
                padding: 2rem 0;
            }
        }

        /* Scroll animations */
        .section {
            opacity: 0;
            transform: translateY(50px);
            transition: all 0.8s ease-out;
        }

        .section.visible {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <div class="header-content">
                <h1 class="main-title">رؤية عُمان</h1>
                <p class="subtitle">نحو مستقبل مزدهر ومستدام</p>
                <div class="year-badge">2040</div>
            </div>
        </div>
    </header>

    <!-- Navigation -->
    <nav class="nav">
        <div class="container">
            <ul class="nav-list">
                <li class="nav-item"><a href="#vision">الرؤية</a></li>
                <li class="nav-item"><a href="#pillars">المحاور</a></li>
                <li class="nav-item"><a href="#goals">الأهداف</a></li>
                <li class="nav-item"><a href="#team">الفريق</a></li>
            </ul>
        </div>
    </nav>

    <div class="container">
        <!-- Vision Section -->
        <section id="vision" class="section">
            <h2 class="section-title">رؤية عُمان 2040</h2>
            <div style="text-align: center; font-size: 1.3rem; line-height: 2; color: #444; max-width: 800px; margin: 0 auto;">
                <p style="margin-bottom: 2rem;">
                    <strong>"عُمان مجتمع معافى ومنتج في بيئة مستدامة يقوده مواطن معتز بهويته وانتمائه، يستثمر قدراته ومؤهلاته في اقتصاد متنوع ومستدام يتميز بالابتكار وحكومة فاعلة تكفل العدالة وسيادة القانون"</strong>
                </p>
                <p>
                    تهدف رؤية عُمان 2040 إلى بناء مستقبل مزدهر للسلطنة من خلال التركيز على التنمية المستدامة والاستثمار في الإنسان العُماني وتنويع مصادر الدخل وتعزيز الابتكار والتكنولوجيا.
                </p>
            </div>
        </section>

        <!-- Pillars Section -->
        <section id="pillars" class="section">
            <h2 class="section-title">المحاور الرئيسية للرؤية</h2>
            <div class="pillars-grid">
                <div class="pillar-card">
                    <div class="pillar-icon">👨‍💼</div>
                    <h3 class="pillar-title">الإنسان والمجتمع</h3>
                    <p class="pillar-description">
                        بناء مجتمع معافى ومنتج يتمتع بمستوى معيشي مرتفع ويحافظ على هويته وقيمه الأصيلة مع الانفتاح على الثقافات الأخرى.
                    </p>
                </div>
                
                <div class="pillar-card">
                    <div class="pillar-icon">🏭</div>
                    <h3 class="pillar-title">الاقتصاد والتنمية</h3>
                    <p class="pillar-description">
                        تطوير اقتصاد متنوع ومرن وتنافسي يقوم على المعرفة والابتكار ويستثمر الموقع الاستراتيجي للسلطنة.
                    </p>
                </div>
                
                <div class="pillar-card">
                    <div class="pillar-icon">🏛️</div>
                    <h3 class="pillar-title">الحوكمة والأداء المؤسسي</h3>
                    <p class="pillar-description">
                        تعزيز دولة القانون والمؤسسات وكفاءة الأداء الحكومي وجودة الخدمات المقدمة للمواطنين والمستثمرين.
                    </p>
                </div>
            </div>
        </section>

        <!-- Goals Section -->
        <section id="goals" class="section">
            <h2 class="section-title">الأهداف الاستراتيجية</h2>
            <div class="stats-grid">
                <div class="stat-item">
                    <span class="stat-number">5%</span>
                    <div class="stat-label">نمو اقتصادي سنوي</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">500K</span>
                    <div class="stat-label">وظيفة جديدة</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">95%</span>
                    <div class="stat-label">كفاءة الخدمات الحكومية</div>
                </div>
                <div class="stat-item">
                    <span class="stat-number">80%</span>
                    <div class="stat-label">مساهمة القطاع الخاص</div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 3rem; font-size: 1.2rem; line-height: 1.8; max-width: 900px; margin-left: auto; margin-right: auto;">
                <h3 style="color: #8B0000; margin-bottom: 2rem; font-size: 2rem;">القطاعات الواعدة</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
                    <div style="background: linear-gradient(135deg, #FFF8DC, #F5DEB3); padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                        <strong>🌊 الاقتصاد الأزرق</strong><br>
                        الاستفادة من الموارد البحرية والسياحة الشاطئية
                    </div>
                    <div style="background: linear-gradient(135deg, #FFF8DC, #F5DEB3); padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                        <strong>⚡ الطاقة المتجددة</strong><br>
                        الاستثمار في الطاقة الشمسية وطاقة الرياح
                    </div>
                    <div style="background: linear-gradient(135deg, #FFF8DC, #F5DEB3); padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                        <strong>💻 التكنولوجيا المالية</strong><br>
                        تطوير الخدمات المصرفية والمالية الرقمية
                    </div>
                    <div style="background: linear-gradient(135deg, #FFF8DC, #F5DEB3); padding: 1.5rem; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                        <strong>🏭 الثورة الصناعية 4.0</strong><br>
                        تطبيق التقنيات الذكية في الصناعة
                    </div>
                </div>
            </div>
        </section>

        <!-- Team Section -->
        <section id="team" class="section">
            <h2 class="section-title">فريق التطوير</h2>
            <div class="team-grid">
                <div class="team-card">
                    <div class="team-name">محمد أشرف علي</div>
                    <div class="team-role">مطور ومهندس حلول سحابية</div>
                    <div class="company-info">
                        <strong>شركة Smartovate</strong><br>
                        حاصل على شهادة AZ-900 من مايكروسفت أزور<br>
                        متخصص في تطوير التطبيقات السحابية والذكية
                    </div>
                </div>
                
                <div class="team-card">
                    <div class="team-name">الدكتور عبد الخالق</div>
                    <div class="team-role">خبير استراتيجي ومستشار تقني</div>
                    <div class="company-info">
                        <strong>شركة Smartovate</strong><br>
                        حاصل على شهادة AZ-900 من مايكروسفت أزور<br>
                        متخصص في الاستراتيجيات الرقمية والتحول التقني
                    </div>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 3rem; background: rgba(139, 0, 0, 0.1); padding: 2rem; border-radius: 15px;">
                <h3 style="color: #8B0000; margin-bottom: 1rem;">شركة Smartovate</h3>
                <p style="font-size: 1.2rem; line-height: 1.8;">
                    شركة رائدة في مجال الحلول التقنية الذكية والتحول الرقمي، متخصصة في تطوير التطبيقات السحابية 
                    والذكاء الاصطناعي وحلول المايكروسوفت أزور. نعمل على دعم رؤية عُمان 2040 من خلال توفير 
                    أحدث التقنيات والحلول المبتكرة.
                </p>
            </div>
        </section>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <p style="font-size: 1.2rem; margin-bottom: 1rem;">
                <strong>رؤية عُمان 2040 - نحو مستقبل مزدهر</strong>
            </p>
            <p>
                تم التطوير بواسطة محمد أشرف علي والدكتور عبد الخالق من شركة Smartovate
            </p>
            <p style="margin-top: 1rem; opacity: 0.8;">
                معتمد على تقنيات مايكروسفت أزور - شهادة AZ-900
            </p>
        </div>
    </footer>

    <script>
        // Scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.section').forEach(section => {
            observer.observe(section);
        });

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Add parallax effect to header
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const header = document.querySelector('.header');
            if (header) {
                header.style.transform = `translateY(${scrolled * 0.5}px)`;
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/health')
def health_check():
    return {'status': 'healthy', 'message': 'Oman Vision 2040 Website is running successfully'}

if __name__ == '__main__':
    # Use environment port for Azure deployment, default to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)