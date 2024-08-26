from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate attendance sheet PDF from a list of names.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Input file containing the list of names.")
    parser.add_argument("-o", "--output", type=str, default="attendance_sheet.pdf", help="Output PDF file name.")
    return parser.parse_args()



# PARAMETERS
fontsize = 16
header_height = 40
row_height = 80

def create_pdf(data, output_file):
    # ファイル拡張子が ".pdf" でない場合、警告を出力して PDF フォーマットに変更する
    _, file_extension = os.path.splitext(output_file)
    if file_extension.lower() != '.pdf':
        print("警告：出力ファイルの拡張子が '.pdf' ではありません。PDF フォーマットで出力します。")
        output_file = os.path.splitext(output_file)[0] + ".pdf"

    # PDFドキュメントの作成
    doc = SimpleDocTemplate(output_file, pagesize=A4)

    # 表のデータを作成
    table_data = [['', 'Name', 'IN', 'OUT', 'HOME']]
    for position, name in data:
        table_data.append([position, name, '', '', ''])

    # 表のスタイルを設定
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # テキストを上下の中央に配置
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), fontsize), 
                        ('BOTTOMPADDING', (0, 0), (-1, 0), -100),
                        ('TOPPADDING', (0, 0), (-1, 0), -100),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)
                    ])

    # 表を作成
    row_heights = [header_height] + [row_height] * (len(table_data) - 1)
    table = Table(table_data, colWidths=[doc.width/5.0]*5, rowHeights=row_heights)
    table.setStyle(style)

    # 各行の高さを設定
    for i in range(1, len(table_data)):
        table.setStyle(TableStyle([('TEXTCOLOR', (0, i), (-1, i), colors.black),
                                   ('FONTNAME', (0, i), (-1, i), 'Helvetica'),
                                   ('FONTSIZE', (0, i), (-1, i), fontsize),
                                   ('ALIGN', (0, i), (-1, i), 'CENTER'),
                                   ('VALIGN', (0, i), (-1, i), 'MIDDLE'),  # テキストを上下の中央に配置
                                   ]))

    # PDFに表を追加
    doc.build([table])

if __name__ == "__main__":
    args = parse_arguments()

    input_file = args.input
    output_file = args.output

    # ファイルを読み込んでPDFを生成
    with open(input_file, 'r') as file:
        lines = file.read().splitlines()
        data = [line.split(', ') for line in lines]
    print(data)

    create_pdf(data, output_file)
