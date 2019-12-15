from shutil import register_unpack_format,unpack_archive
from py7zr import unpack_7zarchive
from zipfile import ZipFile
from rarfile import RarFile
from tqdm import tqdm
import tarfile


def z7():
    register_unpack_format('7zip', ['.7z'], unpack_7zarchive)
    unpack_archive('dist.7z', '/Users/developer/PycharmProjects/macex')


def rar():
    with RarFile("FileZilla_3.46.0_macosx-x86.app.tar.bz2") as rf:
        rf.extractall()


def tar():
    with tarfile.open("FileZilla_3.46.0_macosx-x86.app.tar.bz2") as tf:
        tf.extractall()

def zip():
    with ZipFile('yb.zip', 'r') as zipObj:
        for file in tqdm(iterable=zipObj.namelist(), total=len(zipObj.namelist())):
            zipObj.extract(member=file, path="/Users/developer/PycharmProjects/macex")
