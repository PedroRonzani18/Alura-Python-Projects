from pathlib import Path


def partial_to_full_path(path):
    parent = Path(__file__).parent
    for _ in range(path.count('../')):
        parent = parent.parent
    return parent.joinpath(path.lstrip('../'))


print(partial_to_full_path("../csv/aluguel.csv"))
