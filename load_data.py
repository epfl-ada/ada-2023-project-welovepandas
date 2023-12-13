import gzip
import pandas as pd
from tqdm import tqdm


def load_gzip_txt_data(path: str, attributes: list[str], max_entries: int = None) -> pd.DataFrame:
    """
    Loads the data from a gzip file.
    Note: All columns are of type string, still need to cast them using 'df.astype'.

    :param path: str, the path where the gzip file is located.
    :param attributes: list of str, list of attributes that we want to retrieve.
    :param max_entries: int, number of lines to read. If None, all lines are read.
    :return: pd.Dataframe, a dataframe containing the data.
    """

    print("Loading data from: ", path)

    ratings = dict((attribute, []) for attribute in attributes)

    with gzip.open(path, 'rt', encoding='utf-8') as f:

        # Count the number of attributes of the current entry (used only for max_entry)
        entry_attribute = 0

        for line in tqdm(f):
            line_parts = line.split(":", 1)

            if line_parts[0] in attributes:
                ratings[line_parts[0]].append(line_parts[1].strip())
                entry_attribute = (entry_attribute + 1) % len(attributes)

            # If we want to use max_entry
            if max_entries is not None \
                    and len(ratings[attributes[0]]) == max_entries \
                    and entry_attribute == 0:
                break

    ratings = pd.DataFrame(ratings)
    return ratings
  