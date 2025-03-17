from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Configuración de la base de datos
engine = create_engine('sqlite:///tickets.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Modelo de Tickets
class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    email = Column(String)
    problema = Column(String)
    prioridad = Column(String)
    estado = Column(String)
    fecha = Column(DateTime, default=datetime.utcnow)

# Crear la tabla si no existe
Base.metadata.create_all(engine)

# Funciones CRUD
def crear_ticket(nombre, email, problema, prioridad, estado="Abierto", fecha=None):
    if not fecha:
        fecha = datetime.utcnow()
    nuevo_ticket = Ticket(
        nombre=nombre,
        email=email,
        problema=problema,
        prioridad=prioridad,
        estado=estado,
        fecha=fecha
    )
    session.add(nuevo_ticket)
    session.commit()

def obtener_tickets():
    return session.query(Ticket).all()

def actualizar_estado_ticket(ticket_id, nuevo_estado):
    ticket = session.query(Ticket).filter_by(id=ticket_id).first()
    if ticket:
        ticket.estado = nuevo_estado
        session.commit()

def eliminar_ticket(ticket_id):
    ticket = session.query(Ticket).filter_by(id=ticket_id).first()
    if ticket:
        session.delete(ticket)
        session.commit()
