from typing import Any


def artifact_sorter(
        artifacts: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"],
        reverse=True
        )


def power_filter(
        mages: list[dict[str, Any]],
        min_power: int
) -> list[dict[str, Any]]:
    return list(
        filter(
            lambda mage: mage["power"] >= min_power,
            mages
        )
    )


def spell_transformer(
        spells: list[str]
) -> list[str]:
    return list(
        map(
            lambda spell: "* " + spell + " *",
            spells
        )
    )


def mage_stats(
        mages: list[dict[str, Any]]
) -> dict[str, Any]:
    return {
        "max_power": max(
            mages,
            key=lambda mage: mage["power"]
        )["power"],
        "min_power": min(
            mages,
            key=lambda mage: mage["power"]
        )["power"],
        "avg_power": round(
            sum(
                map(lambda mage: mage["power"], mages)
            ) / len(mages),
            2
        )
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 89, "type": "focus"},
        {"name": "Fire Staff", "power": 100, "type": "weapon"},
        {"name": "Ancient Crown", "power": 250, "type": "relic"}
    ]
    print(artifact_sorter(artifacts))

    mages = [
        {"name": "Aldric", "power": 45, "element": "Fire"},
        {"name": "Lyra", "power": 120, "element": "Ice"},
        {"name": "Thorne", "power": 80, "element": "Earth"},
        {"name": "Selene", "power": 95, "element": "Light"},
        {"name": "Zephyr", "power": 200, "element": "Wind"},
        {"name": "Mordered", "power": 100, "element": "Darkness"}
    ]
    print(power_filter(mages, 100))

    spells = ["fireball", "heal", "shield", "teleport"]
    print(spell_transformer(spells))

    print(mage_stats(mages))
