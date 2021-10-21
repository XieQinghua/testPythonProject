# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('测试下，大王叫我来巡山')
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != k) and (i != j) and (j != k):
                    print(i, j, k)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
