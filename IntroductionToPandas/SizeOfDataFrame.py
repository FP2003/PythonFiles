import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    row = len(players)
    col = len(players.columns)
    return [row, col]