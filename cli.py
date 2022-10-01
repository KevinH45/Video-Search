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
    parser.add_argument("--add", help="The video id to add")
    args = parser.parse_args()

    if args.add:
        vid = args.add
        res = requests.post("http://localhost:5000/api/video", json={"video": vid})

        print("Added to DB!")

    if args.query and not args.add:
        query = args.query
        
        res = requests.post("http://127.0.0.1:5000/api/query",
                            json={"query": query})
        if res.status_code == 200:

            for i,j in res.json().items():
                print(i,":",j)


        else:
            print("Error: ", res) # Bug: Return error message of 403 right now



if __name__ == "__main__":
    main()
