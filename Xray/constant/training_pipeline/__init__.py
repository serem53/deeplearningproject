from datetime import datetime
from typing import List

import torch

TIMESTAMP: datetime=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

################################################################

ARTIFACT_DIR: str="artifacts"

BUCKET_NAME: str="dl-xray-lung-project"

S3_DATA_FOLDER: str= "chest_xray"

CLASS_LABEL_1: str="NORMAL"

CLASS_LABEL_2: str = "PNEUMONIA"