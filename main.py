import helpers as h
from timerange import TimeRange
from friend import Friend
from custom_list import CustomList


def main():
    available_minutes = CustomList(range(1440))
    # From here, add as much as friend objects you'd like.
    # Also, for each friend object, call the add_busy_range to add unavailable time range for each friend
    f1 = Friend("Dobby")
    f1.add_busy_range(TimeRange(start_time="04:00", end_time="06:00"))
    f1.add_busy_range(TimeRange(start_time="09:00", end_time="10:00"))
    f2 = Friend("Bobby")
    f2.add_busy_range(TimeRange(start_time="12:00", end_time="14:00"))
    f2.add_busy_range(TimeRange(start_time="18:00", end_time="21:30"))
    f3 = Friend("Robby")
    f3.add_busy_range(TimeRange(start_time="16:00", end_time="23:00"))

    for m in available_minutes[:]:
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)

    for tr in h.prettify_available_minutes(available_minutes):
        print(f"You can meet in {tr}")



if __name__ == "__main__":
    main()