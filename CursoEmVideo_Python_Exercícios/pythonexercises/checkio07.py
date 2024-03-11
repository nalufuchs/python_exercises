def between_markers(text: str, start: str, end: str) -> str:
    i = text.find(start)+1
    end = text.find(end)
    return text[i:end]


print("Example:")
print(between_markers("What is >apple<", ">", "<"))
print(between_markers("What is >apple<", ">", "<"))
print(between_markers("What is [apple]", "[", "]"))
print(between_markers("What is ><", ">", "<"))
print(between_markers("[an apple]", "[", "]"))