"""
これは圧縮ファイルを一括で解凍したときに発生する、同じ名前のフォルダが入れ子になるのを訂正するプログラムです。
本プログラムによって生じた損害(特にフォルダの喪失など)に対して当方は一切の責任を持ちません。
MITライセンス。
作：NaokiSato102

※理論上mainを再帰的実行すればn重(n>=2)へ対応可能
"""

from typing import Union, Optional
import sys
import os
import pathlib
from random import uniform
import shutil

def show_dir(
			file_list:Union[pathlib.Path, str], 
			show_count:Optional[int]=10
		) -> None:
	
	"""ファイルパスのリストをshow_count以下の個数表示
	show_count以下の個数なら全部表示

	Parameters
	----------
	file_list : pathilib.Path | str
		ファイルパスのリスト
	show_count : int, optional
		この数値より多いと省略。デフォルトは10
	"""
	for index, i in enumerate(file_list):
		print(i)
		if show_count < index:
			print("etc....")
			break


def core(arg_path):

	print("走査開始点のフォルダ")
	print(arg_path,"\n")

	if arg_path.is_file():
		print("このパスはファイルにつき、これと同じ親ディレクトリのファイルを走査する")
		dirname = arg_path.parent

	else:
		print("このパスはフォルダにつき、このフォルダ内を走査する")
		dirname = arg_path

	while 1:
		
		print("---------------- 現在走査中フォルダ --------------------")
		print(dirname)
		print(f"親フォルダ = {dirname.parents[0].stem}")
		print(f"子フォルダ = {dirname.stem}")

		if dirname.stem == dirname.parents[0].stem:
			print("重複フォルダ")
			break
		
		if 1 < len((file_list := os.listdir(dirname))):
			print("[エラー] 重複フォルダ発見前に子フォルダに内容のあるフォルダに到着。")
			show_dir(file_list,5)
			input("エンターキー入力で終了/次に移る")
			return
		
		print("より深いパスの走査へ移行\n")
		dirname = dirname.joinpath("".join(file_list))

	new_dir = dirname.parents[1].joinpath(f'tmp{int(uniform(10000,0)):05}')
	old_dir = dirname
	dst_dir = dirname.parents[0]
	print(f"new_dir = {new_dir}")
	print(f"dst_dir = {dst_dir}")
	print(f"old_dir = {old_dir}")


	shutil.move(old_dir, new_dir)

	if os.listdir(dst_dir):
		input("フォルダの移転に失敗の恐れ")
		exit(1)

	print(dst_dir)

	try:
		os.rmdir(dst_dir)
	except OSError as e:
		input('元ファイル削除失敗のため、何か移転もれの恐れ', e)
		raise

	shutil.move(new_dir, dst_dir)


def main():
	"""メインです
	"""

	if len(sys.argv) < 2:
		input(
			"""これは圧縮ファイルを一括で解凍したときに発生する、
			同じ名前のフォルダが入れ子になるのを訂正するプログラムです。
			入れ子になっているフォルダを引数に与えてください。"""
		)
		exit(0)

	for n in sys.argv[1:]:
		arg_path = pathlib.Path(n).resolve()
		core(arg_path)


main()