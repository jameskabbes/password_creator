import kabbes_user_client
import kabbes_menu
import kabbes_password_creator
import py_starter as ps

class Client( kabbes_password_creator.PasswordCreator ):

    BASE_CONFIG_DICT = {
        "_Dir": kabbes_password_creator._Dir,
        "_repo_Dir": kabbes_password_creator._repo_Dir
    }

    def __init__( self, dict={}, **kwargs ):

        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        self.cfg_password = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        kabbes_password_creator.PasswordCreator.__init__( self )
