from urllib.parse import urlparse
import importlib


def main():
    url = input("Enter URL: ")

    site_name = _get_site_name(url)

    try:
        module = importlib.import_module(
            f"sites.{site_name.title()}.{site_name.title()}"
        )
        site = getattr(module, site_name.title())

    except (ImportError, ArithmeticError):
        print(f"Failed to find site {site_name}")
        return

    raw_data = site.get_data(url)

    comments = site.parse_date(raw_data)

    print(comments)


def _get_site_name(url: str):
    parsed_url = urlparse(url)

    split_url = parsed_url.netloc.split(".")
    return split_url[-2].lower()


if __name__ == "__main__":
    main()
