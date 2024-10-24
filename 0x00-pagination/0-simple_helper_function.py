#!/usr/bin/env python3
"""Simple helper function to calculate pagination indices"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive) and
        end index (exclusive) for the given page.
    """
    start_idx: int = (page - 1) * page_size
    end_idx: int = page * page_size

    return start_idx, end_idx
