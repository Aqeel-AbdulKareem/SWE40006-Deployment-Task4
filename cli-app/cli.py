import sys
import statistics

print("SWE40006 Statistics CLI")

if len(sys.argv) < 2:
    print("Usage: python cli.py 70 82 91 65")
    sys.exit(1)

try:
    numbers = [float(value) for value in sys.argv[1:]]
except ValueError:
    print("Error: all values must be numbers.")
    sys.exit(1)

print(f"Values processed: {len(numbers)}")
print(f"Minimum: {min(numbers):.2f}")
print(f"Maximum: {max(numbers):.2f}")
print(f"Average: {statistics.mean(numbers):.2f}")
print(f"Median: {statistics.median(numbers):.2f}")