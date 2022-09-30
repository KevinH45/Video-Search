# Basic command line interface for the program

import argparse
import sys
import requests


def main():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Simple search engine that can index YouTube videos and return relevant timestamps related to a query")

    # Add the arguments
    parser.add_argument("query", help="The query to search for")
    args = parser.parse_args()

    if args.query:
        query = args.query
        
        res = requests.post("http://127.0.0.1:5000/api/query",
                            json={"query": query})
        if res.status_code == 200:
            print(res.json())
        else:
            print("Error: ", res) # Bug: Return error message of 403 right now


if __name__ == "__main__":
    main()
