class Addr:
    def __init__(self, name: str = None, tel: str = None, addr: str = None):
        self.name = name
        self.tel = tel
        self.addr = addr

    def __str__(self):  # java toString(), 객체 설명문
        return 'name: ' + self.name + ', tel: ' + self.tel + ', addr: ' + self.addr
