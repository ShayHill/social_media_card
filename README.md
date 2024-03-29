# create social media cards for LinkedIn, Facebook, and (untested) Twitter

This will create cards (images as clickable links) for social media sites. See [this article](https://www.foundationsafety.com/social-cards) for a full explanation.

Host the output of `write_social_media_card` somewhere, link to it on a social-media site, and that site will build a card (or preview) with the (altered) image at `local_image_path`. Clicking that preview will forward visitors to the provided `url`.

    :param author: The author of the page.
    :param title: The title of the page.
    :param description: The description of the page. Try to make this around 200
        characters to avoid warnings.
    :param url: The url to which the card will link.
    :param remote_image_dir: The directory on the remote server where the images will
        be hosted online. E.g., https://example.com/images/
    :param local_image_path: The path to the image on the local machine.
    :param output_image_dir: output images will be written here
    :param output_html_dir: (optional) output html will be written here. If not
        given, output_image_dir will be used. The flexibility is here for those who
        like to keep binaries (output images) and text files (output html) separate.

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

A lot of what this does is prepare your images.

1. If you provide a banner image, that banner will be laid over the input image to brand your card.
2. Pads LinkedIn and Facebook images to avoid cropping. LinkedIn will crop any images with an aspect ratio < 1:1.
3. Pads Twitter images to 2:1. I don't have a Twitter account to check that this is necessary, but other card generators I've found pad Twitter images to 2:1, so I assume there is a reason.

See an example call in `example_create_card.py`.

![GitHub Logo](/binaries/output_images/example_image.jpg)

The LinkedIn and Twitter appropriate aspect ranges are so different that you probably want to run this script twice with different images and banners. Maybe a third time to tune for Facebook. That would be the best way to tune, because I haven't heavily parameterized or made provisions for site-specific images.

To see exactly how this works, run `python -m social_media_cards.create_card` then examine the output in `binaries/output_images` and `output_html/`.

Test image by <a href="https://pixabay.com/users/frankwinkler-64960/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=540812">Frank Winkler</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=540812">Pixabay</a>
