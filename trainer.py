import plyvel
import os
from pathlib import Path

roaming = os.getenv('APPDATA')
vs_db_folder = rf'{roaming}\Vampire_Survivors\Local Storage\leveldb'
vs_db_path = Path(vs_db_folder)

if (vs_db_path.exists() and vs_db_path.is_dir()):
    db = plyvel.DB(vs_db_folder, create_if_missing=False)
    db.put(b'_file://\x00\x01CapacitorStorage.Coins', b'\x0199999')

    print('Coins applied')
else:
    print('Game directory not found. exiting')
