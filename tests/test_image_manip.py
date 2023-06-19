
from PIL import Image
from social_media_card import pad_image

class TestPadImage:
        
    def test_padding_with_transparency(self):
        test_image = Image.new('RGBA', (100, 100), color=(0, 0, 0, 255))
        padded_image = pad_image(test_image, 10, 10, 20, 20)
        assert padded_image.size == (130, 130)
        assert padded_image.mode == 'RGBA'
        assert padded_image.getpixel((0, 0)) == (255, 255, 255, 0)  # type: ignore
        assert padded_image.getpixel((9, 9)) == (255, 255, 255, 0)  # type: ignore
    
    def test_padding_without_transparency(self):
        test_image = Image.new('RGBA', (100, 100), color=(0, 0, 0, 255))
        test_image = test_image.convert('RGB')
        padded_image = pad_image(test_image, 10, 10, 20, 20)
        assert padded_image.size == (130, 130)
        assert padded_image.mode == 'RGB'
        assert padded_image.getpixel((0, 0)) == (255, 255, 255)  # type: ignore
        assert padded_image.getpixel((9, 9)) == (255, 255, 255)  # type: ignore
