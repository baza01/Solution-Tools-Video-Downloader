import streamlit as st
import streamlit.components.v1 as components
import requests
import urllib.parse
import os

# 1. إعداد الصفحة بنظام Wide لاستغلال الجوانب للألعاب
st.set_page_config(
    page_title="Solution Tools Download Video Tiktok Without Watermark & Youtub, Instagram and Facebook MP3 & MP4 Free 2026 | تحميل فيديوهات تيك توك بدون علامة مائية ،يوتيوب ،انستقرام و فايسبوك MP3 & MP4 مجانا 2026",
    page_icon="⚡",
    layout="wide",
)
st.markdown(
    f"""
    <script>
        var meta = document.createElement('meta');
        meta.name = "google-site-verification";
        meta.content = "3OalxEE5eG8HR0bf8gzBbNvh3On5RUsweJteiJpdaTU";
        document.getElementsByTagName('head')[0].appendChild(meta);
    </script>
    """,
    unsafe_allow_html=True
)

# كود التحقق السحري - يضع الكود في "رأس" الصفحة رغماً عن القيود
# 3. عنوان الموقع الذي يراه الزوار
st.markdown("<h1 style='text-align: center; color: white;'>⚡ SOLUTION TOOLS DOWNLOAD VIDEO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>تحميل فيديوهات من جميع المنصات بسهولة</p>", unsafe_allow_html=True)

# --- 2. محرك الربح الخلفي (Popunder). ---
components.html("""<script type='text/javascript' src='//pl28514603.effectivegatecpm.com/c6/5f/8a/c65f8a139a9ffa5d8b03075f7821fd4c.js'></script>""", height=0)
ad_link = "https://www.effectivegatecpm.com/fnm1ha40cf?key=2e8e674cc5f9402c67e5a8277faee09d"
ad_banner_728 = "https://www.highperformanceformat.com/09fc5e7625238657d095f102f5be82d6/invoke.js" 
ad_banner_300 = "https://www.highperformanceformat.com/b2a26b7c867c1488c61726b4c12a9d78/invoke.js" 

