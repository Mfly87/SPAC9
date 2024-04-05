class MySQLServerCredentials():
    def __init__(self, host: str, user: str, password: str, port: int) -> None:
        self._host = host
        self._user = user
        self._password = password
        self._port = port

    @property
    def host(self) -> str:
        return self._host
    
    @property
    def user(self) -> str:
        return self._user
    
    @property
    def password(self) -> str:
        return self._password
    
    @property
    def port(self) -> int:
        return self._port
    
    def get_credentials_dict(self):
        return {
            "host": self.host,
            "user": self.user,
            "password": self.password,
            "port": self.port,
        }
        