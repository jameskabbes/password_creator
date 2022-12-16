import dir_ops as do
import os
import py_starter as ps

_Dir = do.Dir( os.path.abspath( __file__ ) ).ascend()   #Dir that contains the package 
_src_Dir = _Dir.ascend()                                  #src Dir that is one above
_repo_Dir = _src_Dir.ascend()                    
_cwd_Dir = do.Dir( do.get_cwd() )
data_Dir = _repo_Dir.join_Dir( path = 'Data' )

settings_Path = _Dir.join_Path( path = 'default_settings.json' )
settings = ps.Settings( **ps.json_to_dict( settings_Path.read() ) )

### Word List
if settings.word_list.path == '':
    if settings.word_list.inside_data_dir:
        words_Path = data_Dir.join_Path( path = settings.word_list.rel_path )

else:
    words_Path = do.Path( settings.word_list.path )

if not words_Path.exists():
    words_Path.create()

### Imports
from . import main
from . import generator_support