from time import sleep
from example import Example


def main(*args, **kwargs):
    """"""
    sleep(5)
    test = Example("test_table")
    test.create_table()
    test.insert("test", "test", "test", "test")
    test.get("test", "test")
    test.update("test", "test", "no", "no")
    test.get("test", "test")

    test.remove_table()


if __name__ == "__main__":
    main()
