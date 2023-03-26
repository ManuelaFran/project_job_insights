from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    assert count_ocurrences(path, 'Python') == 44
    assert count_ocurrences(path, 'python') == 44
    assert count_ocurrences(path, 'Javascript') == 22
    assert count_ocurrences(path, 'javascript') == 22
