from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    # raise NotImplementedError
    industries = set()
    for row in read(path):
        if row["industry"]:
            industries.add(row["industry"])
    return industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    # raise NotImplementedError
    filtered_by_industries = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_by_industries.append(job)
    return filtered_by_industries
