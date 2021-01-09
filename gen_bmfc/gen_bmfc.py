# encoding:utf-8
# 生成 bmfc 文件

import os
import gen_setting
import bmfc_file

class GenBMFC(object):
    def __init__(self, setting):
        self.setting = setting
        # 需要填充的 unicode 字符列表，包含对应的图片信息。
        self.chars = []

    def gen(self, out_file_path):
        # 遍历图片目录下的图片，获得图片信息
        self.__get_imgs_info_in_dir(self.setting.imgs_dir)
        # 输出到 bmfc 文件
        self.__gen_bmfc(out_file_path)

    # 获得指定目录下的图片文件的图片信息。
    def __get_imgs_info_in_dir(self, imgs_dir):
        for root, dirs, files in os.walk(imgs_dir):
            for f in files:
                code = self.__get_img_info(f)
                self.chars.append((os.path.join(root, f), code))

    # 获得指定图片的图片信息，图片的大小，图片对应的 unicode。
    def __get_img_info(self, img_path):
        code = self.__convert_file_name_to_unicode(img_path)
        return code

    # 输出到 bmfc 文件
    def __gen_bmfc(self, out_file_path):
        print(self.chars)
        file = bmfc_file.BMFCFile(self.setting)
        file.set_chars(self.chars)
        file.write(out_file_path)

    # 转换文件名对应的 unicode
    def __convert_file_name_to_unicode(self, file_path):
        name = os.path.splitext(os.path.basename(file_path))[0]
        if len(name) > 1:
            if name[0] == 'U' or name[0] == 'u':
                return int(name[1:])
        else:
            return ord(name[0])


def test():
    setting = gen_setting.GenSetting()
    setting.imgs_dir = "K:/GitHub/BMFontAuto/imags"
    c = GenBMFC(setting)
    c.gen("./out.bmfc")


def main():
    test()


if __name__ == "__main__":
    main()
