
from abc import ABC
import configparser


class CoreObject(ABC):
    
    @property
    def platform(self):
        if 'PLATFOEM' not in globals():
            env = configparser.ConfigParser()
            env.read('./env.ini')
            global PLATFOEM
            PLATFOEM = env['environment']['platform']
        return PLATFOEM
