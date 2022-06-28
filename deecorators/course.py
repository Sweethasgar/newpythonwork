class course:
    course_name=str
    active_status:bool

    def add_course(self,**kwargs):
      self.course_name=kwargs.get("course_name")
      self.active_status=kwargs.get("active_status")

    def __str__(self):
         return self.course_name





class Batch:
    course:course
    batch_code:str
    start_date:str


    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code





class student:

    st_name:str
    gender:str
    roll:int
    batch:Batch
    def add_student(self,**kwargs):
        self.st_name=kwargs.get("st_name")
        self.gender=kwargs.get("gender")
        self.roll=kwargs.get("roll")
        self.batch=kwargs.get("batch")

    def __str__(self):
        return self.st_name




django=course()
django.add_course(course_name="django",active_status=True)

bigdat=course()
bigdat.add_course(course_name="bigdata",active_status=True)


may=Batch()
may.add_batch(course=django,batch_code="may22",start_date="22-06,22")

may1=Batch()
may1.add_batch(course=bigdat,batch_code="may24",start_date="24-06,22")



st_name=student()
st_name.add_student(st_name="rahul",gender="male",roll="24",batch=may)

st_name1=student()
st_name1.add_student(st_name="ahmed",gender="male",roll="24",batch=may1)

print(st_name1.batch.course.course_name)

