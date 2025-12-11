import os

from rich import print


async def create_folder(base_path: str, path: str) -> str:
    """
    Return the full path, if  `upload` destination exists,
    if not exist, then create destination, then return full path
    """
    
    # upload path
    _full_path: str = os.path.join(base_path, path)
    
    if os.path.exists(_full_path):
        # if path exist
    
        print("\n\t[bold green]Upload found :)[/bold green]\n")
        return _full_path
    else:
        # if path doesnot exist
    
        print("\n\t[italic red]Upload didn't exists :([/italic red]")
        print("\t[italic yellow]Creating the Upload[/italic yellow]")
        os.mkdir(_full_path)
        print("\t[bold green]Upload Created  :)[/bold green]\n")
        return _full_path
        