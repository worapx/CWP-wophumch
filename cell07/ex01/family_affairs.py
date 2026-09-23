def family_affairs(family):
    return list(filter(lambda name: family[name] == "red", family))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}
print(family_affairs(dupont_family))