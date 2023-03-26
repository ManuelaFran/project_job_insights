from src.pre_built.sorting import sort_by

jobs = [
    {"min_salary": 5000, "max_salary": 15000, "date_posted": "2016-08-09"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-10-01"},
    {"min_salary": 600, "max_salary": 1000, "date_posted": "2022-25-05"},
    {"min_salary": 2500, "max_salary": 5500, "date_posted": "2002-12-09"},
]


def test_sort_by_criteria():
    sorted_max = [
        {'min_salary': 5000, 'max_salary': 15000, 'date_posted': '2016-08-09'},
        {'min_salary': 2500, 'max_salary': 5500, 'date_posted': '2002-12-09'},
        {'min_salary': 2000, 'max_salary': 5000, 'date_posted': '2020-10-01'},
        {'min_salary': 600, 'max_salary': 1000, 'date_posted': '2022-25-05'}
    ]

    sort_by(jobs, "max_salary")
    assert jobs == sorted_max

    sorted_min = [
        {'min_salary': 600, 'max_salary': 1000, 'date_posted': '2022-25-05'},
        {'min_salary': 2000, 'max_salary': 5000, 'date_posted': '2020-10-01'},
        {'min_salary': 2500, 'max_salary': 5500, 'date_posted': '2002-12-09'},
        {'min_salary': 5000, 'max_salary': 15000, 'date_posted': '2016-08-09'}
    ]

    sort_by(jobs, "min_salary")
    assert jobs == sorted_min

    jobs_date_sorted = [
        {'min_salary': 2000, 'max_salary': 5000, 'date_posted': '2020-10-01'},
        {'min_salary': 5000, 'max_salary': 15000, 'date_posted': '2016-08-09'},
        {'min_salary': 2500, 'max_salary': 5500, 'date_posted': '2002-12-09'},
        {'min_salary': 600, 'max_salary': 1000, 'date_posted': '2022-25-05'}
    ]

    sort_by(jobs, "date_posted")
    assert jobs == jobs_date_sorted
