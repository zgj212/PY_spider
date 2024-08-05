
#https://www.pearvideo.com/category_1 原网站

#视频的url 经过处理  需要拼接
import requests
import os

url = "https://www.pearvideo.com/video_1795594"
video_id = url.split("_")[1]

video_status_url = f"https://www.pearvideo.com/videoStatus.jsp?contId={video_id}&mrd=0.5404765338953266"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "referer": url
}

try:
    resp = requests.get(url=video_status_url, headers=headers)
    resp.raise_for_status()  # 检查请求是否成功
except requests.RequestException as e:
    print(f"请求失败: {e}")
    exit()

dict = resp.json()

systemTime = dict["systemTime"]
srcUrl = dict["videoInfo"]["videos"]["srcUrl"]

srcUrl = srcUrl.replace(systemTime, f"cont-{video_id}")

video_file_name = f"梨视频1_{video_id}.mp4"
video_file_name = os.path.join("downloads", video_file_name)
os.makedirs("downloads", exist_ok=True)

with open(video_file_name, "wb") as f:
    f.write(requests.get(srcUrl).content)

print(f"视频已保存到 {video_file_name}")