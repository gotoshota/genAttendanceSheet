# genAttendanceSheet
研究室のドアとかに貼る出席シートを生成するためのプログラム。

## 使い方
### 1.事前準備
reportlab が必要。
```bash
pip install reportlab
```
などでインストールする。

### 2.名前リストの作成
`names.txt`に以下の様な内容を記述する。
```txt
# position, name
PD, 田中太郎
M1, 山田花子
...
```

### 3.実行
pythonで実行する。
```bash
python genAttendanceSheet.py --input names.txt
```
出力する pdf のファイル名を指定する場合は、`--output` オプションを使用する。
```bash
python genAttendanceSheet.py --input names.txt --output attendance_sheet.pdf
```
