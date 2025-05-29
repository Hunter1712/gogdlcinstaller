# GOG DLC Installer Runner Script

This Python script automates the execution of multiple `.sh` installer scripts located in a specified directory. It makes each installer executable and then runs it, automatically responding to common prompts during the installation process.

## Features

- Automatically finds all `.sh` installer scripts in a given directory.
- Makes each script executable (`chmod +x`).
- Runs each installer using `pexpect`, handling common interactive prompts:
  - Disables pager prompts by sending `n`.
  - Presses Enter to continue when prompted.
  - Accepts licenses automatically by sending `y`.
  - Selects the default installation destination.
- Prints progress and completion messages.

## Requirements

- Python 3
- `pexpect` module (`pip install pexpect`)

---

## Usage

1. **Set the installer directory:**

   Edit the `DLC_PATH` variable in the script to point to the folder containing your `.sh` installers. For example:

        DLC_PATH = "/path/to/your/installers"

2. **Run the script:**

        python3 main.py

    Example

        Running /path/to/your/installers/setup1.sh ...
        Finished /path/to/your/installers/setup1.sh
        ----------------------------------------
        Running /path/to/your/installers/setup2.sh ...
        Finished /path/to/your/installers/setup2.sh
        ----------------------------------------
        All installers processed.

## Notes
This script is designed specifically for Linux systems.

The script assumes typical prompts from the installers. If your installers use different prompts, you may need to update the `run_installer` function's expect patterns.

The script runs installers sequentially and waits for each to finish before starting the next.

Ensure the installers do not require manual intervention beyond the handled prompts.

## License

This script is provided as-is under the MIT License.

Feel free to contribute.