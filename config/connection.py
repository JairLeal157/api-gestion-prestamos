from sqlalchemy import create_engine, MetaData

# Datos de conexión
user = "root"
password = "4JGqspLoqSqAmIien753"
host = "containers-us-west-159.railway.app"
port = "5964"
database = "railway"

# Crear la cadena de conexión
string_connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

# Crear el motor de la base de datos y la metadatos
engine = create_engine(string_connection)
meta = MetaData()



