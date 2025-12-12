from js import document


def compute_average(event):
    def num(id):
        el = document.getElementById(id)
        if el and el.value != "":
            try:
                return float(el.value)
            except:
                return 0.0
        return 0.0

    Strength = num("Strength")
    Dexterity = num("Dexterity")
    Constitution = num("Constitution")
    Intelligence = num("Intelligence")
    Wisdom = num("Wisdom")
    Charisma = num("Charisma")

    # safe DOM setter
    def safe_set(id, value):
        el = document.getElementById(id)
        if el:
            el.innerText = value

    safe_set("strength_output", Strength)
    safe_set("dex_output", Dexterity)
    safe_set("const_output", Constitution)
    safe_set("int_output", Intelligence)
    safe_set("wis_output", Wisdom)
    safe_set("char_output", Charisma)

    average = (Strength + Dexterity + Constitution + Intelligence + Wisdom + Charisma) / 6

    first_el = document.getElementById("first")
    last_el = document.getElementById("last")
    first = first_el.value if first_el else ""
    last = last_el.value if last_el else ""

    safe_set("name", f"Name: {first} {last}")
    safe_set("output", f"Your General Weighted Average is {round(average, 2)}")

    container = document.getElementById("grades_container")
    if container:
        container.style.display = "block"