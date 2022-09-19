from PIL import Image, ImageDraw, ImageFont

def generate_postcard(in_path, out_path, message=None, crop=None, width=None):
    """Create a Postcard With a Text Greeting

   Arguments:
        in_path {str} - - the file location for the input image.
        out_path {str} - - the desired location for the output image.
        crop {tuple} - - The crop rectangle, as a(left, upper, right, lower)-tuple. Default = None.
        width {int} - - The pixel width value. Default = None.
    Returns:
        str - - the file path to the output image.
    """
    
    with Image.open(in_path) as im:
        print(im.size)  # => (1331, 2567)
        im_crop = im.crop(crop)
        print(im_crop.size)  # => (450, 450)
        #im_crop.save(out_path)
        im_resized = im_crop.resize((im_crop.width *2, im_crop.height*2))
        print(im_resized.size)  # => (900, 900)
        

        if message is not None:
            draw = ImageDraw.Draw(im_resized)
            #font = ImageFont.load_default()
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=40)
            draw.text((30, 30), message, font=font, fill='white')

    im_resized.save(out_path)
    return out_path    
    
    # raise Exception('generate_postcard not implemented')

if __name__=='__main__':
    print(generate_postcard('./imgs/img.jpg',
                            './imgs/new_img.jpg',
                            "Woof, woof!",
                            (425,875,875,1325)))




'''
# Udacity Solution
from PIL import Image, ImageDraw, ImageFont

def generate_postcard(in_path, out_path, message=None, crop=None, width=None):
    img = Image.open(in_path)
    print(img.size, '<= original size')  # debug line

    if crop is not None:
        img = img.crop(crop)

    if width is not None:
        ratio = width/float(img.size[0])
        print(img.size, '<=  crop size')  # debug line
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        print(img.size, '< =  final size')  # debug line

    if message is not None:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        draw.text((10, 30), message, font=font, fill='white')
        
    img.save(out_path)
    return out_path

if __name__=='__main__':
    print(generate_postcard('./imgs/img.jpg', 
                            './imgs/out.jpg',
                            'woof!',
                            (450, 900, 900, 1300),
                            200))

'''

