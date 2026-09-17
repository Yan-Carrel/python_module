import sys

if __name__ == "__main__":
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}
    i: int = 0

    if len(args) <= 1:
        print(
            "Usage python3 ft_inventory_system.py "
            "<item1>:<value> <item2>:<value> ...")
    else:
        print("=== Inventory System Analysis ===")
        for arg in args:
            try:
                if ((arg[0] == ':')
                        or (':' not in arg)
                        or (arg[-1] == ':')):
                    raise Exception(f"Error - invalid parameter '{arg}'")

                item_name, quantity = arg.split(':')

                if item_name in inventory:
                    raise Exception(
                        f"Redundant item '{item_name}' - discarding"
                        )

                inventory[item_name] = int(quantity)

            except ValueError as e:
                print(f"Quantity error for '{item_name}': {e}")
                continue
            except Exception as e:
                print(e)
                continue

        if inventory:
            print(f"Got inventory: {inventory}")
            print(f"Item list: {list(inventory.keys())}")

            values = inventory.values()
            sum_values = sum(values)
            inventory_len = len(inventory)
            print(
                f"Total quantity of the {inventory_len} items: {sum_values}"
                )

            _min = list(inventory)[0]
            _max = list(inventory)[0]
            for key in inventory.keys():
                if inventory[key] < inventory[_min]:
                    _min = key
                if inventory[key] > inventory[_max]:
                    _max = key
                print(
                    f"Item {key} represents "
                    f"{(inventory[key] / sum_values * 100):.1f}%"
                    )

            print(
                f"Item most abundant: {_max} with quantity {inventory[_max]}"
                )
            print(
                f"Item least abundant: {_min} with quantity {inventory[_min]}"
                )

            inventory.update({"magic_item": 1})
            print(f"Updated inventory: {inventory}")
        else:
            print(
                "Usage python3 ft_inventory_system.py "
                "<item1>:<value> <item2>:<value> ...")
