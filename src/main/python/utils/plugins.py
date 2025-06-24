from typing import Callable, Type, TypeVar, Generic, Dict, Optional

T = TypeVar("T")


class PluginRegistry(Generic[T]):
    def __init__(self):
        self.registry: Dict[str, Type[T]] = {}

    def _register(self, name: str, class_: Type[T]) -> None:
        reg_class = self.registry.setdefault(name, class_)
        if reg_class is not class_:
            raise RuntimeError(f'Attempting to re-register {name} which was already set to {reg_class!r}')

    def register_as(self, name: str) -> Callable[[Type[T]], Type[T]]:
        def decorator(class_: Type[T]) -> Type[T]:
            self._register(name, class_)
            return class_
        return decorator

    def create_instance(self, name: str, **kwargs) -> Optional[Type[T]]:
        "Get the appropriate executor class from the registry and creates the instance of it"
        if name not in self.registry:
            raise ValueError(f'Executor {name} does not exist in the registry')

        exec_class = self.registry[name]
        executor = exec_class(**kwargs)
        return executor

