from api.config import ConfigEnv

def test_config_env():
    env = {
        "PORT": "8080",
        "JSON_DIR": "test-json",
        "ENVIRON": "dev",
        "LOG_LEVEL": "DEBUG",
        "LOG_DIR": "/var/log"
    }
    config = ConfigEnv(env)
    assert config.PORT == 8080
    assert config.JSON_DIR == "test-json"
    assert config.ENVIRON == "dev"
    assert config.LOG_LEVEL == "DEBUG"
    assert config.LOG_DIR == "/var/log"

def test_wrong_values():
    env = {
        "PORT": "8080",
        "JSON_DIR": "test-json",
        "ENVIRON": "dev",
        "LOG_LEVEL": "DEBUG",
        "LOG_DIR": "/var/log"
    }
    try:
        config = ConfigEnv(env)
        assert False
    except Exception:
        assert True

def test_wrong_LOG_LEVEL():
    env = {
        "PORT": 8080,
        "JSON_DIR": "test-json",
        "ENVIRON": "dev",
        "LOG_LEVEL": "WRONG",
        "LOG_DIR": "/var/log"
    }
    try:
        config = ConfigEnv(env)
        assert False
    except Exception:
        assert True
    