import os
import random
import io

from PIL import Image, ImageDraw, ImageFont, ImageFilter

class ImageCode(object):
    # 字体的位置，不同版本的系统会有不同
    font_path = os.path.join(os.path.dirname(__file__),'fonts/monaco.ttf')
    # 生成几位数的验证码
    number = 4
    # 生成验证码图片的高度和宽度
    size = (100, 30)
    # 背景颜色，默认为白色
    bgcolor = (255, 255, 255)
    # 字体颜色，默认为蓝色
    fontcolor = (0, 0, 255)
    # 干扰线颜色。默认为红色
    linecolor = (255, 0, 0)
    # 是否要加入干扰线
    draw_line = True
    # 加入干扰线条数的上下限
    line_number = (1, 5)
    # 用来随机生成一个字符串
    source = list('2345678abcdefhijkmnpqrstuvwxyzABCDEFGHJKLMNPQRTUVWXY')

    # 实现单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    # 生成验证码文本
    def __gene_text(self):
        return ''.join(random.sample(self.source, self.number))  # number是生成验证码的位数

    # 用来绘制干扰线
    def __gene_line(self,draw, width, height):
        begin = (random.randint(0, width), random.randint(0, height))
        end = (random.randint(0, width), random.randint(0, height))
        draw.line([begin, end], fill=self.linecolor)

    # 生成验证码图片二进制
    def __gene_code(self):
        width, height = self.size  # 宽和高
        image = Image.new('RGBA', (width, height), self.bgcolor)  # 创建图片
        font = ImageFont.truetype(self.font_path, 25)  # 验证码的字体
        draw = ImageDraw.Draw(image)  # 创建画笔
        text = self.__gene_text()  # 生成字符串
        font_width, font_height = font.getsize(text)
        draw.text(((width - font_width) / self.number, (height - font_height) / self.number), text,
                  font=font, fill=self.fontcolor)  # 填充字符串

        if self.draw_line:
            self.__gene_line(draw, width, height)
        image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0),
                                Image.BILINEAR)  # 创建扭曲
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强

        # generate image binary streams
        buf = io.BytesIO()
        image.save(buf, 'png')
        image_buf = buf.getvalue()
        return image_buf, text

    def gene_code(self):
        return self.__gene_code()

if __name__ == '__main__':

    image = ImageCode()

    image,text = image.gene_code()
    print(image,text)
