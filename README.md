# ⏰ Python CLI Alarm Clock

A simple command-line alarm clock built with Python. This project demonstrates object-oriented design, file persistence using JSON, command-line argument parsing with `argparse`, and a continuously running scheduler to trigger alarms.

## Features

* Add one-time alarms
* Add repeating (daily) alarms
* List all saved alarms
* Remove alarms by ID
* Persistent storage using a local JSON file
* Continuous scheduler that monitors alarms
* Terminal bell notification (`\a`) when an alarm triggers
* Clean shutdown using `Ctrl + C`

## Project Structure

```text
alarm_clock/
│
├── main.py          # Entry point
├── cli.py           # Command-line argument parser
├── alarm.py         # Alarm model
├── storage.py       # JSON storage handler
├── scheduler.py     # Alarm scheduler
├── alarms.json      # Alarm data
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

* Python 3.10 or newer

This project uses only Python's standard library and does not require any third-party packages.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd alarm_clock
```

Create a virtual environment:

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Usage

### Add a one-time alarm

```bash
python main.py add 07:30
```

### Add a repeating alarm

```bash
python main.py add 18:00 --repeat
```

### List alarms

```bash
python main.py list
```

Example output:

```text
Current Alarms:
[1] 07:30 | Once | Enabled
[2] 18:00 | Daily | Enabled
```

### Remove an alarm

```bash
python main.py remove 1
```

### Start the alarm scheduler

```bash
python main.py run
```

The scheduler continuously checks the current time and triggers alarms when they match.

Stop the scheduler at any time with:

```text
Ctrl + C
```

## Alarm Storage

Alarms are stored locally in `alarms.json`.

Example:

```json
[
    {
        "id": 1,
        "hour": 7,
        "minute": 30,
        "repeat": false,
        "enabled": true
    }
]
```

## Design Overview

The application is divided into small, focused modules:

* **main.py** – Coordinates the application flow.
* **cli.py** – Defines and parses command-line commands.
* **alarm.py** – Represents an alarm and handles validation and serialization.
* **storage.py** – Loads and saves alarms to a JSON file.
* **scheduler.py** – Continuously checks the current time and triggers alarms.
