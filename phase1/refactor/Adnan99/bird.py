from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        """Perform flying action."""
        raise NotImplementedError

class CanFly(FlyBehavior):
    def fly(self):
        print("Flying")

class CannotFly(FlyBehavior):
    def fly(self):
        raise NotImplementedError("This bird can't fly")

class Bird:
    def __init__(self, fly_behavior: FlyBehavior):
        self._fly_behavior = fly_behavior

    def fly(self):
        return self._fly_behavior.fly()

    def can_fly(self) -> bool:
        return isinstance(self._fly_behavior, CanFly)

class Sparrow(Bird):
    def __init__(self):
        super().__init__(CanFly())

class Ostrich(Bird):
    def __init__(self):
        super().__init__(CannotFly())
