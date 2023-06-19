"""Paths to local files and directories and remote file urls.

:author: Shay Hill
:created: 2022-11-10
"""

from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin

_PROJECT = Path(__file__, "..", "..").resolve()
_BINARIES = _PROJECT / "binaries"
_OUTPUT_IMAGES = _BINARIES / "output_images"
_OUTPUT_HTML = _PROJECT / "output_html"

_OUTPUT_IMAGES.mkdir(parents=True, exist_ok=True)
_OUTPUT_HTML.mkdir(parents=True, exist_ok=True)

RESOURCES = _PROJECT / "resources"
HTML_TEMPLATE = RESOURCES / "template.html"

# INPUT_IMAGES is a convenience for me. This variable is only used to create an input
# image path when calling `write_social_media_card`. It's not used in the code.
INPUT_IMAGES = _BINARIES / "input_images"
INPUT_IMAGES.mkdir(parents=True, exist_ok=True)


def _twitterize_filename(filename: str | Path) -> str:
    """Return an image filename for Twitter."""
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    return f"{stem}_twitter{suffix}"


@dataclass(frozen=True)
class FilePaths:
    """Paths to output files and image host urls.

    :param filename: The name of the input image file. The card itself and all images
        will be variations of this name.
    :param remote_image_url: The directory where the output images will be hosted.
    """

    image_filename: str
    remote_image_url: str

    @property
    def _stem(self) -> str:
        """Return the stem of the image filename."""
        return Path(self.image_filename).stem

    @property
    def _twitter_image_filename(self) -> str:
        """Return the filename for Twitter images."""
        return _twitterize_filename(self.image_filename)

    @property
    def output_image_path(self) -> Path:
        """Return the path to the output image for LinkedIn / Facebook cards."""
        return _OUTPUT_IMAGES / self.image_filename

    @property
    def output_image_path_twitter(self) -> Path:
        """Return the path to the output image for Twitter cards."""
        return _OUTPUT_IMAGES / self._twitter_image_filename

    @property
    def output_html_path(self) -> Path:
        """Return the path to the output HTML file."""
        return _OUTPUT_HTML / f"{self._stem}.html"

    @property
    def image_url(self) -> str:
        """Return the image url for LinkedIn / Facebook cards."""
        return urljoin(self.remote_image_url, self.image_filename)

    @property
    def image_url_twitter(self) -> str:
        """Return the image url for Twitter cards."""
        return urljoin(self.remote_image_url, self._twitter_image_filename)
