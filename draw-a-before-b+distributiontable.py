import argparse
import math
import random


def calculate(tiles_remaining, tiles, iterations):
    if tiles_remaining < tiles['A'] + tiles['B'] + tiles['C']:
        raise ValueError(
            "tiles_remaining < tiles['A'] + tiles['B'] + tiles['C']")

    tile_list = ['A'] * tiles['A'] + ['B'] * tiles['B'] + ['C'] * tiles['C'] + \
        ['N'] * (tiles_remaining - tiles['A'] - tiles['B'] - tiles['C'])
    half = math.ceil(tiles_remaining / 2)
    index = {"A": 0, "B": 0, "C": 0}
    successes = {"A": 0, "B": 0}
    waits = {"countA": 0, "sumA": 0, "countB": 0, "sumB": 0}
    tiles_drawn = {
        "AA": {},
        "AC": {},
        "AAC": {},
        "BB": {},
        "BC": {},
        "BBC": {}}
    for i in range(0, tiles['A'] + tiles['C'] + 1):
        tiles_drawn['AA'][i] = 0
        tiles_drawn['AC'][i] = 0
        tiles_drawn['AAC'][i] = 0
    for i in range(0, tiles['B'] + tiles['C'] + 1):
        tiles_drawn['BB'][i] = 0
        tiles_drawn['BC'][i] = 0
        tiles_drawn['BBC'][i] = 0
    for _ in range(iterations):
        random.shuffle(tile_list)
        tile_list_a = tile_list[:half]
        tile_list_b = tile_list[half:tiles_remaining]
        index['A'] = tile_list_a.index('A') if "A" in tile_list_a \
            else tiles_remaining + 1
        index['C'] = tile_list_a.index('C') if "C" in tile_list_a \
            else tiles_remaining + 1
        index['A'] = min(index['A'], index['C'])
        tiles_drawn['AA'][tile_list_a.count('A')] += 1
        tiles_drawn['AC'][tile_list_a.count('C')] += 1
        tiles_drawn['AAC'][
            tile_list_a.count('A') +
            tile_list_a.count('C')] += 1
        index['B'] = tile_list_b.index('B') if "B" in tile_list_b \
            else tiles_remaining + 1
        index['C'] = tile_list_b.index('C') if "C" in tile_list_b \
            else tiles_remaining + 1
        index['B'] = min(index['B'], index['C'])
        tiles_drawn['BB'][tile_list_b.count('B')] += 1
        tiles_drawn['BC'][tile_list_b.count('C')] += 1
        tiles_drawn['BBC'][
            tile_list_b.count('B') +
            tile_list_b.count('C')] += 1
        if min(index['A'], index['B']) < tiles_remaining:
            if index['A'] <= index['B']:
                waits['countA'] += 1
                waits['sumA'] += index['A']
                successes['A'] += 1
            else:
                waits['countB'] += 1
                waits['sumB'] += index['B']
                successes['B'] += 1

    probability = {
        "A": successes['A'] / iterations,
        "B": successes['B'] / iterations}
    avg_wait = {
        "A": waits['sumA'] / waits['countA'] if waits['countA'] else 0,
        "B": waits['sumB'] / waits['countB'] if waits['countB'] else 0}
    tiles_drawn_prob = {
        'AA': {key: value / iterations for key, value in tiles_drawn['AA'].items()},
        'AC': {key: value / iterations for key, value in tiles_drawn['AC'].items()},
        'AAC': {key: value / iterations for key, value in tiles_drawn['AAC'].items()},
        'BB': {key: value / iterations for key, value in tiles_drawn['BB'].items()},
        'BC': {key: value / iterations for key, value in tiles_drawn['BC'].items()},
        'BBC': {key: value / iterations for key, value in tiles_drawn['BBC'].items()}}

    return probability, avg_wait, tiles_drawn_prob


def main(tiles_remaining, tiles, iterations):
    probability, avg_wait, tiles_drawn_prob = calculate(
        tiles_remaining, tiles, iterations)

    print(f"A draws 1 out of {tiles['A'] + tiles['C']} before B: {probability['A']*100:6.2f}%")
    print(f"B draws 1 out of {tiles['B'] + tiles['C']} before A: {probability['B']*100:6.2f}%")
    print(f"neither draws successfully:  {(1 - probability['A'] - probability['B'])*100:6.2f}%")
    print(f"moves to wait on average A:  {avg_wait['A']:6.2f}")
    print(f"moves to wait on average B:  {avg_wait['B']:6.2f}")
    print(f"tiles   A:A     A:C     A:A&C   B:B     B:C     B:B&C")
    for i in range(0, max(tiles['A'] + tiles['C'],
                          tiles['B'] + tiles['C']) + 1):
        print(f"{i:2d}{tiles_drawn_prob['AA'].get(i, 0) * 100:10.2f}%"
              f"{tiles_drawn_prob['AC'].get(i, 0) * 100:7.2f}%"
              f"{tiles_drawn_prob['AAC'].get(i, 0) * 100:7.2f}%"
              f"{tiles_drawn_prob['BB'].get(i, 0) * 100:7.2f}%"
              f"{tiles_drawn_prob['BC'].get(i, 0) * 100:7.2f}%"
              f"{tiles_drawn_prob['BBC'].get(i, 0) * 100:7.2f}%")

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
        default=0,
        help="Number of positive tiles for player A remaining.")
    parser.add_argument(
        "-b", "--tiles_b",
        type=int,
        default=0,
        help="Number of positive tiles for player B remaining. If TILES_B = 0 then players flip for TILES_A tiles.")
    parser.add_argument(
        "-c", "--tiles_c",
        type=int,
        default=1,
        help="Number of positive tiles for both players. Set TILES_A and TILES_B to 0 to let both players flip for a specific number of tiles.")
    parser.add_argument(
        "-i", "--iterations",
        type=int,
        default=100000,
        help="Number of simulation iterations.")
    args = parser.parse_args()

    main(
        tiles_remaining=args.tiles_remaining,
        tiles={"A": args.tiles_a, "B": args.tiles_b, "C": args.tiles_c},
        iterations=args.iterations)
