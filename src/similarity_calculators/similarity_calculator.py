from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING

import numpy as np


if TYPE_CHECKING:
    from src.Config import Config


class SimilarityCalculator(ABC):
    @abstractmethod
    def calculate_similarity(
        self, embeddings: np.ndarray, config: "Config"
    ) -> np.ndarray:
        """
        Calculates the similarity between given embeddings based on the
        provided configuration.
        :param embeddings: A NumPy array containing the embeddings to compare.
        :param config: An instance of Config that contains parameters for the
        similarity calculation.
        :return: An array of similarity scores.
        """
        raise NotImplementedError