# --- 3. تنسيق CSS المحسن ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .widget-box { 
        background: rgba(255,255,255,0.05); 
        border-radius: 15px; padding: 20px; border: 1px solid #333; text-align: center;
    }
    .button-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 15px;
        margin-top: 25px;
    }
    
    .dl-btn {
        padding: 20px;
        color: white !important;
        border-radius: 12px;
        font-weight: bold;
        text-decoration: none;
        text-align: center;
        font-size: 20px;
        transition: 0.3s;
        border: none;
        display: block;
    }
    
    .video-btn { background: linear-gradient(90deg, #238636, #2ea043); } /* أخضر للفيديو */
    .audio-btn { background: linear-gradient(90deg, #1f6feb, #388bfd); } /* أزرق للصوت */
    
    .dl-btn:hover { transform: translateY(-3px); filter: brightness(1.1); box-shadow: 0 5px 15px rgba(0,0,0,0.3); }
    </style>
""", unsafe_allow_html=True)

left_col, main_col, right_col = st.columns([1, 2, 1])

# العمود الأيسر: لعبة ذكاء داخلية (تخمين الرقم)
with left_col:
    st.markdown('<div class="widget-box"><h3>🎮 لغز الأرقام</h3>', unsafe_allow_html=True)
    st.write("حاول تخمين الرقم السري بين 1 و 100")
    if 'secret_number' not in st.session_state:
        import random
        st.session_state.secret_number = random.randint(1, 100)
    
    guess = st.number_input("ضع رقمك هنا:", min_value=1, max_value=100, key="guess_game")
    if st.button("تحقق"):
        if guess < st.session_state.secret_number: st.warning("أكبر بقليل!")
        elif guess > st.session_state.secret_number: st.warning("أصغر بقليل!")
        else: st.success("رائع! لقد فزت!")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # إعلان صغير تحت اللعبة لزيادة الربح
    components.html("""
        <div style="text-align:center;">
            <script type="text/javascript">
                atOptions = {'key' : '7cc90dc5d87cbec36c2f51ccaf5a3c54', 'format' : 'iframe', 'height' : 50, 'width' : 320, 'params' : {}};
            </script>
            <script type="text/javascript" src="//www.highperformanceformat.com/7cc90dc5d87cbec36c2f51ccaf5a3c54/invoke.js"></script>
        </div>
    """, height=70)
   
        # إضافة البنر 300x250 أسفل الأزرار مباشرة
    components.html("""
        <div style="text-align:center;">
            <script type="text/javascript">
                atOptions = {'key' : 'b2a26b7c867c1488c61726b4c12a9d78', 'format' : 'iframe', 'height' : 250, 'width' : 300, 'params' : {}};
                </script>
                <script type="text/javascript" src="//www.highperformanceformat.com/b2a26b7c867c1488c61726b4c12a9d78/invoke.js"></script>
            </div>
        """, height=260)    

# --- العمود الأوسط: المحتوى الرئيسي والإعلانات ---
with main_col:
    st.markdown('<div class="header-box"><h1 style="color:#FF4B4B; font-size: 45px; margin:0;">⚡ SOLUTION TOOLS DOWNLOAD VIDEO</h1><p style="color:#888;">Professional Media Downloader</p></div>', unsafe_allow_html=True)
    
    # البانر العلوي (728x90) مع ارتفاع كافٍ لمنع القص
    components.html("""
        <div style="text-align:center;">
            <script type="text/javascript">
                atOptions = {'key' : '09fc5e7625238657d095f102f5be82d6', 'format' : 'iframe', 'height' : 90, 'width' : 728, 'params' : {}};
            </script>
            <script type="text/javascript" src="//www.highperformanceformat.com/09fc5e7625238657d095f102f5be82d6/invoke.js"></script>
        </div>
    """, height=110)

    url = st.text_input("", placeholder="ENTRER الصق رابط الفيديو هنا للبدء(يوتيوب، تيك توك، انستقرام، فيسبوك) و اضغط على")
    if url:
        st.video(url)
        encoded_url = urllib.parse.quote(url)
        target_url = f"https://downr.org/#url={url}"     
        
        st.markdown(f"""
            <div class="button-container">
                <a href="{target_url}" onclick="window.open('{ad_link}', '_blank');" class="dl-btn video-btn">
                    🎬 تحميل MP4 (فيديو)
                </a>
                <a href="{target_url}" onclick="window.open('{ad_link}', '_blank');" class="dl-btn audio-btn">
                    🎵 تحميل MP3 (صوت)
                </a>
            </div>
            <p style="text-align:center; color:#8b949e; margin-top:20px; font-size:13px;">
                * سيتم نقلك مباشرة لاستخراج الجودة المطلوبة بعد ظهور الإعلان.
            </p>
        """, unsafe_allow_html=True)

# --- الجانب الأيمن (لعبة الألوان الحقيقية) ---
with right_col:
    st.markdown('<div class="widget-box"><h3>🎨 لعبة الألوان</h3>', unsafe_allow_html=True)
    components.html("""
        <div id="status" style="color:#FF4B4B; font-weight:bold; margin-bottom:10px;">تذكر اللون الذي سيضيء!</div>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
            <button id="btn0" onclick="press(0)" class="color-btn" style="background:#ff4b4b; opacity:0.6;"></button>
            <button id="btn1" onclick="press(1)" class="color-btn" style="background:#28a745; opacity:0.6;"></button>
            <button id="btn2" onclick="press(2)" class="color-btn" style="background:#007bff; opacity:0.6;"></button>
            <button id="btn3" onclick="press(3)" class="color-btn" style="background:#ffc107; opacity:0.6;"></button>
        </div>
        <button onclick="playRound()" style="width:100%; margin-top:15px; padding:10px; cursor:pointer;">ابدأ الجولة</button>
        
        <script>
        let target = 0;
        function playRound() {
            target = Math.floor(Math.random() * 4);
            const btn = document.getElementById('btn' + target);
            btn.style.opacity = "1";
            btn.style.boxShadow = "0 0 20px white";
            document.getElementById('status').innerText = "تذكر اللون...";
            setTimeout(() => { 
                btn.style.opacity = "0.6"; 
                btn.style.boxShadow = "none";
                document.getElementById('status').innerText = "أي لون أضاء؟";
            }, 600);
        }
        function press(id) {
            if(id === target) {
                alert("إجابة صحيحة! 🎉");
                document.getElementById('status').innerText = "رائع! جولة جديدة؟";
            } else {
                alert("خطأ! ركز أكثر ❌");
            }
        }
        </script>
        <style>
        .color-btn { height: 70px; border: none; border-radius: 8px; cursor: pointer; transition: 0.3s; }
        </style>
    """, height=350)
    st.markdown('</div>', unsafe_allow_html=True)

    # تكرار إعلان 320x50 لضمان الربح من الجانب الآخر أيضاً
    components.html("""
        <div style="text-align:center;">
            <script type="text/javascript">
                atOptions = {'key' : '7cc90dc5d87cbec36c2f51ccaf5a3c54', 'format' : 'iframe', 'height' : 50, 'width' : 320, 'params' : {}};
            </script>
            <script type="text/javascript" src="//www.highperformanceformat.com/7cc90dc5d87cbec36c2f51ccaf5a3c54/invoke.js"></script>
        </div>
    """, height=70)

# --- 5. مقال الـ SEO في الأسفل (لجوجل) ---

# هذا الجزء هو ما سيجعل جوجل يضعك في النتيجة الأولى
st.markdown("""
    <div style="margin-top: 50px; padding: 30px; background: rgba(0,0,0,0.2); border-radius: 15px; direction: rtl; text-align: right;">
        <h2 style="color: #38bdf8;">أفضل أداة تنزيل فيديوهات أونلاين مجاناً</h2>
        <p>يعتبر موقع <b>Solution Tools</b> الثورة الجديدة في عالم <b>تحميل الملتيميديا</b>. إذا كنت تتساءل عن <i>  كيفية تحميل فيديوهات تيك توك بدون علامة مائية، يوتيوب، فيسبوك، إنستقرام، وتويتر</i>، فقد وصلت إلى المكان الصحيح.</p>
        
        <h3>مميزات خدمة التحميل لدينا:</h3>
        <ul>
            <li><b>دعم جميع المنصات:</b> تحميل من تيك توك، يوتيوب، فيسبوك، إنستقرام، وتويتر.</li>
            <li><b>جودات متعددة:</b> نوفر لك جودة 1080p و 4K بضغطة زر.</li>
            <li><b>تحويل MP3:</b> أسرع محول فيديو إلى MP3 بجودة صوت نقية 320kbps.</li>
        </ul>
        
        <p>لا تحتاج لتثبيت برامج؛ موقعنا يعمل مباشرة على المتصفح للآيفون والأندرويد والكمبيوتر. استمتع بتجربة <b>تنزيل فيديو</b> سريعة وآمنة تماماً.</p>
    </div>
""", unsafe_allow_html=True)

GA_JS = """
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3K920TRWE2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-3K920TRWE2');
</script>
"""

st.components.v1.html(GA_JS, height=0)


