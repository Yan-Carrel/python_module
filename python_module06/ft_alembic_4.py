#!/usr/bin/python3
import alchemy


if __name__ == "__main__":
    print("=== Alembic_4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    print("Testing the hidden create_earth: ", end=alchemy.create_earth())
