from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, select, delete


class DBInterface:
    def __init__(self, db_url='sqlite:///list.db'):
        # Create a SQLAlchemy database engine
        self.engine = create_engine(db_url, echo=True)
        # Define metadata for database tables
        self.metadata = MetaData()
        # Define a 'tasks' table with columns: task_id (primary key) and task (string)
        self.tasks_table = Table(
            "tasks",
            self.metadata,
            Column("task_id", Integer, primary_key=True, autoincrement=True),
            Column("task", String))
        # Create the tables in the database if they do not exist
        self.metadata.create_all(bind=self.engine)
        # Create a session factory for interacting with the database
        self.Session = sessionmaker(bind=self.engine)

    def create_task(self, task_name):
        # Create a new task in the database
        session = self.Session()
        statement = insert(self.tasks_table).values(task=task_name)
        session.execute(statement)
        session.commit()
        session.close()

    def get_all_tasks(self):
        # Retrieve all tasks from the database
        session = self.Session()
        statement = select(self.tasks_table)
        tasks = session.execute(statement)
        # Convert the result to a dictionary to be able to query the data
        tasks = dict(tasks.fetchall())
        session.close()
        return tasks

    def delete_task(self, task_id):
        # Delete a specific task by task_id
        session = self.Session()
        statement = delete(self.tasks_table).where(self.tasks_table.c.task_id == task_id)
        result = session.execute(statement)
        rows_affected = result.rowcount  # Number of rows affected by the delete operation
        session.commit()
        session.close()
        if rows_affected == 0:
            # If no rows were affected, task_id was not found
            return None
        else:
            # Deletion successful
            return True

    def delete_all_tasks(self):
        # Delete all tasks from the database to delete the list
        session = self.Session()
        statement = delete(self.tasks_table)
        session.execute(statement)
        session.commit()
        session.close()
