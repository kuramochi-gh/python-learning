"""
ファイル名: guess_date.py
概要:
    ユーザが想像した月日を当てるプログラムです。
    ユーザが入力したヒントに基づいて、正しい月日を推測します。

使用方法:
    コマンドラインから実行し、画面の指示に従って操作してください。
"""

print("0101から1231までの間で、あなたの好きな日付をひとつ思い浮かべてください。")
print("あなたの考えた日付を、二分探索を用いて9回以内に的中させます。")

month_low = 1
month_high = 12
day_low = 1
day_high = 31
month_guess_view = None
day_guess_view = None

# 月を特定する
for i in range(4):
    # month_lowとmonth_highjが同じ場合、ループを抜ける
    if month_low == month_high:
        month_guess_view = month_low
        break

    # 推測値を確認
    month_guess = (month_low + month_high) // 2
    if len(str(month_guess)) == 1:
        month_guess_view = "0" + str(month_guess)
    else:
        month_guess_view = month_guess

    print("あなたの考えた日付は", month_guess_view, "より後の月ですか？（yes/no）")
    answer = input()

    if answer in ("yes", "y"):
        month_low = month_guess + 1
    elif answer in ("no", "n"):
        month_high = month_guess
    else:
        print("yesかnoで回答してください。")
        print("処理を終了します。")
        exit()

# 日を特定する
for i in range(5):
    # day_lowとday_highjが同じ場合、ループを抜ける
    if day_low == day_high:
        day_guess_view = day_low
        break

    # 推測値を確認
    day_guess = (day_low + day_high) // 2
    if len(str(day_guess)) == 1:
        day_guess_view = "0" + str(day_guess)
    else:
        day_guess_view = day_guess

    print(
        "あなたの考えた日付は",
        str(month_guess_view) + str(day_guess_view),
        "より後の日付ですか？（yes/no）",
    )
    answer = input()

    if answer in ("yes", "y"):
        day_low = day_guess + 1
    elif answer in ("no", "n"):
        day_high = day_guess
    else:
        print("yesかnoで回答してください。")

print("あなたの考えた日付は", str(month_guess_view) + str(day_guess_view), "です")
