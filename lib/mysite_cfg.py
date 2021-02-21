import os

import yaml

class MysiteCfg:

    def __init__(self):
        cfg_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'mysitecfg.yml')
        with open(cfg_path, 'r') as fp:
            self.cfg = yaml.load(fp.read(), Loader=yaml.FullLoader)

    @property
    def env(self):
        return self.cfg['ENV']

mysite_cfg = MysiteCfg()