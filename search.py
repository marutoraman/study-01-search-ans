import os

'''
定数は大文字で定義する
'''
# csv_path
SOURCE_CSV_PATH = "source.csv"
# csvが存在しない場合の初期データ
DEFAULT_CARACTORS = ["ぜんいつ", "たんじろう", "ねずこ", "いのすけ"]

'''
処理は細かく関数化する
関数化のポイント、関数内には具体的な内容は記述せずに引数に持たせる
この処理でしか使えなくなってしまうような記述は極力避けて
別のプロジェクトに使い回す前提で記述する
'''
def read_source(csv_path:str):
    '''
    sourceをCSVから読み込む
    関数の基本は、引数(今回はcsv_path) → 処理(関数の中身) → 戻り値(return)
    '''
    # ファイルが存在しない場合は、初期値で新規作成
    if not os.path.exists(csv_path):
        print(f"csv_path:{csv_path} が存在しません。新規作成します。")
        write_source(csv_path, DEFAULT_CARACTORS)
    # ファイルを読み込み
    with open(csv_path, 'r', encoding="utf-8_sig") as f:
        return f.read().splitlines() # readでファイル読み込み、splitlinesで１行づつに分解してlistとして返す


def write_source(csv_path:str, source:list):
    '''
    sourceをcsvに書き込む
    '''
    with open(csv_path, 'w', encoding="utf-8_sig") as f:
        f.write("\n".join(source)) # listを改行(\n)で連結してファイルに書き込む
        
    # 特に戻り値が必要ない場合はreturnは省略できる、その場合はNoneが返る


def search():
    '''
    mainとなる検索処理
    '''
    # sourceをcsvから読み込む
    source = read_source(SOURCE_CSV_PATH)
    
    # While Trueにすると無限に繰り返す
    while True:
        # ユーザー入力
        word=input("鬼滅の登場人物を入力　＞＞　")
        # 検索
        if word in source:
            print(f"『{word}』は登録されています。")
        else:
            print(f"『{word}』は未登録です。")
            # 追加
            is_add=input("追加登録しますか？(n:しない y:する)　＞＞　")
            if is_add == "y":
                source.append(word)
        
        # sourceをcsvに書き込む
        write_source(SOURCE_CSV_PATH, source=source)


'''
実行時に呼び出したい関数を記述する
if __name__等の記述は、今の段階では、定型文として覚えるだけで良い
'''
if __name__ == "__main__":
    search()