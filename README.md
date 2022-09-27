# Video Search

## Slingshot Description
After helping lawyers with NLP, we're back with this week's challenge. This challenge is very near and dear to my heart. Hopefully you have fun building something very cool (imo), open source it, win an Amazon cash prize, and get SLINGSHOT VERIFIED 

### 🟣 Context/Problem 🟣 
Employees at companies often have to parse through a ton of information in documentation/JIRA/Confluence etc while building their new project. Reading so much documentation and "how to do X" can often be super boring though. 

### 🟡 Opportunity 🟡
 With remote work, a lot of knowledge transfer and team discourse happens on video calls. Calls that are usually recorded on Zoom and archived. There is a ton of useful, bite-sized, "tutorial" information trapped in these zoom calls, which if extracted, could lead to companies creating their own "internal Youtubes of how to do XYZ"

## Tech Used:
HUGE Credit to:
- [ShelfDB](https://github.com/nitipit/shelfdb)
- [YoutubeTranscriptAPI](https://github.com/jdepoix/youtube-transcript-api)
- [Scikit-Learn](https://scikit-learn.org/stable/index.html)

## Usage Guide:
- Send a POST Request at ```/api/videos``` to submit a new video
- Send a POST Request at ```/api/query``` to search for a video + timestamps