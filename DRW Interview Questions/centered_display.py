def centerDisplay(width, content):
    centered = []

    for word in content:
        padding = width - len(word)
        left = padding // 2 + (padding % 2)
        right = padding // 2
        centered.append("." * left + word + "." * right)
    return centered

if __name__ == "__main__":
    result = centerDisplay(11,["middle", "names"])
    print(result)