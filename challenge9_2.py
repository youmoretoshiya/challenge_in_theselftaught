while True:
    ans = input('年齢を入力してください。終了する場合はqを入力してください。:')
    if ans == "q":
        print("終了します")
        break
    else:
        try:
            ans = int(ans)
            with open("age.txt", "a") as f:
                f.write(str(ans))
                f.write()
        except ValueError as error:
            print("数字を入力してください")
