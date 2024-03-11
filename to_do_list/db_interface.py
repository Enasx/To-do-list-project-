from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, select, delete


class DBInterface:
    def __init__(self, db_url='sqlite:///list.db'):
        self.engine = create_engine(db_url, echo=True)
        self.metadata = MetaData()
        self.tasks_table = Table(
            "tasks",
            self.metadata,
            Column("task_id", Integer, primary_key=True, autoincrement=True),
            Column("task", String))
        self.metadata.create_all(bind=self.engine)

        self.Session = sessionmaker(bind=self.engine)

    def create_task(self, task_name):
        session = self.Session()
        statement = insert(self.tasks_table).values(task=task_name)
        session.execute(statement)
        session.commit()
        session.close()

    def get_all_tasks(self):
        session = self.Session()
        statement = select(self.tasks_table)
        tasks = session.execute(statement)
        tasks = dict(tasks.fetchall())
        print(tasks)
        session.close()
        return tasks

    def delete_task(self, task_id):
        try:
            session = self.Session()
            statement = delete(self.tasks_table).where(task_id=task_id)
            session.execute(statement)
            session.commit()
            session.close()
            return True
        except Exception:
            return None

    def delete_all_tasks(self):
        session = self.Session()
        statement = delete(self.tasks_table)
        session.execute(statement)
        session.commit()
        session.close()
