def ft_count_harvest_recursive():
    days_until_harvest = int(input("Days until harvest: "))
    count_harvest(days_until_harvest, 1)
    print("Harvest time!")


def count_harvest(harvest_day, current_day):
    if (current_day < harvest_day + 1):
        print(f"Day {current_day}")
        count_harvest(harvest_day, current_day + 1)
