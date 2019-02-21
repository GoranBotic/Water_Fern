import pkgutil

#Loop through all packages in this directory, append them to __all__
__all__ = []
for loader, name, pkg in  pkgutil.walk_packages(__path__):
    __all__.append(name)