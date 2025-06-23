# https://atcoder.jp/contests/abc411/tasks/abc411_a

def main():
    L = int(input("必要な長さLを入力してください: "))
    P = input("パスワード文字列Pを入力してください: ")

    if len(P) >= L:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()