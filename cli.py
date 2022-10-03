import argparse
import sys
import requests


def main():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Simple search engine that can index YouTube videos and return relevant timestamps related to a query")

    # Add the arguments
    parser.add_argument("--query", help="The query to search for")
    parser.add_argument("--add", help="The video ID to index")
    args = parser.parse_args()

    # If the user doesn't provide any arguments, print the help message
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    # TODO: Add the ability to add a video to the index and search for a query

    if args.query:
        print(f"Searching for {args.query}...")

        try:
            response = requests.post(
                "http://127.0.0.1:5000/api/query", json={"query": args.query})
            response.raise_for_status()
        except requests.RequestException:
            print("An error occurred while querying!")
            sys.exit(1)

        results = response.json()
        if results:
            print("Video link: ", results["link"])
            print("Timestamps: ", results["times"])
        else:
            print("No results found! You can add a video to the index using --add")

    if args.add:
        print("Adding video: https://www.youtube.com/watch?v=" + args.add)

        try:
            response = requests.post(
                "http://localhost:5000/api/video", json={"video_id": args.add})
            response.raise_for_status()
        except requests.RequestException:
            print("An error occurred while adding the video!")
            sys.exit(1)

        print("Video added successfully!")


if __name__ == "__main__":
    main()
