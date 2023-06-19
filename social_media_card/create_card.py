"""Call main.write_social_media_card() to create social media cards.

:author: Shay Hill
:created: 2022-11-16
"""
from social_media_card.main import write_social_media_card
from social_media_card.paths import RESOURCES


def _github_demo_card():
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


if __name__ == "__main__":
    _github_demo_card()
