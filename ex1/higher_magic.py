from collections.abc import Callable

Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell(target: str, power: int) -> str:
    return f"Spell affects {target} for {power} power"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
            spell1: Spell,
            spell2: Spell
        ) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power)
        )
    return combined


def power_amplifier(
            base_spell: Spell,
            multiplier: int
        ) -> Spell:
    def amplified_spell(target: str, power: int) -> str:
        return (
            base_spell(target, power * multiplier)
        )
    return amplified_spell


def conditional_caster(
            condition: Condition,
            spell: Spell
        ) -> Spell:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return (spell(target, power))
        else:
            return "Spell fizzled"
    return caster


def enough_power(
            _: str,
            power: int
        ) -> bool:
    return power >= 50


def spell_sequence(
            spells: list[Spell]
        ) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [
            spell(target, power)
            for spell in spells
        ]
    return sequence


if __name__ == "__main__":

    # print(fireball("Dragon", 29))
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)("Dragon", 100)
    print(
        f"Combined spell result: "
        f"{combined[0]}, {combined[1]}\n"
    )

    print("Testing power amplifier...")
    original = fireball("Dragon", 10)
    amplified = power_amplifier(fireball, 3)("Dragon", 10)
    print(
        f"Original: {original}\n"
        f"Amplified: {amplified}\n"
    )

    print("Testing conditional caster...")
    print(conditional_caster(enough_power, fireball)("Dragon", 10))

    print("\nTesting spell sequence...")
    spells: list[Spell] = [fireball, heal]
    sequence = spell_sequence(spells)
    for result in sequence("Dragon", 50):
        print(result)
