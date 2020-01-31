from zope.interface import Attribute, Interface, implementer


class ICrendentialStorageInterface(Interface):
    """ Storage Interface """

    uuid = Attribute("Credential universally unique identifier")
    email = Attribute("Credential owner email")
    password = Attribute("Write-only credential password")
    name = Attribute("Credential owner name")
    username = Attribute("Credential owner username")
    msisdn = Attribute("Credential owner msisdn")
    citizen_id = Attribute("Credential owner citizen id")
    metadata = Attribute("Credential metadata")

    def create():
        """ Create """

    def get_by():
        """ Get Credential by attribute """

    def check_password():
        """ Check Password """


@implementer(ICrendentialStorageInterface)
class Storage:
    def create(self):
        from keyloop.models.credentials import Credential

        return Credential()
