import pandas as pd
from get_number_of_lines import get_number_of_lines
from tqdm import tqdm

def load_reviews(path, max_entries = None):
    
    print("Loading reviews from", path)
    number_of_lines = None # get_number_of_lines(path)
    print(f"Number of lines: {number_of_lines}")
    
    reviews = {
        "beer_id": [],
        "user_id": [],
        "date": [],
        "appearance": [],
        "abv": [],
        "aroma": [],
        "palate": [],
        "taste": [],
        "overall": [],
        "rating": [],
        "text": [],
    }

    with open(path, 'r', encoding='utf-8') as f:
        for index, line in enumerate(tqdm(f, total=number_of_lines)):
            if line.startswith("beer_id: "):
                reviews["beer_id"].append(int(line[len("beer_id: "):].strip()))
            elif line.startswith("user_id: "):
                reviews["user_id"].append(line[len("user_id: "):].strip())
            elif line.startswith("date: "):
                reviews["date"].append(float(line[len("date: "):].strip()))
            elif line.startswith("appearance: "):
                reviews["appearance"].append(float(line[len("appearance: "):].strip()))
            elif line.startswith("abv: "):
                reviews["abv"].append(float(line[len("abv: "):].strip()))
            elif line.startswith("aroma: "):
                reviews["aroma"].append(float(line[len("aroma: "):].strip()))
            elif line.startswith("palate: "):
                reviews["palate"].append(float(line[len("palate: "):].strip()))
            elif line.startswith("taste: "):
                reviews["taste"].append(float(line[len("taste: "):].strip()))
            elif line.startswith("overall: "):
                reviews["overall"].append(float(line[len("overall: "):].strip()))
            elif line.startswith("rating: "):
                reviews["rating"].append(float(line[len("rating: "):].strip()))
            elif line.startswith("text: "):
                reviews["text"].append(line[len("text: "):].strip())

            if isinstance(max_entries, int) and len(reviews["text"]) == max_entries:
                reviews = pd.DataFrame(reviews)
                reviews.sort_values(by=['date'], inplace=True)
                return reviews

    reviews = pd.DataFrame(reviews)
    reviews.sort_values(by=['date'], inplace=True)
    return reviews