from config.db import Base
from sqlalchemy import ForeignKey, String, Column, Integer, Boolean, DateTime, Float, Enum, JSON, Date, Text
from sqlalchemy.orm import relationship
import enum

class Role(enum.Enum):
    user = "user"
    admin = "admin"
    avocat = "avocat"

class Days(enum.Enum):
    lundi = "lundi"
    mardi = "mardi"
    mercredi = "mercredi"
    jeudi = "jeudi"
    vendredi = "vendredi"
    samedi = "samedi"
    dimanche = "dimanche"

class AvocatStatus(enum.Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"

class AppointmentStatus(enum.Enum):
    pending = "pending"
    done = "done"
    canceled = "canceled"

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(255))
    prenom = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255), nullable=True)
    isGoogleUser = Column(Boolean, default=False)
    createdAt = Column(DateTime)
    role = Column(Enum(Role), default="user")
    avocat = relationship("Avocat", back_populates="user")
    rating = relationship("Rating", back_populates="user")
    appointments = relationship("Appointment", back_populates="user")

class Avocat(Base):
    __tablename__ = "avocat"
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String(255))
    wilaya = Column(String(50))
    phoneNumber = Column(String(255))
    facebookUrl = Column(String(255))
    description = Column(Text)
    status = Column(Enum(AvocatStatus), default="pending")
    isBlocked = Column(Boolean, default=False)
    categories = Column(JSON)
    workDays = Column(JSON)
    rate = Column(Float, default=0)
    imageUrl = Column(String(255), nullable=True)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)
    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="avocat")
    rating = relationship("Rating", back_populates="avocat")
    availabilities = relationship("AvailabilityAvocat", back_populates="avocat")
    appointments = relationship("Appointment", back_populates="avocat")
    
class Rating(Base):
    __tablename__ = "rating"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("user.id"))
    avocatId = Column(Integer, ForeignKey("avocat.id"))
    rate = Column(Float)
    createdAt = Column(DateTime)
    avocat = relationship("Avocat", back_populates="rating")
    user = relationship("User", back_populates="rating")
    comment = relationship("Comment", back_populates="rating")
    
class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, index=True)
    ratingid = Column(Integer, ForeignKey("rating.id"))
    comment = Column(String(255))
    rating = relationship("Rating", back_populates="comment")


class Availability(Base):
    __tablename__ = "availability"
    id = Column(Integer, primary_key=True, index=True)
    start = Column(String(255))
    end = Column(String(255))
    avocats = relationship("AvailabilityAvocat", back_populates="availability")
    appointments = relationship("Appointment", back_populates="availability")

class AvailabilityAvocat(Base):
    __tablename__ = "availability_avocat"
    avocatId = Column(Integer, ForeignKey("avocat.id"), primary_key=True)
    avocat = relationship("Avocat", back_populates="availabilities")
    availabilityId = Column(Integer, ForeignKey("availability.id"), primary_key=True)
    availability = relationship("Availability", back_populates="avocats")

class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    status = Column(Enum(AppointmentStatus), default="pending")
    phoneNumber = Column(String(255))
    description = Column(String(255))
    avocatId = Column(Integer, ForeignKey("avocat.id"))
    avocat = relationship("Avocat", back_populates="appointments")
    userId = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="appointments")
    availabilityId = Column(Integer, ForeignKey("availability.id"))
    availability = relationship("Availability", back_populates="appointments")
