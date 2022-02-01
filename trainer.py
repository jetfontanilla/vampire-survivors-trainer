import plyvel
import os

roaming = os.getenv('APPDATA')
vs_db_folder = rf'{roaming}\Vampire_Survivors\Local Storage\leveldb'

db = plyvel.DB(vs_db_folder, create_if_missing=False)
db.put(b'_file://\x00\x01CapacitorStorage.Coins', b'\x0199999')

print('Coins applied')