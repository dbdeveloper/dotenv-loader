from pathlib import Path

def test_load_env(*args, **kwargs) -> Path:
   dotenv_loader = args[0]
   rest_args = args[1:]
   return dotenv_loader.load_env(*rest_args, **kwargs)
