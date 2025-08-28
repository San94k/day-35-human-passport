
### streak.py
```python
from __future__ import annotations
import argparse
from datetime import date, datetime

def parse_date(s: str) -> date:
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError("Use format YYYY-MM-DD, e.g. 2025-07-25")

def calc_day(start: date, today: date) -> int:
    # День старту = 1
    return (today - start).days + 1

def main():
    parser = argparse.ArgumentParser(description="GitHub streak day counter")
    parser.add_argument("--start", type=parse_date, default=parse_date("2025-07-25"),
                        help="Start date (YYYY-MM-DD). Default: 2025-07-25")
    parser.add_argument("--today", type=parse_date, default=date.today(),
                        help="Override today's date (YYYY-MM-DD). Default: system date")
    args = parser.parse_args()

    if args.today < args.start:
        raise SystemExit("Error: --today can't be earlier than --start")

    day = calc_day(args.start, args.today)

    print(f"Day: {day}")
    print(f"Range: {args.start.isoformat()} → {args.today.isoformat()} (Europe/Warsaw)")
    if day % 5 == 0:
        print("Milestone hit! 🔥")
    print("Keep going! 🚀")

if __name__ == "__main__":
    main()
