import json
import sys
import re


def load_json(file_path):
    """Loading Data from JSON"""
    with open(file_path, "r") as file:
        return json.load(file)


def save_json(data, file_path):
    """Formating and save resalt in file report.json"""
    with open(file_path, "w") as file:
        json_str = json.dumps(data, indent=2, separators=(",", ": "))
        # regular expressions
        json_str = re.sub(r"\[\s*\{", "[{", json_str)
        json_str = re.sub(r"\}\s*,\s*\{", "}, {", json_str)
        json_str = re.sub(r"\}\s*\]", "}]", json_str)
        json_str = re.sub(r"(\s{2})(\s{2})", r"\1", json_str)

        file.write(json_str)


def update_values(tests, values):
    """Updates the values in the tests structure based on data from values."""
    value_dict = {item["id"]: item["value"] for item in values["values"]}

    index = 0
    while index < len(tests["tests"]):
        test = tests["tests"][index]
        if "id" in test and test["id"] in value_dict:
            test["value"] = value_dict[test["id"]]
        if "values" in test:
            for nested_test in test["values"]:
                tests["tests"].append(nested_test)
        index += 1

    return tests


def main(values_file, tests_file, report_file):
    # Loading the data from the files
    values = load_json(values_file)
    tests = load_json(tests_file)

    # Update the values in the structure tests
    updated_tests = update_values(tests, values)

    # Save the updated structure to a file report.json
    save_json(updated_tests, report_file)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("USE: python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)
