import time
from datetime import datetime


class AlarmScheduler:
    def __init__(self, storage):
        self.storage = storage
        self.triggered = set()

    def start(self):
        print("Alarm Clock Started")
        print("Press Ctrl+C to stop.\n")

        try:
            while True:
                now = datetime.now()
                current = (now.hour, now.minute)

                for alarm in self.storage.get_all_alarms():

                    if not alarm.enabled:
                        continue

                    alarm_time = (alarm.hour, alarm.minute)

                    if current == alarm_time:

                        # Prevent multiple rings within the same minute
                        if alarm.id in self.triggered:
                            continue

                        self.triggered.add(alarm.id)

                        print("\n" + "=" * 40)
                        print("⏰ ALARM!")
                        print(f"Time: {alarm.time_str}")
                        print("=" * 40)
                        print("\a")

                        if not alarm.repeat:
                            alarm.enabled = False
                            self.storage.save()

                    else:
                        # Allow alarm to trigger again after the minute passes
                        self.triggered.discard(alarm.id)

                time.sleep(1)

        except KeyboardInterrupt:
            print("\nAlarm Clock Stopped")