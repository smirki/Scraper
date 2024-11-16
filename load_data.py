```
import json
from typing import Any

def load_data(filename: str) -> None:
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            # update the current data with the loaded data
            # (this line is a placeholder, replace with your actual data update logic)
            print(f"Loaded data from {filename}: {data}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except json.JSONDecodeError as e:
        print(f"Error loading JSON file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
```