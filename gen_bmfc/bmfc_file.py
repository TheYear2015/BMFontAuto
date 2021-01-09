# encoding:utf-8
# bmfc 文件操作

import os
import gen_setting


class BMFCFile:
    def __init__(self, setting):
        self.setting = setting
        # 需要填充的 unicode 字符列表，包含对应的图片信息。
        self.chars = []

    # 设置需要填充的 unicode 字符列表，包含对应的图片信息。
    def set_chars(self, chars):
        self.chars = chars

    # 读取
    def read(self, file_path):
        pass

    # 保存
    def write(self, file_path):
        # 文件头
        lines = ["# AngelCode Bitmap Font Generator configuration file",
                 "fileVersion=1", "", "# font settings"]

        lines.append("")

        lines.append("# character alignment")
        lines.append("")

        lines.append("# output file")
        lines.append("outWidth={}".format(self.setting.max_width))
        lines.append("outHeight={}".format(self.setting.max_height))
        lines.append("outBitDepth={}".format(self.setting.out_bit_depth))
        lines.append("textureFormat={}".format(self.setting.texture_format))
        lines.append("textureCompression={}".format(
            self.setting.texture_compression))
        lines.append("alphaChnl={}".format(self.setting.alpha_chnl))
        lines.append("")

        lines.append("# outline")
        lines.append("")

        lines.append("# selected chars")
        chars = []
        for c in self.chars:
            chars.append(str(c[1]))
        lines.append("chars=" + ','.join(chars))
        lines.append("")

        lines.append("# imported icon images")

        out_dir = os.path.dirname(os.path.abspath(
            file_path)).replace('\\', '/') + '/'
        for c in self.chars:
            # 转换为相对路径
            icon = c[0].replace('\\', '/').replace(out_dir, "")
            lines.append('icon="{}",{},0,0,0'.format(icon, c[1]))

        # 写入文件
        file = open(file_path, "w", encoding="utf-8")
        file.writelines([line+'\n' for line in lines])
        file.close()


def test():
    setting = gen_setting.GenSetting()
    c = BMFCFile(setting)
    c.write("./out.bmfc")


def main():
    test()


if __name__ == "__main__":
    main()
