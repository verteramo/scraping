# @verteramo
# Joins all json files in a directory into a single json file

import argparse, os, json


def get_args():
    parser = argparse.ArgumentParser(description="Scraps tests")
    parser.add_argument("-d", "--directory", type=str)
    parser.add_argument("-o", "--output", type=str, default="output.json")
    return parser.parse_args()


def main(directory, output):
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                data.update(json.load(file))

    with open(output, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main(**vars(get_args()))
