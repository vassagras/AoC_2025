from collections import deque

class ManifoldDay07:

    def __init__(self, diagram, beams):
        self.diagram = diagram
        self.max_i = len(diagram) - 1
        self.max_j = len(diagram[0]) - 1

        self.beams = deque(beams)  # more efficient queue
        self.visited = set()  # stores explored positions
        self.splitter_count = 0

    def propagate_step(self, new_pos) -> None:
        """
        Propagate the beam from its new position.

        Parameters
        ----------
        new_pos : tuple[int, int]
            The position's coordinates after the beam propagation.
        """
        i, j = new_pos
        content = self.diagram[i][j]
        new_positions = []

        # Normal forward propagation
        if content == ".":
            new_positions.append((new_pos[0] + 1, new_pos[1] + 0))

        # Splitter case with diagonal propagation
        elif content == "^":
            new_positions += [(i + m[0], j+ m[1]) for m in [(1, -1), (1, 1)]]
            self.splitter_count += 1

        # Validate the new beam positions
        for x, y in new_positions:
            if 0 <= y <= self.max_j and x <= self.max_i:
                if (x, y) not in self.visited:
                    self.beams.append((x, y))
                    self.visited.add((x, y))

    def propagate(self):
        while self.beams:
            self.propagate_step(self.beams.popleft())