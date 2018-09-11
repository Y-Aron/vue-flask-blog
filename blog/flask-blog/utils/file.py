
from utils import calc_sha1
from config import BASE_DIR
import os

class UploadFile(object):
    UPLOAD_FOLDER = os.path.join(BASE_DIR,'uploads')

    ALLOWED_EXTENSIONS = dict(
        images = ['png','jpg','jpeg','bmp','gif','tiff','psd','swf','svg'],
        files = ['txt']
    )

    def __init__(self, file = None):
        self.file = file
        self.file_name = None
        self.file_path = None
        self.file_body = None
        self.file_exists = False

    def make_file(self, file=None):
        if not self.file: self.file = file
        filename = self.file.filename
        body = self.file.read()
        ret = self.get_file_path(filename, body)

        self.file_name = ret['filename']
        self.file_path = ret['file_path']
        self.file_body = body
        self.file_exists = ret['exists']


    def save(self):
        if self.file_path and self.file_body:

            if self.file_exists:
                return

            with open(self.file_path, 'wb') as f:
                f.write(self.file_body)

    def get_file_path(self, filename, body=None):
        dir_name = 'unknown'

        file_ext = '.' in filename and filename.rsplit('.', 1)[1]

        # body 存在表示文件是上传 需要重命名
        if body:
            filename = calc_sha1(body)
            # 初始化文件名
            if file_ext :
                filename += '.{ext}'.format(ext=file_ext)

        # 定位文件所在文件夹名
        for key, val in self.ALLOWED_EXTENSIONS.items():
            if file_ext and file_ext.lower() in val:
                dir_name = key

        # 组合文件的绝对路径 如果文件不存在则创建
        file_dir = os.path.join(self.UPLOAD_FOLDER, dir_name)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        file_path = os.path.join(file_dir, filename)

        exists = os.path.exists(file_path)

        return dict(file_path = file_path, filename = filename, exists=exists)

    # # 判断文件是否存在 存在返回文件对象
    # def __file_exists(self, file_path):
    #     if not os.path.exists(self.UPLOAD_FOLDER):
    #         return False
    #
    #     # 获取 UPLOAD_FOLDER 路径下的文件名列表
    #     file_list = get_file_list(self.UPLOAD_FOLDER)
    #
    #     # 判断路径是否一致  一致返回true
    #     for fp in file_list:
    #         if fp == file_path:
    #             return True