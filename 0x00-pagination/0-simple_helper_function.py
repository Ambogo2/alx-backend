#!/usr/bin/env python3
""" Simple helper function module"""


def index_range(page: int, page_size: int) -> tuple:
    """Calculate start and end indices"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
