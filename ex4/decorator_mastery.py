<<<<<<< HEAD
from collections.abc import Callable
from typing import Any
import functools
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        final = end - start

        print(f"Spell completed in {final:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args[2] < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args, **kwargs)

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for x in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(
                            f"Spell failed, retrying... "
                            f"(attempt {x + 1}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if not name.replace(" ", "").isalpha():
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}\n")

    print("Testing retrying spell...")
    guild = MageGuild()

    @retry_spell(3)
    def waaaaagh() -> str:
        raise ValueError("Boom")

    print(waaaaagh())
    print()

    print("Testing MageGuild...")
    print(guild.validate_mage_name("Gandalf The Mage"))
    print(guild.validate_mage_name("Gandalf123"))
    print(guild.cast_spell("Lighting", 15))
    print(guild.cast_spell("Lighting", 2))
=======
from collections.abc import Callable
from typing import Any
import functools
import time


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        final = end - start

        print(f"Spell completed in {final:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args[2] < min_power:
                return "Insufficient power for this spell"
            else:
                return func(*args, **kwargs)

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for x in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    print(
                            f"Spell failed, retrying... "
                            f"(attempt {x + 1}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if not name.replace(" ", "").isalpha():
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    print(f"Result: {fireball()}\n")

    print("Testing retrying spell...")
    guild = MageGuild()

    @retry_spell(3)
    def waaaaagh() -> str:
        raise ValueError("Boom")

    print(waaaaagh())
    print()

    print("Testing MageGuild...")
    print(guild.validate_mage_name("Gandalf The Mage"))
    print(guild.validate_mage_name("Gandalf123"))
    print(guild.cast_spell("Lighting", 15))
    print(guild.cast_spell("Lighting", 2))
>>>>>>> 470fb54 (ending 03/04)
