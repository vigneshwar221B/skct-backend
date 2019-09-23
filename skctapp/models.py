from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    img = models.ImageField(upload_to="image")
    name = models.CharField(max_length=100)
    pos = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    pdf_file = models.FileField(null=True, default=None)

    def __str__(self):
        return f"{self.name}"


class SupportingFaculty(models.Model):
    img = models.ImageField(upload_to="image")
    name = models.CharField(max_length=100)
    pos = models.CharField(max_length=30, null=True)
    email = models.EmailField()
    pdf_file = models.FileField(null=True, default=None)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    name = models.TextField(null=True, blank=True)
    company_name = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Placement(models.Model):
    name = models.TextField(null=True, blank=True)
    year = models.TextField(null=True, blank=True)
    students = models.ManyToManyField(Student)
    def __str__(self):
        return f"{self.name}"


class Recuriters(models.Model):
    img = models.ImageField(upload_to="image")

    def __str__(self):
        return f"{self.img.url.split('/')[-1]}"


class Images(models.Model):
    image = models.ImageField(upload_to="image")
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.image.url.split('/')[-1]}"


class Lab(models.Model):
    name = models.CharField(max_length=50, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return f"{self.name}"



class Club(models.Model):
    club_name = models.CharField(max_length=50)
    club_details = models.TextField()
    club_photo = models.ImageField(upload_to="image")

    def __str__(self):
        return f"{self.club_name}"


class Academics(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return f"{self.name}"


class BestPratices(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return f"{self.name}"


class AssociationStudents(models.Model):
    name = models.TextField()
    class_name = models.TextField()
    designation = models.TextField()

    def __str__(self):
        return f"{self.name}"


class AssociationFacultys(models.Model):
    name = models.TextField()
    position = models.TextField()
    email = models.EmailField()
    phone_num = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}"


class AssociationImages(models.Model):
    img = models.ImageField()
    des = models.TextField()

    def __str__(self):
        return f"{self.des}"


class AssociationAchievements(models.Model):
    pdf = models.FileField()
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Association(models.Model):
    name = models.TextField()
    achievements = models.ManyToManyField(AssociationAchievements)
    images = models.ManyToManyField(AssociationImages)
    faculties = models.ManyToManyField(AssociationFacultys)
    students = models.ManyToManyField(AssociationStudents)

    def __str__(self):
        return f"{self.name}"





class Events(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="image", blank=True, null=True)
    date = models.DateTimeField(blank=True)
    description = models.TextField()
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    pdf_file = models.FileField(null=True, default=None)

    def __str__(self):
        return f"{self.name}"


class Announcement(models.Model):
    img = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.description


class UpcomingEvents(models.Model):
    img = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Hod(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to="image", null=True)
    phone_num = models.CharField(max_length=10)
    thought = models.TextField(null=True)

    def __str__(self):
        return f"{self.name}"


class Publications(models.Model):
    author_name = models.TextField(null=True)
    title = models.TextField(null=True)
    journals_name = models.TextField(null=True)
    issn_no = models.TextField(null=True)
    volume = models.TextField(null=True)
    year = models.TextField(null=True)
    publisher_name = models.TextField(null=True)
    scopes = models.TextField(null=True)

    def __str__(self):
        return f"{self.title}"

class Higherstudies(models.Model):
    name = models.TextField(null=True)
    batch = models.TextField(null=True)
    college = models.TextField(null=True)
    cource = models.TextField(null=True)
    

    def __str__(self):
        return f"{self.name}"        

class Proposals(models.Model):
    title = models.TextField(null=True)
    target_group = models.TextField(null=True)
    duration = models.TextField(null=True)
    amount = models.TextField(null=True)
    name = models.TextField(null=True)
    des = models.TextField(null=True)

    def __str__(self):
        return f"{self.title}"                

class Projectsponcered(models.Model):
    title = models.TextField(null=True)
    agency_name = models.TextField(null=True)
    investigator = models.TextField(null=True)
    amount = models.TextField(null=True)


    def __str__(self):
        return f"{self.title}"        


class Patents(models.Model):
    title = models.TextField(null=True)
    name = models.TextField(null=True)
    date_applied = models.TextField(null=True)
    status = models.TextField(null=True)
    no = models.TextField(null=True)

    def __str__(self):
        return f"{self.title}"


class Mous1(models.Model):
    industry = models.TextField(null=True)
    date = models.TextField(null=True)
    activity = models.TextField(null=True)

    def __str__(self):
        return f"{self.industry}"


class Disalumini(models.Model):
    name = models.TextField(null=True)
    batch = models.TextField(null=True)
    company = models.TextField(null=True)

    def __str__(self):
        return f"{self.name}"


class Phddetails(models.Model):
    name = models.TextField(null=True)
    area = models.TextField(null=True)
    status = models.TextField(null=True)

    def __str__(self):
        return f"{self.name}"
class Dlibrary(models.Model):
   
    description = models.TextField()
    image = models.ImageField(null=True)

class Department(models.Model):
    name = models.CharField(max_length=50, null=True)
    dname = models.CharField(max_length=50, null=True)
    beprograms = models.TextField(null=True)
    meprograms = models.TextField(null=True)
    certificate = models.CharField(max_length=100, null=True)
    dep_image = models.ImageField(upload_to="image", null=True)
    about = models.TextField(null=True)
    vision = models.TextField(null=True)
    mission = models.TextField(null=True)
    hod = models.OneToOneField(Hod, on_delete=models.CASCADE)
    academics = models.ManyToManyField(Academics)
    bp = models.ManyToManyField(BestPratices)
    facultys = models.ManyToManyField(Faculty)
    sfacultys = models.ManyToManyField(SupportingFaculty)
    labs = models.ManyToManyField(Lab)
    events = models.ManyToManyField(Events)
    club = models.ManyToManyField(Club)
    gallery = models.ManyToManyField(Images)
    publications = models.ManyToManyField(Publications)
    patents = models.ManyToManyField(Patents)
    mous1 = models.ManyToManyField(Mous1)
    placements = models.ManyToManyField(Placement)
    disalumini = models.ManyToManyField(Disalumini)
    phddetails = models.ManyToManyField(Phddetails)
    recuriters = models.ManyToManyField(Recuriters)
    associations = models.ManyToManyField(Association)
    higherstudies = models.ManyToManyField(Higherstudies)
    projectsponcered = models.ManyToManyField(Projectsponcered)
    proposals = models.ManyToManyField(Proposals)
    library=models.ManyToManyField(Dlibrary)

    def __str__(self):
        return f"{self.name}"


class Result(models.Model):
    name = models.TextField()
    url = models.URLField()

    def __str__(self):
        return f"{self.name}"


class TimeTable(models.Model):
    name = models.TextField()
    pdf = models.FileField()

    def __str__(self):
        return f"{self.name}"


class Calender(models.Model):
    name = models.TextField()
    pdf = models.FileField()

    def __str__(self):
        return f"{self.name}"


class Principal(models.Model):
    name = models.TextField()
    des = models.TextField()
    phone = models.TextField(max_length=10)
    pdf = models.FileField()
    img = models.ImageField()

    def __str__(self):
        return f"{self.name}"


class Main(models.Model):
    announcement = models.ManyToManyField(Announcement)
    events = models.ManyToManyField(Events)


class Admission(models.Model):
    name = models.TextField()
    pdf_file = models.FileField()

    def __str__(self):
        return f"{self.name}"


class SKCTDigest(models.Model):
    pass


class Facilities(models.Model):
    img = models.ImageField()
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Library(models.Model):
    staff_name = models.TextField()

    def __str__(self):
        return f"{self.staff_name}"


class LibraryImage(models.Model):
    img = models.ImageField()

    def __str__(self):
        return f"{self.img.url.split('/')[-1]}"


class CollegeGallery(models.Model):
    img = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return f"{self.description}"


class Form(models.Model):
    name = models.TextField()
    pdf = models.FileField()

    def __str__(self):
        return f"{self.name}"


class Nirf(models.Model):
    name = models.TextField()
    pdf = models.FileField()

    def __str__(self):
        return f"{self.name}"


class Downloads(models.Model):
    name = models.TextField()
    pdf = models.FileField()

    def __str__(self):
        return f"{self.name}"


class Brochure(models.Model):
    name = models.TextField()
    pdf = models.FileField()

    def __str__(self):
        return f"{self.name}"


class Reports(models.Model):
    name = models.TextField()
    pdf = models.FileField()

    def __str__(self):
        return f"{self.name}"
