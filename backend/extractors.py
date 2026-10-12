"""
Platform detection and extraction utilities
"""
import re
from typing import Optional

def detect_platform(url: str) -> Optional[str]:
    """
    Detect the platform from a given URL.
    
    Args:
        url: The URL to analyze
        
    Returns:
        Platform identifier (youtube, instagram, tiktok, etc.) or None
    """
    url = url.lower()
    
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    elif "instagram.com" in url:
        return "instagram"
    elif "tiktok.com" in url:
        return "tiktok"
    elif "reddit.com" in url:
        return "reddit"
    elif "facebook.com" in url or "fb.watch" in url:
        return "facebook"
    elif "twitter.com" in url or "x.com" in url:
        return "x"
    elif "threads.net" in url:
        return "threads"
    
    return None
