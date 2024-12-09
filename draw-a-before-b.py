import argparse
import math
import random


def calculate(tiles_remaining, tiles, iterations):
    if tiles_remaining < tiles['A'] + tiles['B']:
        raise ValueError("tiles_remaining < tiles['A'] + tiles['B']")

    tile_list = ['A'] * tiles['A'] + ['B'] * tiles['B'] + \
        ['N'] * (tiles_remaining - tiles['A'] - tiles['B'])
    half = math.ceil(tiles_remaining / 2)
    successes = {"A": 0, "B": 0}
    waits = {"countA": 0, "sumA": 0, "countB": 0, "sumB": 0}

    for _ in range(iterations):
        random.shuffle(tile_list)
        if tiles['B']:
            tile_list_a = tile_list[:half]
            tile_list_b = tile_list[half:tiles_remaining]
            if "A" in tile_list_a:
                if "B" in tile_list_b[:tile_list_a.index("A")]:
                    waits['countB'] += 1
                    waits['sumB'] += tile_list_b.index("B")
                    successes['B'] += 1
                else:
                    waits['countA'] += 1
                    waits['sumA'] += tile_list_a.index("A")
                    successes['A'] += 1
            elif "B" in tile_list_b:
                waits['countB'] += 1
                waits['sumB'] += tile_list_b.index("B")
                successes['B'] += 1
        elif tile_list.index("A") % 2 == 0:
            waits['countA'] += 1
            waits['sumA'] += tile_list.index("A") / 2
            successes['A'] += 1
        else:
            waits['countB'] += 1
            waits['sumB'] += tile_list.index("A") / 2
            successes['B'] += 1

    probability = {
        "A": successes['A'] / iterations,
        "B": successes['B'] / iterations}
    avg_wait = {
        "A": waits['sumA'] / waits['countA'] if waits['countA'] else 0,
        "B": waits['sumB'] / waits['countB'] if waits['countB'] else 0}

    return probability, avg_wait


def main(tiles_remaining, tiles, iterations):
    probability, avg_wait = calculate(tiles_remaining, tiles, iterations)

    print(f"A draws 1 out of {tiles['A']} before B: {probability['A']:9.5f}")
    print(f"B draws 1 out of {tiles['B'] if tiles['B'] else tiles['A']} before A: {probability['B']:9.5f}")
    if tiles['B']:
        print(f"neither draws successfully:  {1 - probability['A'] - probability['B']:9.5f}")
    print(f"moves to wait on average A:  {avg_wait['A']:9.5f}")
    print(f"moves to wait on average B:  {avg_wait['B']:9.5f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="simulates (2p Carcassonne) tile draws and prints stats",
        epilog="Player A is the next player to draw a tile – so not necessarily the starting player.")
    parser.add_argument(
        "-t", "--tiles_remaining",
        type=int,
        default=71,
        help="Number of total tiles remaining.")
    parser.add_argument(
        "-a", "--tiles_a",
        type=int,
        default=1,
        help="Number of positive tiles for player A remaining.")
    parser.add_argument(
        "-b", "--tiles_b",
        type=int,
        default=0,
        help="Number of positive tiles for player B remaining. If TILES_B = 0 then players flip for TILES_A tiles.")
    parser.add_argument(
        "-i", "--iterations",
        type=int,
        default=100000,
        help="Number of simulation iterations.")
    args = parser.parse_args()

    main(
        tiles_remaining=args.tiles_remaining,
        tiles={"A": args.tiles_a, "B": args.tiles_b},
        iterations=args.iterations)
