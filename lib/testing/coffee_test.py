from lib.coffee import Coffee

def test_coffee_creation():
    coffee = Coffee("Small", 5)
    assert coffee.size == "Small"
    assert coffee.price == 5

def test_tip(capsys):
    coffee = Coffee("Medium", 10)
    coffee.tip()
    captured = capsys.readouterr()
    assert "This coffee is great" in captured.out
    assert coffee.price == 11