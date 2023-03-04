import json


class Atelier:

    def __init__(self, machines_nb=0, tasks=None, scheduling=None):
        if scheduling is None:
            scheduling = []
        if tasks is None:
            tasks = []
        self.machines_nb = machines_nb
        self.tasks = tasks
        self.scheduling = scheduling

    def load_atelier(self, filepath):
        file = open(filepath)
        data = json.load(file)
        self.machines_nb = data.get("M")
        self.tasks = data.get("taches")
        self.scheduling = data.get("ordonnancement")

    def save_atelier(self, file):
        data = {
            "M": self.machines_nb,
            "taches": self.tasks,
            "ordonnancement": self.scheduling
        }
        with open(file, 'w') as output:
            json.dump(data, output)

    def add_task(self, label, color, p):
        self.tasks.append({
            "id": len(self.tasks),
            "label": label,
            "couleur": color,
            "p": p
        })

    def edit_task(self, to_edit, label, color, p):
        for t in self.tasks:
            if t.get("id") == to_edit:
                t.update({
                    "label": label,
                    "couleur": color,
                    "p": p
                })

    def remove_task(self, id):
        self.tasks[:] = [t for t in self.tasks if t.get("id") != id]
        for t in self.tasks:
            t.update({"id": self.tasks.index(t)})

    def switch_scheduling(self, schedule1, schedule2):
        a, b = self.scheduling.index(schedule1), self.scheduling.index(schedule2)
        self.scheduling[b], self.scheduling[a] = self.scheduling[a], self.scheduling[b]

    def tasks_time(self):
        tasks_time = []
        precedent_task_end = 0
        for task in self.tasks:
            total_task_time = 0
            tasks_time.append({
                "id": task.get("id")
            })
            for time in task.get("p"):
                total_task_time += time
                tasks_time[-1]["m" + str(task.get("p").index(time) + 1)] = time
            tasks_time[-1]["start"] = precedent_task_end
            tasks_time[-1]["end"] = precedent_task_end + total_task_time
            precedent_task_end = precedent_task_end + total_task_time
        return tasks_time

    def total_tasks_time(self):
        return self.tasks_time()[-1]["end"]

    def johnson_algo(self):
        m1, m2 = [], []
        for t in self.tasks:
            if t.get("p")[0] < t.get("p")[1]:
                m1.append({
                    "id": t.get("id"),
                    "time": t.get("p")[0]
                })
            else:
                m2.append({
                    "id": t.get("id"),
                    "time": t.get("p")[1]
                })
        m1 = sorted(m1, key=lambda v: v.get("time"), reverse=True)
        m2 = sorted(m2, key=lambda v: v.get("time"), reverse=True)
        return m1, m2
