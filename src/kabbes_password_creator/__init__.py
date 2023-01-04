import dir_ops as do
import os
import py_starter as ps

_Dir      = do.Dir( os.path.abspath( __file__ ) ).ascend()
_src_Dir  = do.Dir( os.path.abspath( __file__ ) ).ascend(level_to_ascend=2)
_repo_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend(level_to_ascend=3)


DEFAULT_CONFIG_PATH = _Dir.join_Path( path = 'default_config.json' )

### Imports
from .Client import Client