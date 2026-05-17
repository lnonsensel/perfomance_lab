import json
import sys


def read_file(path: str) -> dict:
    with open(path) as file:
        values = json.load(file)
    return values


def reformat_values(values: dict) -> dict:
    vals = values["values"]
    new_values = {}
    for val in vals:
        new_values[val["id"]] = val["value"]
    return new_values


def run_through_tests(tests: list[dict]):
    for test in tests:
        if "values" in test:
            yield from run_through_tests(test["values"])
        yield test


def main(values: dict, tests: dict, report_path: str) -> None:
    for test in run_through_tests(tests["tests"]):
        if test["id"] in values:
            test["value"] = values[test["id"]]
    with open(report_path, "w") as report:
        json.dump(tests, report, indent=1)


if __name__ == "__main__":
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    values = read_file(values_path)
    tests = read_file(tests_path)
    values = reformat_values(values)
    main(values, tests, report_path)
