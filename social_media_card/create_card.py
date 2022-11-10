#!/usr/bin/env python3
# last modified: 221110 14:12:13
"""HTML template for social media card.

:author: Shay Hill
:created: 2022-11-09
"""

from pathlib import Path
from typing import Optional

from social_media_card.html_template import write_social_media_card_html
from social_media_card.image_manip import (
    get_image_with_banner,
    pad_image,
    write_image_variants,
)
from social_media_card.paths import FilePaths, INPUT_IMAGES


def write_social_media_card(
    author: str,
    title: str,
    description: str,
    url: str,
    remote_image_dir: str,
    local_image_path: str | Path,
    banner_path: Optional[str | Path] = None,
    banner_padding: Optional[int] = None,
    padding: int = 0,
) -> None:
    """Write the social media card to the output directories.

    :param author: The author of the page.
    :param title: The title of the page.
    :param description: The description of the page. Try to make this around 200
        characters to avoid warnings.
    :param url: The url to which the card will link.
    :param remote_image_dir: The directory on the remote server where the images will
        be hosted online. E.g. `https://example.com/images/`.
    :param local_image_path: The path to the image on the local machine.

    :param banner_path: The path to an optional banner image. This will be added on
        top of the input image.
    :param banner_padding: The padding to apply to the banner image. This is the
        number of pixels to add to the top of the image before pasting the banner. If
        not provided, the banner height will be used. Use something other that the
        banner height if you have transparency in your banner and would like to see
        some of the image through it.
    :param padding: Optional minimum padding around the image. This padding is added
        *after* any banner is applied. I often use screenshots of my website. In
        order to crop exactly around the images (this looks best with the banner), I
        have to crop exactly at the text margin, which can look a bit crowded.

    :effects:
        - writes two images to OUTPUT_IMAGES: one for LinkedIn and one for Twitter
        - writes a file to OUTPUT_HTML: the HTML file for the card
    """
    paths = FilePaths(Path(local_image_path).name, remote_image_dir)
    image = get_image_with_banner(local_image_path, banner_path, banner_padding)
    if padding:
        image = pad_image(image, padding, padding, padding, padding)
    write_image_variants(image, paths)
    write_social_media_card_html(author, title, description, url, paths)


if __name__ == "__main__":
    from pathlib import Path
    from social_media_card.paths import RESOURCES

    write_social_media_card(
        author="Your Name Here",
        title="Your Title Here",
        description="A description of your page.",
        url="https://duckduckgo.com",
        remote_image_dir="https://somesite.com/images/",
        local_image_path=RESOURCES / "example_image.jpg",
        padding=3,
        banner_path=RESOURCES / "example_banner.png",
        banner_padding=80,
    )

