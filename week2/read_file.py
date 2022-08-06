import random
with open('src/test.txt', 'r') as file:
    f_content = file.read()
    f_content_list = f_content.split("\n")
    f_selection = random.choice(f_content_list)
    print(f_selection)
