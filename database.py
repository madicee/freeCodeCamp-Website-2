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

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("insert into application job_id, full_name, email, linkedin_url, education, work_experience, resume_url) values (:jobs{{'job_id'}}, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, {"job_id" : job_id, "full_name": data["full_name"], "email": data["email"], "linkedin_url": data["linkedin_url"], "education": data["education"], "work_experience": data["work_experience"], "resume_url": data["resume_url"]})
  
  
