import os


def create_boilerplate(site_name):
    boilerplate_content = f"""
from typing import Any
from base.scraper import Scraper
from base.comment import Comment

class {site_name}(Scraper):

    SITE_NAME = "{site_name}"
    BASE_URL : str

    def get_data(self, url: str) -> Any:
        ...

    def parse_data(self) -> list[Comment]:
        ...
"""

    directory = os.path.join("sites", site_name)
    file_path = os.path.join(directory, f"{site_name}.py")

    os.makedirs(directory, exist_ok=False)

    with open(file_path, "w") as file:
        file.write(boilerplate_content)

    print(f"Boilerplate for site '{site_name}' created at {file_path}")


def main():
    while True:
        site_name = input("Enter the site name: ").strip()

        print(f"\nYou entered:\nSite Name: {site_name}")
        confirmation = input("Correct? ([y]/n): ").strip().lower()

        if confirmation in ["", "y"]:
            break

    create_boilerplate(site_name)


if __name__ == "__main__":
    main()
