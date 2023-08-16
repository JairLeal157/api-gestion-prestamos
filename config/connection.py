from sqlalchemy import create_engine, MetaData

# Datos de conexión
user = "root"
password = "pJebl3zB3k6hCExS3Nyv"
host = "containers-us-west-149.railway.app"
port = "6839"
database = "railway"

# Crear la cadena de conexión
string_connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

# Crear el motor de la base de datos y la metadatos
engine = create_engine(string_connection)
meta = MetaData()



