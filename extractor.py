from shutil import register_unpack_format,unpack_archive
from py7zr import unpack_7zarchive
from zipfile import ZipFile
from rarfile import RarFile
from tqdm import tqdm
import tarfile
import os
import sys

class Zipper:
    def __init__(self):
        self.output_path = os.getcwd()
        self.zipper_file = sys.argv[1]
        filename, ext = os.path.splitext(self.zipper_file)


        if ext == "7z":
            self.z7()
        elif ext == "rar":
            self.rar()
        elif ext == "tar" or "gz":
            self.tar()

        elif ext == "zip":
            self.zip()

    def z7(self):
        register_unpack_format('7zip', ['.7z'], unpack_7zarchive)
        unpack_archive(self.zipper_file, self.output_path)


    def rar(self):
        with RarFile(self.zipper_file) as rf:
            rf.extractall()


    def tar(self):
        with tarfile.open(self.zipper_file) as tf:
            tf.extractall()

    def zip(self):
        with ZipFile(self.zipper_file, 'r') as zipObj:
            for file in tqdm(iterable=zipObj.namelist(), total=len(zipObj.namelist())):
                zipObj.extract(member=file, path=self.output_path)


if __name__ == '__main__':
    Zipper()