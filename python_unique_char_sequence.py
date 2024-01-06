# https://adventofcode.com/2022/day/6
import sys, subprocess

# catch if user didnt give argument
if len(sys.argv) > 1:
    buffer = sys.argv[1]
else:
    print(f"Usage: {sys.argv[0]} 'sequence'")
    quit()

i = 0
# NOTE: as the problem asks to find 4 chars, window=4
window = 4
while i < len(buffer):
    current = buffer[i:i+window]
    current_set = set(current)
    if len(current_set) == window:
        print(f"Found solution: '{current}' starting at index {i}. Answer {i+window}")
        break
    i += 1
