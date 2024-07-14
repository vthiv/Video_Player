from Library_Item import LibraryItem

def test_LibraryItem(capsys):
    output = LibraryItem("Tom and Jerry", "Fred Quimby", 4)

    assert output.name == "Tom and Jerry"
    assert output.director == "Fred Quimby"
    assert output.rating == 4

    with capsys.disabled():
        print()
        print(f"tested {output.__class__.__name__} successfully")


def test_LibraryItem2(capsys):
    output = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)

    assert output.name == "Breakfast at Tiffany's"
    assert output.director == "Blake Edwards"
    assert output.rating == 5

    with capsys.disabled():
        print()
        print(f"tested {output.__class__.__name__} successfully")


def test_LibraryItem3(capsys):
    output = LibraryItem("Casablanca", "Michael Curtiz", 2)

    assert output.name == "Casablanca"
    assert output.director == "Michael Curtiz"
    assert output.rating == 2

    with capsys.disabled():
        print()
        print(f"tested {output.__class__.__name__} successfully")


def test_LibraryItem4(capsys):
    output = LibraryItem("The Sound of Music", "Robert Wise", 1)

    assert output.name == "The Sound of Music"
    assert output.director == "Robert Wise"
    assert output.rating == 1

    with capsys.disabled():
        print()
        print(f"tested {output.__class__.__name__} successfully")


def test_LibraryItem5(capsys):
    output = LibraryItem("Gone with the Wind", "Victor Fleming", 3)

    assert output.name == "Gone with the Wind"
    assert output.director == "Victor Fleming"
    assert output.rating == 3

    with capsys.disabled():
        print()
        print(f"tested {output.__class__.__name__} successfully")
