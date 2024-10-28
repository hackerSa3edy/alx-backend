#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Tuple, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_idx: int = (page - 1) * page_size
    end_idx: int = page * page_size

    return start_idx, end_idx


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the Server instance.
        """
        self.__dataset: Optional[List[List]] = None
        self.__indexed_dataset: Optional[Dict[int, List]] = None
        self.__dataset_len: Optional[int] = None

    @property
    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: The cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)

                # Skip the header row
                self.__dataset = [row for row in reader][1:]
                self.__dataset_len = len(self.__dataset)

        return self.__dataset

    @property
    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create an indexed dataset by sorting position, starting at 0.

        Returns:
            Dict[int, List]: The indexed dataset.
        """
        if self.__indexed_dataset is None:
            self.__indexed_dataset = {i: row for i, row in enumerate(
                self.dataset
                )}
        return self.__indexed_dataset

    @property
    def dataset_len(self) -> int:
        """
        Get the length of the dataset.

        Returns:
            int: The length of the dataset.
        """
        if self.__dataset_len is None:
            self.__dataset_len = len(self.dataset)
        return self.__dataset_len

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Handle deletion of items when querying.

        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination information.
        """
        assert 0 <= index < self.dataset_len, "Index out of range."

        indexed_data_keys = sorted(self.indexed_dataset.keys())
        remaining_indices = [
            idx for idx in indexed_data_keys if idx >= index
        ][:page_size]
        data = [self.indexed_dataset[idx] for idx in remaining_indices]
        next_index = (remaining_indices[-1] + 1
                      if len(remaining_indices) == page_size
                      else None)

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
