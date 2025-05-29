#!/usr/bin/env python3
import pexpect
import sys
import glob
import os

DLC_PATH = ""

def run_installer(installer_path):
    # Run installer with pager disabled
    child = pexpect.spawn(f'env PAGER=cat bash "{installer_path}"', encoding='utf-8', timeout=None)

    while True:
        try:
            index = child.expect([
                r"\(1-21 of \d+ lines, see more\?\) \[Y/n\]:",
                r"Type 'back' to go back\.\s*Press enter to continue\.\s*>",
                r"Accept this license\? \[y/N\]:",
                r"Choose install destination by number.*\nType 'back' to go back\.\s*>",
                pexpect.EOF,
                pexpect.TIMEOUT,
            ])

            if index == 0:
                # see more prompt
                child.sendline("n")
            elif index == 1:
                # press enter to continue
                child.sendline("")
            elif index == 2:
                # accept license
                child.sendline("y")
            elif index == 3:
                # accept default destination
                child.sendline("")
            elif index == 4:
                # EOF, finished
                print(f"Finished {installer_path}")
                break
            elif index == 5:
                # timeout: no prompt, just continue waiting
                continue

        except pexpect.exceptions.EOF:
            print(f"EOF reached for {installer_path}")
            break
        except Exception as e:
            print(f"Error with {installer_path}: {e}")
            break

def main():
    installers = glob.glob(os.path.join(DLC_PATH, "*.sh"))
    if not installers:
        print(f"No installers found in {DLC_PATH}")
        sys.exit(1)

    for installer in installers:
        print(f"Running {installer} ...")
        run_installer(installer)
        print("-" * 40)

    print("All installers processed.")

if __name__ == "__main__":
    main()
