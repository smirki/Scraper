```
import json

def save_data(filename):
    with open(filename, 'w') as f:
        json.dump(your_data, f)