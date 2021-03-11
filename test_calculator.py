import calculator

class TestCalculator:
    def test_add(self):
            assert 8 == calculator.add(3, 5)

    def test_subtract(self):
            assert 6 == calculator.subtract(10, 4)
