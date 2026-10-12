"""
Media download and extraction functionality
"""
from typing import Dict, Any, Optional
import yt_dlp
import os
from pathlib import Path

def extract_media_info(url: str) -> Dict[str, Any]:
    """
    Extract media information from a URL using yt-dlp.
    
    Args:
        url: The URL to extract information from
        
    Returns:
        Dictionary containing media information
    """
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Extract formats
            formats = []
            if 'formats' in info:
                for fmt in info['formats']:
                    format_info = {
                        'format_id': fmt.get('format_id'),
                        'ext': fmt.get('ext'),
                        'quality': fmt.get('quality'),
                        'filesize': fmt.get('filesize'),
                        'is_audio_only': fmt.get('vcodec') == 'none',
                    }
                    formats.append(format_info)
            
            # Add MP3 audio option
            formats.append({
                'format_id': 'mp3_320',
                'ext': 'mp3',
                'quality': 320,
                'is_audio_only': True,
            })
            
            return {
                'success': True,
                'title': info.get('title', 'Unknown'),
                'duration': info.get('duration'),
                'uploader': info.get('uploader'),
                'thumbnail': info.get('thumbnail'),
                'is_video': info.get('vcodec') != 'none',
                'formats': formats,
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
        }

def perform_download(
    url: str,
    download_type: str = "video",
    quality: str = "best",
    custom_title: Optional[str] = None
) -> Dict[str, Any]:
    """
    Download media from a URL.
    
    Args:
        url: The URL to download from
        download_type: Type of download (video, audio, image)
        quality: Quality setting (best, 1080p, 720p, mp3_320, etc.)
        custom_title: Custom filename (optional)
        
    Returns:
        Dictionary containing download result
    """
    try:
        output_dir = Path("downloads")
        output_dir.mkdir(exist_ok=True)
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'outtmpl': str(output_dir / f'{custom_title or "%(title)s"}.%(ext)s'),
        }
        
        if download_type == "audio" or "mp3" in quality:
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320' if 'mp3_320' in quality else '192',
                }],
            })
        else:
            ydl_opts['format'] = 'best'
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            
            # For audio downloads, update extension to .mp3
            if download_type == "audio" or "mp3" in quality:
                filename = filename.rsplit('.', 1)[0] + '.mp3'
            
            filepath = Path(filename)
            
            return {
                'success': True,
                'filename': filepath.name,
                'filepath': str(filepath),
                'size_bytes': filepath.stat().st_size if filepath.exists() else 0,
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
        }
