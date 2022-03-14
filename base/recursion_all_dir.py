import os


def cat_all_file(dir_path, n):
    """
    :param dir_path: 目录路径
    :param n: 1=dir / else=file
    :return: 该路径下所有目录
    """
    # 判断 文件/目录
    _all = [{"name": file, "res": os.path.isdir(f"{dir_path}/{file}")} for file in os.listdir(dir_path)]
    # all_dir=目录集   all_file=文件集
    all_dir = [_dir['name'] for _dir in _all if _dir['res']]
    all_file = [_file['name'] for _file in _all if _file['res'] is False]
    # 1=dir / else=file
    return all_dir if (n == 1) else all_file


print(cat_all_file("/Users/jg-test/Downloads/", 1))


def cat_all_recursion(dir_path="/"):
    """
    :param dir_path:
    :return:
    """
    all_file = os.listdir(dir_path)
    # 如果路径下没有目录了is_none=0
    is_none = 0 if (len([_dir for _dir in all_file if "." not in str(_dir)]) == 0) else [_dir for _dir in all_file if "." not in str(_dir)]
    # print(is_none)


# print(cat_all_recursion("/Users/jg-test/Downloads/"))
