from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from yt_dlp import YoutubeDL
import os
import uvicorn

app = FastAPI()

class VideoRequest(BaseModel):
    url: str

def download_shorts_video(url: str):
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "Video downloaded successfully."

@app.post("/api/download")
async def download_video(request: VideoRequest):
    try:
        local_file_path = download_shorts_video(request.url)

        if not os.path.exists(local_file_path):
            raise HTTPException(status_code=404, detail="Video not found after download.")
        
        return FileResponse(
            path=local_file_path,
            media_type='video/mp4',
            filename=os.path.basename(local_file_path)
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    