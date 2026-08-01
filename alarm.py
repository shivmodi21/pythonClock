from dataclasses import dataclass
from datetime import datetime


@dataclass
class Alarm:
    id: int
    hour: int
    minute: int
    repeat: bool = False
    enabled: bool = True

    def __post_init__(self):
        """Validate alarm time after object creation."""
        if not (0 <= self.hour <= 23):
            raise ValueError("Hour must be between 0 and 23.")

        if not (0 <= self.minute <= 59):
            raise ValueError("Minute must be between 0 and 59.")

    @property
    def time_str(self) -> str:
        """Return time in HH:MM format."""
        return f"{self.hour:02d}:{self.minute:02d}"

    def to_dict(self) -> dict:
        """Convert Alarm to a JSON-serializable dictionary."""
        return {
            "id": self.id,
            "hour": self.hour,
            "minute": self.minute,
            "repeat": self.repeat,
            "enabled": self.enabled,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Create an Alarm object from a dictionary."""
        return cls(
            id=data["id"],
            hour=data["hour"],
            minute=data["minute"],
            repeat=data.get("repeat", False),
            enabled=data.get("enabled", True),
        )

    @classmethod
    def from_time_string(
        cls,
        id: int,
        time_str: str,
        repeat: bool = False,
        enabled: bool = True
    ):
        """
        Create an Alarm from a HH:MM time string.
        """
        try:
            hour_str, minute_str = time_str.split(":")
            hour = int(hour_str)
            minute = int(minute_str)
        except ValueError:
            raise ValueError("Time must be in HH:MM format.")

        return cls(
            id=id,
            hour=hour,
            minute=minute,
            repeat=repeat,
            enabled=enabled,
        )

    def should_ring(self, now: datetime) -> bool:

        if not self.enabled:
            return False

        if now.hour != self.hour or now.minute != self.minute:
            return False

        if (
            self.last_triggered
            and self.last_triggered.date() == now.date()
            and self.last_triggered.hour == now.hour
            and self.last_triggered.minute == now.minute
        ):
            return False

        self.last_triggered = now
        return True

    def __str__(self):
        repeat = "Daily" if self.repeat else "Once"
        status = "Enabled" if self.enabled else "Disabled"

        return (
            f"[{self.id}] "
            f"{self.time_str} | "
            f"{repeat} | "
            f"{status}"
        )