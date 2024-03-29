import configparser
from pathlib import Path

from rptodo import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

def get_database_path(config_file: Path) -> Path: 
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]['database'])
 
def init_databae(db_path: Path) -> int: 
    try: 
        db_path.write_text("[]")
        return SUCCESS
    except OSError: 
        return DB_WRITE_ERROR
    
    