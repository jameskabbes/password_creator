import dir_ops as do
import os
import py_starter as ps
import kabbes_settings

_Dir      = do.Dir( os.path.abspath( __file__ ) ).ascend()
_src_Dir  = do.Dir( os.path.abspath( __file__ ) ).ascend(level_to_ascend=2)
_repo_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend(level_to_ascend=3)
_cwd_Dir  = do.Dir( do.get_cwd() )
data_Dir = _repo_Dir.join_Dir( path = 'Data' )


Dirs = {
"_Dir"      : _Dir,
"_src_Dir"  : _src_Dir,
"_repo_Dir" : _repo_Dir,
"_cwd_Dir"  : _cwd_Dir,
"data_Dir"  : data_Dir,
}


settings = kabbes_settings.Settings( **Dirs )
DEFAULT_SETTINGS_PATH = settings._Dir.join_Path( path = 'default_settings.json' )
settings = kabbes_settings.load_Settings( DEFAULT_SETTINGS_PATH, settings=settings )

### Word List
if not settings.words.Path.exists():
    settings.words.Path.create()

### Imports
from . import main
from . import generator_support