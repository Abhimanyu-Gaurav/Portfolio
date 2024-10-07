from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Portfolio</title>
        <style>
            body { text-align: center; padding: 50px; font-family: Arial, sans-serif; background-color: #f8f9fa; }
            h1 { font-size: 2.5em; color: #333; }
            p { font-size: 1.2em; color: #666; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; }
            blockquote { font-style: italic; margin: 20px 0; }
        </style>

        <!-- Google Analytics Tracking Code -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-WZSK913Q88"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-WZSK913Q88');  <!-- Update this with your tracking ID -->
        </script>
    </head>
    <body>
        <h1>👋 Hi, I'm Abhimanyu Kumar Gaura V!</h1>
        <p>🌍 A passionate Software Developer based in Delhi, skilled in Python, FastAPI, and web scraping.</p>
        <p>💻 I specialize in building data-driven applications and automation tools.</p>

        <h2>Projects</h2>
        <ul>
            <li><strong>Google Maps Scraper Tool:</strong> An automated tool to scrape business data from Google Maps using Python and FastAPI.</li>
            <li><strong>Web Scraper Tool:</strong> A web scraper built with FastAPI and BeautifulSoup for data automation.</li>
            <li><strong>To-Do List Application:</strong> A CRUD API built with FastAPI and Docker.</li>
        </ul>

        <h2>Blogs</h2>
        <p>Coming soon...</p>

        <h2>Testimonials</h2>
        <p>What my clients say:</p>
        <blockquote>"Abhimanyu did an excellent job!"</blockquote>

        <h2>Contact Information</h2>
        <p>📧 Contact: <a href="mailto:kr.abhi.gaurav11@gmail.com">kr.abhi.gaurav11@gmail.com</a></p>
    </body>
    </html>
    """
