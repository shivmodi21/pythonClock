from alarm import Alarm
from storage import AlarmStorage
from cli import create_parser
from scheduler import AlarmScheduler
import sys

parser = create_parser()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(0)

args = parser.parse_args()

storage = AlarmStorage()
storage.load()

if args.command == "add":
    try:
        alarm = Alarm.from_time_string(
            id=storage.next_id(),
            time_str=args.time,
            repeat=args.repeat,
        )

        storage.add_alarm(alarm)
        print(f"✓ Alarm added: {alarm}")

    except ValueError as e:
        print(f"Error: {e}")

elif args.command == "list":
    alarms = storage.get_all_alarms()

    if not alarms:
        print("No alarms found.")
    else:
        print("Current Alarms:")
        for alarm in alarms:
            print(alarm)

elif args.command == "remove":
    if storage.remove_alarm(args.id):
        print("Alarm removed.")
    else:
        print("Alarm not found.")

elif args.command == "run":
    scheduler = AlarmScheduler(storage)
    scheduler.start()