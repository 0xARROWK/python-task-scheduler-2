from view import *


def test():
    atelier = Atelier(machines_nb=2)
    atelier.load_atelier("atelier1.json")
    print(
        "\nNombre de machines : " + str(atelier.machines_nb) +
        "\nTaches : " + str(atelier.tasks) +
        "\nOrdonnancement : " + str(atelier.scheduling)
    )
    total_tasks_time = atelier.total_tasks_time()
    print(
        "\nTemps total de réalisation : " + str(total_tasks_time)
    )
    atelier.add_task("LABEL", "#555", [10, 5])
    print(
        "\n\nTaches ajoutée : " + str(atelier.tasks)
    )
    atelier.edit_task(1, "EDITED", "#000", [20, 5])
    print(
        "\n\nTaches modifiée : " + str(atelier.tasks)
    )
    atelier.remove_task(1)
    print(
        "\n\nTaches supprimée : " + str(atelier.tasks)
    )
    atelier.switch_scheduling(0, 3)
    atelier.switch_scheduling(3, 2)
    print(
        "\n\nOrdonnacement modifié : " + str(atelier.scheduling)
    )
    atelier.save_atelier("test.json")
    atelier.load_atelier("test.json")
    print(
        "\nNombre de machines sauvegardées : " + str(atelier.machines_nb) +
        "\nTaches sauvegardées : " + str(atelier.tasks) +
        "\nOrdonnancement sauvegardé : " + str(atelier.scheduling)
    )
    tasks_time = atelier.tasks_time()
    print(
        "\nTemps de début et de fin des tâches : " + str(tasks_time)
    )
    total_tasks_time = atelier.total_tasks_time()
    print(
        "\nTemps total de réalisation : " + str(total_tasks_time)
    )


if __name__ == '__main__':
    test()
    atelier = Atelier()
    atelier.load_atelier("atelier1.json")
    Window(atelier)
