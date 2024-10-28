#!/usr/bin/env python3
"""Implement Hypermedia pagination"""

import csv
import math
from typing import Tuple, List, Dict, Optional


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
    def dataset_len(self) -> int:
        """
        Get the length of the dataset.

        Returns:
            int: The length of the dataset.
        """
        if self.__dataset_len is None:
            self.__dataset_len = len(self.dataset)
        return self.__dataset_len

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows for the specified page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_idx, end_idx = index_range(page, page_size)
        return self.dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get the hypermedia pagination information for the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination information.
        """
        data = self.get_page(page, page_size)
        start_idx, end_idx = index_range(page, page_size)

        return {
            'page_size': page_size if len(data) != 0 else 0,
            'page': page,
            'data': data,
            'next_page': page + 1 if end_idx < self.dataset_len else None,
            'prev_page': page - 1 if start_idx > 0 else None,
            'total_pages': math.ceil(self.dataset_len / page_size)
        }
