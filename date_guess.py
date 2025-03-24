"""
ファイル名: guess_date.py
概要:
    ユーザが想像した月日を当てるプログラムです。
    ユーザが入力したヒントに基づいて、正しい月日を推測します。

使用方法:
    コマンドラインから実行し、画面の指示に従って操作してください。
"""


def format_two_digits(num):
    """数字を0埋めして2桁の文字列に変換する"""
    return f"{num:02d}"


def get_user_input(prompt):
    """プロンプトを表示してユーザの入力を取得する"""
    return input(prompt).strip().lower()


def binary_search_guess(low, high, label):
    """
    low～highの範囲で、ユーザの考えている値を二分探索で推測する。
    label: 推測対象の名前（例: '月', '日'）に利用。
    戻り値: 推測値, 質問回数
    """
    count = 0
    # ループはlow==highになった時点でbreak
    while low < high:
        count += 1
        guess = (low + high) // 2
        guess_view = format_two_digits(guess)
        prompt = f"\nあなたの考えた{label}は {guess_view} より後ですか？（yes/no）: "
        answer = get_user_input(prompt)

        if answer in ("yes", "y"):
            low = guess + 1
        elif answer in ("no", "n"):
            high = guess
        else:
            print("\nyesかnoで回答してください。")
            print("処理を終了します。\n")
            exit(1)
    return low, count


def main():
    print("\n0101から1231までの間で、あなたの好きな日付をひとつ思い浮かべてください。")
    # 二分探索で月は4回（2^4==16）、日は5回（2^5==32）、計9回以内に的中させる
    print("あなたの考えた日付を、二分探索を用いて9回以内に的中させます。")

    # 月の推測（1～12）
    month, month_count = binary_search_guess(1, 12, "月")
    month_view = format_two_digits(month)

    # 日の推測（1～31）
    day, day_count = binary_search_guess(1, 31, "日")
    day_view = format_two_digits(day)

    total_count = month_count + day_count

    print(f"\nあなたの考えた日付は {month_view}{day_view} です。")
    print(f"質問回数: {total_count}回\n")


if __name__ == "__main__":
    main()
