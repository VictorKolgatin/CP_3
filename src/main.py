from pprint import pprint

from src.utils import load_file, executed_last_operations, format_operation

FILENAME = "operations.json"
count_last_operation = 5


def main():
    operations_file = load_file(FILENAME)
    last_operation = executed_last_operations(operations_file, count_last_operation)
    return format_operation(last_operation)


pprint(main())
