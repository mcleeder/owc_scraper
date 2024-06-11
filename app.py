from urllib.parse import urlparse
import importlib


def main():
    # url = input("Enter URL: ")
    url = "https://www.stereogum.com/2266436/the-number-ones-taylor-swifts-shake-it-off/columns/the-number-ones/"  # noqa: E501

    site_name = _get_site_name(url)

    try:
        module = importlib.import_module(
            f"sites.{site_name.title()}.{site_name.title()}"
        )
        site = getattr(module, site_name.title())()

    except ImportError:
        print(f"Failed to find site {site_name}")
        return

    raw_data = site.get_data(url=url)

    comments = site.parse_data(raw_data)

    # TODO: Send data somewhere
    print(f"Found {len(comments)} comments")


def _get_site_name(url: str):
    parsed_url = urlparse(url)

    # TODO: This'll break on urls like .co.uk
    split_url = parsed_url.netloc.split(".")
    return split_url[-2].lower()


if __name__ == "__main__":
    main()
