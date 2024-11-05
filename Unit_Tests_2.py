###      #   изменение с 5 на 10
# Пункты задачи:
# 1. Скачайте исходный код для тестов.

import unittest


# Исходный класс Runner
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 10 ###      #   изменение с 5 на 10

    def __str__(self):
        return self.name

# 2. Создайте класс RunnerTest и соответствующие описанию методы.
# Тестовый класс для класса Runner
class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        # Проверяем, что после 10 шагов distance равен 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        # Проверяем, что после 10 пробежек distance равен 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        # runner1 использует run, runner2 использует walk
        for _ in range(10):
            runner1.run()
            runner2.walk()

        # Проверяем, что дистанции разные
        self.assertNotEqual(runner1.distance, runner2.distance)


# 3. Запуск тестов
if __name__ == "__main__":
    unittest.main()

###   Вывод на консоль:
# Failure
# Traceback (most recent call last):
#   File "C:\Users\alexa\PycharmProjects\Module_12_Cycle_Support\Unit_Tests_2.py", line 51, in test_challenge
#     self.assertNotEqual(runner1.distance, runner2.distance)
# AssertionError: 100 == 100
#
#
#
# 50 != 100
#
# Expected :100
# Actual   :50
# <Click to see difference>
#
# Traceback (most recent call last):
#   File "C:\Users\alexa\PycharmProjects\Module_12_Cycle_Support\Unit_Tests_2.py", line 32, in test_walk
#     self.assertEqual(runner.distance, 50)
# AssertionError: 100 != 50
#
#
#
# Ran 3 tests in 0.011s
#
# FAILED (failures=2)