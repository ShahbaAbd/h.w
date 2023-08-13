import pytube
videoUrl=input("Enter video Url: \n")
pytube.Youtube(videoUrl).stream.get_highest_resolution().download('Documents')
