def get_texts_for_table():
    texts = []
    with open("./data/texts.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            text, definition, source = line.split(";")
            texts.append([cnt, text, definition])
            cnt += 1
    return texts

