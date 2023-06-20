"""Call main.write_social_media_card() to create social media cards.

:author: Shay Hill
:created: 2022-11-16
"""
import sys

from social_media_card import write_social_media_card
from social_media_card.paths import PROJECT, FilePaths

_RESOURCES = PROJECT / "social_media_card" / "resources"


def _github_demo_card():
    local_image_path = _RESOURCES / "example_image.jpg"
    remote_image_dir = "https://somesite.com/images/"
    output_image_dir = PROJECT / "binaries" / "output_images"
    output_html_dir = PROJECT / "output_html"
    write_social_media_card(
        author="Your Name Here",
        title="Your Title Here",
        description="A description of your page.",
        url="https://duckduckgo.com",
        remote_image_dir=remote_image_dir,
        local_image_path=local_image_path,
        output_image_dir=output_image_dir,
        output_html_dir=output_html_dir,
        padding=3,
        banner_path=_RESOURCES / "example_banner.png",
        banner_padding=80,
    )
    paths = FilePaths(
        local_image_path.name, remote_image_dir, output_image_dir, output_html_dir
    )
    _ = sys.stdout.write(
        f"Created LinkedIn / Facebook image file at {paths.output_image_path}\n"
    )
    _ = sys.stdout.write(
        f"Created Twitter image file at {paths.output_image_path_twitter}\n"
    )
    _ = sys.stdout.write(f"Wrote output html at {paths.output_html_path}\n")


if __name__ == "__main__":
    _github_demo_card()

    # Created LinkedIn / Facebook image ... binaries\output_images\example_image.jpg
    # Created Twitter image file ... binaries\output_images\example_image_twitter.jpg
    # Wrote output html at ... \output_html\example_image.html
