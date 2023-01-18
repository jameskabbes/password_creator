import kabbes_client
import kabbes_password_creator
import py_starter as ps

class Client( kabbes_password_creator.PasswordCreator ):

    _BASE_DICT = {
        "_repo_Dir": kabbes_password_creator._repo_Dir
    }

    def __init__( self, dict={} ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        self.Package = kabbes_client.Package( kabbes_password_creator._Dir, dict=d )
        self.cfg_password = self.Package.cfg

        kabbes_password_creator.PasswordCreator.__init__( self )
