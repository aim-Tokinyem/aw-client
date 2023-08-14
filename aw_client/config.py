from aw_core.config import load_config_toml

default_config = """
[server]
hostname = "localhost"
port = "5600"
protocol = "https"

[client]
commit_interval = 10

[server-testing]
hostname = "localhost"
port = "5666"
protocol = "https"

[client-testing]
commit_interval = 5
""".strip()


def load_config():
    return load_config_toml("aw-client", default_config)
