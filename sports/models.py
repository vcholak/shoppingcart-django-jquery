from django.conf import settings


#class Product():
#    __tablename__ = "product"
#    id = Column(Integer, primary_key=True)
#    name = Column(String(20), nullable=False, unique=True, index=True)
#    description = Column(String(200), nullable=False)
#    category = Column(String(50), nullable=False)
#    price = Column(Float, nullable=False)

#    @classmethod
#    def all(cls):
#        return session.query(Product).all()

#    def __init__(self, name, description, category, price):
#        self.name = name
#        self.description = description
#        self.category = category
#        self.price = price

#    def __repr__(self):
#        return '<Product %r>' % self.name

#    def add(self):
#        session.add(self)
#        session.commit()
#        return self.id


#if not test:
#database_uri = 'postgresql://' + settings.DATABASES['default']['USER'] + ':' + settings.DATABASES['default']['PASSWORD'] + \
#               '@' + settings.DATABASES['default']['HOST'] + '/' + settings.DATABASES['default']['NAME']
#else:
#    database_uri = 'sqlite:///' + app.config['DATABASE']

#engine = create_engine(database_uri, convert_unicode=True)
#Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#session = scoped_session(Session)
#Base.metadata.bind = engine
#Base.metadata.create_all()  # creates all tables if they are not created yet