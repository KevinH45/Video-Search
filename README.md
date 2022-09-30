# Video Search

## Problem statement

Employees at companies often have to parse through a ton of information in documentation/JIRA/Confluence etc while building their new project. Reading so much documentation and "how to do X" can often be super boring though. With remote work, a lot of knowledge transfer and team discourse happens on video calls. Calls that are usually recorded on Zoom and archived. There is a ton of useful, bite-sized, "tutorial" information trapped in these zoom calls, which if extracted, could lead to companies creating their own "internal Youtubes of how to do XYZ".

## Existing solutions

There are a few existing solutions that do this, most notably what is built by Google: their search feature now have a 'highlight' on certain parts of a video when you search something that is part of a video/Google thinks the video is relevant. This is a great feature, but it's not open source.

## Solution

We propose a command line tool that can be used to extract the text from previously-indexed YouTube videos in our database and be able to search through the text and return the relevant timestamp where content of the query is present. This will allow employees to search through the text of the video and get the relevant timestamp where the content is present.

Here's a [YouTube demo](https://youtu.be/ZQ8ux00RJkw) of the code - please read the description for more details.

## Dependencies and resources

- [ShelfDB](https://github.com/nitipit/shelfdb)
- [YoutubeTranscriptAPI](https://github.com/jdepoix/youtube-transcript-api)
- [Scikit-Learn](https://scikit-learn.org/stable/index.html)
- [SentenceTransformers](https://huggingface.co/sentence-transformers/multi-qa-MiniLM-L6-cos-v1)
- Other dependencies can be found in `requirements.txt`
- YT Videos mostly from TedTalks, Tom Scott, and StatQuest (because of their high-quality subtitling and somewhat technical nature)

## Query Search Algorithm

The query search algorithm follows a few simple steps:

- Beforehand, we have saved a collection of YouTube transcripts in our document DB.
- We are given a query via a POST request to `/api/query`.
- As preprocessing, we remove all non-alphabetic characters and stem the query.
- We run the query through the collection of YT transcripts using TF-IDF Vectorization and Cosine Similarity. The document most similar to the query is selected as the "target" document.
- We use the Multi-QA MiniLM model to encode the individual spoken phrases and query.
- We use cosine similarity to determine the phrase most similar to the query, and reference the transcript to find an accurate time for the phrase.

## Usage guide

- Send a POST Request at `/api/videos` to submit a new video
- Send a POST Request at `/api/query` to search for a video + timestamps
