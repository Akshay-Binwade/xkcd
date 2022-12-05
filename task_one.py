"""
CLI tool to fetch data from "https://xkcd.com/"

python task_one.py --max 87  --any 15
"""

import argparse
import random
from random import randrange
from typing import List

# breakpoint()
def get_range(start: int=1, stop: int=87, limit: int=15) -> list[int]:
    '''
    Args:
        start(int): first numeric value of range
        stop(int): last numeric value of range
        limit(int): number of values to be returned

    return:
        list[int]: a list of random numbers between (start, stop) with count of `limit`
    '''
    random_ = [random.randrange(start,stop+1) for i in range(limit)]
    return random_

if __name__ == "__main__":
    example = """example:
    
    python task_one.py --max 87  --any 15
    """

    parser = argparse.ArgumentParser(
        description="CLI tool to fetch resource(s) from API",
        epilog=example
    )

    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=87,
        help="max number of resources to be fetched"
    )

    parser.add_argument(
        "-a",
        "--any",
        type=int,
        default=15,
        help="random sized chunck of resources to be fetched"
    )

    args = parser.parse_args()
    print(args.any)
    print(args.max)


    comic_number_set = get_range(1, args.max, args.any)
    print(comic_number_set)