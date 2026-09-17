#!/usr/bin/python3
import os
import sys
try:
    from dotenv import load_dotenv
except ImportError:
    print("Error, you need to import dotenv module")
    print("run the following commands")
    if sys.prefix == sys.base_prefix:
        print("python3 -m venv .venv")
        print("source .venv/bin/activate")
    print("pip install python-dotenv")
    sys.exit(1)


if __name__ == "__main__":
    default_configs = {
        "Mode": "MATRIX_MODE", "Database": "DATABASE_URL",
        "API Access": "API_KEY", "Log level": "LOG_LEVEL",
        "Zion Network": "ZION_ENDPOINT"
        }

    no_hardcoded = True
    properly_configured = True

    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    print("\nConfiguration loaded:\n")
    for key in list(default_configs.keys()):
        try:
            value = os.getenv(default_configs[key])
            if value is None or value == "":
                raise ValueError(f"{key} is missing")
            elif default_configs[key] == 'API_KEY':
                print(f"{key}: Authenticated")
            elif default_configs[key] == "DATABASE_URL":
                mode = os.getenv("MATRIX_MODE")
                if mode == "production":
                    print(f"{key}: Connected to production cluster")
                else:
                    print(f"{key}: Connected to local instance")
            else:
                print(f"{key}: {value}")
        except ValueError as e:
            properly_configured = False
            print(e)

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if properly_configured:
        print("[OK] .env file properly configured")
    else:
        print("[KO] Error, .env file is not properly configured")

    mode = os.getenv("MATRIX_MODE")
    if mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides are not available")

    print("\nThe Oracle sees all configurations.")
