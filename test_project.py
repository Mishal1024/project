import project


def test_add_task():
    tasks = []
    project.add_task("task","medium",tasks)
    assert tasks[-1].task == "task" and tasks[-1].priority == "medium" and tasks[-1].done == "Incomplete"

def test_mark_task():
    tasks = []
    project.add_task("task","medium",tasks)
    project.mark_task(0,tasks)
    assert tasks[-1].done == "Complete"