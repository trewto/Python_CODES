from pytube import YouTube, Playlist

def get_download_links(video_url,p=1):
    yt = YouTube(video_url)
    streams = yt.streams.filter(progressive=True)
    
    print(f"Available Resolutions for '{yt.title}':")
    for i, stream in enumerate(streams):
        print(f"{p}.{i + 1}. Resolution: {stream.resolution}, Format: {stream.mime_type}")
        print(f"   Download link: {stream.url}")
        print("-----------------------------")
    
    return streams

print("Press 1 for a single video or 2 for a playlist: ")
i = int(input())
print ("GIve me the link")
link = input()

if i == 2:
    #playlist_url = 'https://www.youtube.com/playlist?list='
    playlist_url = link 
    playlist = Playlist(playlist_url)

    p =1 
    for video in playlist.video_urls:
        get_download_links(video,p)
        p += 1
else:
    #video_url = 'https://www.youtube.com/watch?v='
    video_url = link
    get_download_links(video_url)
