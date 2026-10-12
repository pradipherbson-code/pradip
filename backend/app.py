"""
OmniStream FastAPI Backend with Vercel Speed Insights
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path

app = FastAPI(
    title="OmniStream Downloader API",
    description="Multi-Platform Social Media & MP3 Downloader",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/api/health")
async def health_check():
    """Health check endpoint for deployment monitoring"""
    return {
        "status": "healthy",
        "service": "omnistream-downloader",
        "version": "1.0.0"
    }

# Platforms endpoint
@app.get("/api/platforms")
async def get_platforms():
    """List supported platforms"""
    return {
        "platforms": [
            {"name": "YouTube", "id": "youtube", "features": ["video", "audio"]},
            {"name": "Instagram", "id": "instagram", "features": ["video", "images", "reels"]},
            {"name": "TikTok", "id": "tiktok", "features": ["video", "audio"]},
            {"name": "Reddit", "id": "reddit", "features": ["video", "images"]},
            {"name": "Facebook", "id": "facebook", "features": ["video", "images"]},
            {"name": "X/Twitter", "id": "x", "features": ["video", "images"]},
            {"name": "Threads", "id": "threads", "features": ["video", "images"]},
        ]
    }

# Main page with Vercel Speed Insights integrated
@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Main application page with Vercel Speed Insights integration.
    
    Speed Insights is configured according to Vercel's HTML5 quickstart guide:
    https://vercel.com/docs/speed-insights/quickstart
    """
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OmniStream - Multi-Platform Downloader</title>
    <meta name="description" content="Download videos, images, and audio from YouTube, Instagram, TikTok, Reddit, Facebook, X/Twitter, and Threads">
    
    <!-- Vercel Speed Insights -->
    <script>
        window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/speed-insights/script.js"></script>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            max-width: 800px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }
        
        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 2.5em;
            text-align: center;
        }
        
        .subtitle {
            color: #666;
            text-align: center;
            margin-bottom: 30px;
            font-size: 1.1em;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        
        .feature {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s ease;
        }
        
        .feature:hover {
            transform: translateY(-5px);
        }
        
        .feature h3 {
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        
        .status {
            background: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
            margin-top: 30px;
            text-align: center;
        }
        
        .status-badge {
            display: inline-block;
            background: #22c55e;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
            margin-top: 10px;
        }
        
        .info {
            background: #e0f2fe;
            border-left: 4px solid #0284c7;
            padding: 15px;
            margin-top: 20px;
            border-radius: 5px;
        }
        
        .info p {
            color: #0c4a6e;
            line-height: 1.6;
        }
        
        .api-link {
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }
        
        .api-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ OmniStream</h1>
        <p class="subtitle">Multi-Platform Social Media & MP3 Downloader</p>
        
        <div class="info">
            <p>
                <strong>🚀 Vercel Speed Insights Enabled!</strong><br>
                This application now monitors real-world performance metrics to ensure the best user experience.
            </p>
        </div>
        
        <div class="features">
            <div class="feature">
                <h3>📺 YouTube</h3>
                <p>Videos, Shorts & MP3</p>
            </div>
            <div class="feature">
                <h3>📸 Instagram</h3>
                <p>Reels, Posts & Carousels</p>
            </div>
            <div class="feature">
                <h3>🎵 TikTok</h3>
                <p>HD No Watermark</p>
            </div>
            <div class="feature">
                <h3>🔴 Reddit</h3>
                <p>Videos & Galleries</p>
            </div>
            <div class="feature">
                <h3>📘 Facebook</h3>
                <p>Videos & Photos</p>
            </div>
            <div class="feature">
                <h3>🐦 X/Twitter</h3>
                <p>Videos & Images</p>
            </div>
        </div>
        
        <div class="status">
            <h3>API Status</h3>
            <div class="status-badge">✓ Operational</div>
            <p style="margin-top: 15px; color: #666;">
                API Documentation: <a href="/api/platforms" class="api-link">/api/platforms</a> | 
                <a href="/api/health" class="api-link">/api/health</a>
            </p>
        </div>
    </div>
    
    <script>
        // Check API health on page load
        fetch('/api/health')
            .then(response => response.json())
            .then(data => {
                console.log('API Health Check:', data);
                // Speed Insights will automatically track page performance
            })
            .catch(error => {
                console.error('API Health Check Failed:', error);
            });
    </script>
</body>
</html>
    """
    return HTMLResponse(content=html_content)

# Favicon endpoint to prevent 404 errors
@app.get("/favicon.ico")
async def favicon():
    """Return empty response for favicon requests"""
    return JSONResponse(content={}, status_code=204)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
