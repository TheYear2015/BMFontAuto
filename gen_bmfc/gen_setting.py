# encoding:utf-8
# 生成 bmfc 文件的设置信息

class GenSetting(object):

    def __init__(self):
        # 图片资源的路径
        self.imgs_dir = "./"
        # 输出的色深
        self.out_bit_depth = "32"
        # 输出图片的最大尺寸
        self.max_width = 2048
        self.max_height = 2048
        # 输出文件的格式
        self.texture_format = "png"
        # 压缩等级
        self.texture_compression = 0
        # 使用 alpha 通道
        self.alpha_chnl = 1

    # 从配置文件中读取配置信息，json 格式
    def load_file(file_path):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
