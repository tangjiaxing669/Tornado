#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = "Jason Tom"

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(45), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    def __repr__(self):
        return "<Users(id={}, username={})>".format(self.id, self.username)

class OperatorDb:
    def __init__(self, session):
        self._session = session

    def insert(self, **kwargs):
        data_line = Users(**kwargs)
        try:
            self._session.add(data_line)
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise e

    def query(self):
        result_dict = dict()
        result = self._session.query(Users).all()
        for res in result:
            result_dict[res.username] = res.password
        return result_dict

class Main:
    def get_opt(self):
        engine = create_engine('mysql+pymysql://root:redhat@127.0.0.1:3306/users')
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()
        opt = OperatorDb(session)
        return opt
