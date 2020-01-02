# Same_name_nest_simplizer
This is a program that corrects the nesting of folders with the same name, which occurs when uncompressing compressed files at once.  

これは圧縮ファイルを一括で解凍したときに発生する、同じ名前のフォルダが入れ子になるのを訂正するプログラムです。  

※  
Nothing has been done yet.  
まだ何もできてません。


## example  
Eliminate the nest of the same name of the folder decompressed under the foo folder.  
fooフォルダ配下で解凍したフォルダの同名入れ子を解消します。
>	/foo/bar/bar/foobar.py  
>	/foo/foofoo/foofoo/bar.py  
>
>	↓
>
>	/foo/bar/foobar.py  
>	/foo/foofoo/bar.py  

## Disclaimer
We are not responsible for any damage caused by this program (especially loss of folders).  
本プログラムによって生じた損害(特にフォルダの喪失など)に対して当方は一切の責任を持ちません。