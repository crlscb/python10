from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return reduce(max, spells)
    elif operation == "min":
        return reduce(min, spells)
    raise ValueError(f"Unknown operation: {operation}")


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment ({power}) on {target}"


def partial_enchanter(
            base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:
    fire = partial(base_enchantment, 50, "Fire")
    ice = partial(base_enchantment, 50, "Ice")
    lightning = partial(base_enchantment, 50, "Lightning")

    return {
        "fire": fire,
        "ice": ice,
        "lightning": lightning
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0

    if n == 1:
        return 1

    return (
          memoized_fibonacci(n - 1)
          + memoized_fibonacci(n - 2)
    )


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int) -> str:
        return f"{spell} damage"

    @dispatch.register
    def _(spell: str) -> str:
        return spell

    @dispatch.register
    def _(spell: list[Any]) -> str:
        return f"{len(spell)} spells"

    return dispatch


if __name__ == "__main__":

    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    sum_r = spell_reducer(spells, "add")
    product = spell_reducer(spells, "multiply")
    max_r = spell_reducer(spells, "max")
    min_r = spell_reducer(spells, "min")

    print(f"Sum: {sum_r}")
    print(f"Product: {product}")
    print(f"Max: {max_r}")
    print(f"Min: {min_r}")
    try:
        spell_reducer(spells, "division")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting partial applications...")
    enchanters = partial_enchanter(base_enchantment)

    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))
    print(enchanters["lightning"]("Staff"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")

    dispatcher = spell_dispatcher()

    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher([1, 2, 3])}")
    print(dispatcher(3.14))
