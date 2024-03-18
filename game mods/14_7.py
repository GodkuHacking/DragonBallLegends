# 14_7.py
# edits the character zenkai and stars to max!
# made by mindsetpro

from typing import Any, Dict
import json
import sys
from tqdm import tqdm
from colorama import init, Fore

init(autoreset=True)

def invert_bytes(filename: str) -> None:
    """
    Inverts the bytes of a file.

    Args:
        filename (str): The name of the file to invert its bytes.

    Returns:
        None
    """
    arr = bytearray()
    with open(filename, "rb") as f:
        for b in tqdm(f, desc="Inverting bytes", unit="byte"):
            arr += bytearray(b)
            for i in range(len(arr)):
                arr[i] = ~arr[i] + 256

    with open(filename, "wb") as f:
        f.write(arr)

def edit_counts(filename: str) -> None:
    """
    Edits the counts in a JSON file as described in the task.

    Args:
        filename (str): The name of the JSON file to edit.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        data: Dict[str, Any] = json.load(file)

    for item in tqdm(data["characterShards_"], desc="Editing stars", unit="character"):
        if "count" in item and 10 <= item["count"] <= 9998:
            item["count"] = 9999

    for item in tqdm(data["characterPlentyShards_"], desc="Editing zenkais", unit="character"):
        if "count" in item and 10 <= item["count"] <= 6999:
            item["count"] = 7000

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    invert_bytes(filename)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "[USAGE ERROR]: Usage: python 14_7.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    edit_counts(filename)
    print(Fore.GREEN + "[SUCCESS]: Counts edited successfully.")
