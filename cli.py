# Basic command line interface for the program

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

    if args.add:
        vid = args.add
        try:
            r = requests.post("http://127.0.0.1:5000/api/videos",
                              json={"video": vid})
        except requests.exceptions.ConnectionError:  # Database connection error
            print("Error: Could not connect to the database. Is the server running?")
            sys.exit(1)

        # If the request was successful
        if r.status_code == 201:
            print("Video indexed successfully!")
        else:  # If the request was unsuccessful
            print("Error: ", r.status_code, r.reason)
            print("URL: ", r.url)
            sys.exit(1)

    if args.query and not args.add:
        query = args.query

        try:
            r = requests.post("http://127.0.0.1:5000/api/query",
                              json={"query": query})
        except requests.exceptions.ConnectionError:  # Database connection error
            print("Error: Could not connect to the database. Is the server running?")
            sys.exit(1)

        # res = requests.post("http://127.0.0.1:5000/api/query",
        #                     json={"query": query})

        # If the request was successful, print the results
        if r.status_code == 200:
            print("Video ID: ", r.json()["video_id"])
            print("Timestamps: ", str(r.json()["times"]))
        else:  # If the request was unsuccessful
            print("Error: ", r.status_code, r.reason)
            print("URL: ", r.url)
            sys.exit(1)


if __name__ == "__main__":
    main()
