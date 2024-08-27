from sqlalchemy import  create_engine, text

engine = create_engine("postgresql+psycopg2://postgres.hvvzxwtydddbnqzuefvx:3956Medisa%@aws-0-ap-south-1.pooler.supabase.com:6543/postgres")

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = result.all()
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]
    


  
  
  
  
