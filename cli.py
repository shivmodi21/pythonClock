import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="AlarmClock",
        description="A simple command-line alarm clock.",
        epilog="""
            Examples:
            python main.py add 07:30
            python main.py add 18:00 --repeat
            python main.py list
            python main.py remove 1
            python main.py run
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # add
    add_parser = subparsers.add_parser(
        "add",
        help="Add a new alarm"
    )
    add_parser.add_argument(
        "time",
        help="Alarm time in HH:MM format"
    )
    add_parser.add_argument(
        "--repeat",
        action="store_true",
        help="Repeat every day"
    )

    # list
    subparsers.add_parser(
        "list",
        help="List all alarms"
    )

    # remove
    remove_parser = subparsers.add_parser(
        "remove",
        help="Remove an alarm"
    )
    remove_parser.add_argument(
        "id",
        type=int,
        help="Alarm ID"
    )

    # run
    subparsers.add_parser(
        "run",
        help="Start the alarm scheduler"
    )

    return parser