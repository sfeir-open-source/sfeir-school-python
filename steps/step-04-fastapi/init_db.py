from databases import Database
import asyncio

db = Database('sqlite:///test.db')

async def main():

  await db.connect()

  await db.execute("""
  CREATE TABLE IF NOT EXISTS messages (
    id integer PRIMARY KEY,
    author text NOT NULL,
    creation_date datetime default current_timestamp,
    message text NOT NULL);
  """)
  await db.disconnect()


asyncio.run(main())
