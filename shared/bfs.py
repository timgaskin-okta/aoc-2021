from queue import Queue
from typing import Any, Iterable, Callable, Set


class BFS:
    def __init__(self,
                 start: Any,
                 search_space: Iterable[Any],
                 neighbor_function: Callable[[Any, Iterable[Any], Iterable[Any]], Iterable[Any]],
                 end_condition: Callable[[Any, Iterable[Any]], bool] = lambda _, __: False,
                 count_condition: Callable[[Any, Iterable[Any]], bool] = lambda _, __: False) -> None:
        self.start = start
        self.search_space = search_space
        self.end_condition = end_condition
        self.count_condition = count_condition
        self.neighbor_function = neighbor_function

        self.end_node = None
        self.paths = set()
        self.total_visited = None
        self.count = 0

    def run(self):
        queue = Queue()
        queue.put((self.start, [self.start]))

        curr_node = None
        total_visited = 0
        while not queue.empty():
            curr_node, path = queue.get()
            total_visited += 1
            if self.end_condition(curr_node, self.search_space):
                self.end_node = curr_node
                self.paths.add(tuple(path))
                self.total_visited = total_visited
                return self
            elif self.count_condition(curr_node, self.search_space):
                self.paths.add(tuple(path))
                self.count += 1
            else:
                for neighbor in self.neighbor_function(curr_node, path, self.search_space):
                    neighbor_path = path[:] + [neighbor]
                    queue.put((neighbor, neighbor_path))

        self.end_node = curr_node
        self.total_visited = total_visited
        return self
