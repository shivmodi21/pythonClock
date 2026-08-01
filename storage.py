import json
import os
from alarm import Alarm


class AlarmStorage:
    def __init__(self, filename="alarms.json"):
        self.filename = filename
        self.alarms = []

    def load(self):
        """
        Load alarms from the JSON file into self.alarms.
        """
        if not os.path.exists(self.filename):
            self.alarms = []
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.alarms = [Alarm.from_dict(item) for item in data]

        except (json.JSONDecodeError, FileNotFoundError):
            self.alarms = []

    def save(self):
        """
        Save all alarms to the JSON file.
        """
        with open(self.filename, "w") as file:
            json.dump(
                [alarm.to_dict() for alarm in self.alarms],
                file,
                indent=4
            )

    def add_alarm(self, alarm: Alarm):
        """
        Add a new alarm and save immediately.
        """
        self.alarms.append(alarm)
        self.save()

    def remove_alarm(self, alarm_id: int):
        """
        Remove an alarm by its ID.
        Returns True if removed, False otherwise.
        """
        for alarm in self.alarms:
            if alarm.id == alarm_id:
                self.alarms.remove(alarm)
                self.save()
                return True

        return False

    def get_alarm(self, alarm_id: int):
        """
        Return an alarm with the given ID.
        """
        for alarm in self.alarms:
            if alarm.id == alarm_id:
                return alarm

        return None

    def get_all_alarms(self):
        """
        Return all alarms.
        """
        return list(self.alarms)

    def next_id(self):
        """
        Generate the next available alarm ID.
        """
        if not self.alarms:
            return 1

        return max(alarm.id for alarm in self.alarms) + 1