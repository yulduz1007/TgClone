import random


def random_code():
    code = random.randrange(10**5 , 10**6)
    return code

def choose_emoji():
    emoji_list = "👨🏻 ‍💻 👩 ‍🏫 👨 ‍🌾 🤠 🤡 👹 👮 👷‍".split()
    for pos , emoji in enumerate(emoji_list,1):
        print(f"{pos}) {emoji}")

    pos = int(input(">>>"))
    return emoji_list[pos-1]

