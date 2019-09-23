from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import get_object_or_404
import smtplib
import threading
from .models import *
from django.urls import reverse
import socket


def send_mail(to, subject, text):
    # Gmail Sign In
    gmail_sender = 'vickylab2000@gmail.com'
    gmail_passwd = 'passwordai'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    body = '\r\n'.join(['To: %s' % to,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % subject,
                        '', text])

    try:
        server.sendmail(gmail_sender, [to], body)
        print('email sent')
    except:
        print('error sending mail')

    server.quit()


class HomeView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response({
            'name': dept.name,
            'dname': dept.dname,
            'certificate': dept.certificate,
            'image': dept.dep_image.url,
            'about': dept.about,
            'vision': dept.vision,
            'mission': dept.mission,
            'academiics': [{
                'name': academics.name,
                'details': academics.details
            }for academics in dept.academics.all()
            ],

            'best': [
                {
                    'name': bp.name,
                    'details': bp.details
                }
                for bp in dept.bp.all()]
        })


class BeprogramView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response({
            'beprogram': dept.beprograms,
            'dname': dept.dname,
        }
        )


class MeprogramView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response({
            'meprogram': dept.meprograms,
            'dname': dept.dname,
        }
        )


class FacultyView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response(

            [
                {
                    'name': faculty.name,
                    'image': faculty.img.url,
                    'pos': faculty.pos,
                    'email': faculty.email,
                    'file': faculty.pdf_file.url,

                }
                for faculty in dept.facultys.all()
            ]
        )


class LabView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response(
            [

                {'name': lab.name,
                 'description': lab.description,
                 'image': lab.image.url

                 }

                for lab in dept.labs.all()]
        )


class EventsView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response(
            [
                {
                    'pk': event.pk,
                    'name': event.name,
                    'image': event.image.url,
                    'date': event.date,
                    'description': event.description,
                    'contact': event.contact,
                    'email': event.email,

                }
                for event in dept.events.all()]
        )


class ClubView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'name': club.club_name,
                'details': club.club_details,
                'photo': club.club_photo.url

            }for club in dept.club.all()
        ])


class GalleryView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                "url": img.image.url,
                "tip": img.text
            }for img in dept.gallery.all()
        ])


class HodView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response({
            'name': dept.hod.name,
            'email': dept.hod.email,
            'image': dept.hod.image.url,
            'phone_num': dept.hod.phone_num,
            'thought': dept.hod.thought
        })


class MainView(APIView):
    def get(self, request):
        home = Main.objects.first()
        return Response({
            "announcement": [
                {
                    "img": an.img.url,
                    "description": an.description
                }for an in home.announcement.all()
            ],
            "events": [
                {
                    "name": event.name,
                    "img": event.image.url,
                    "date": event.date,
                    "description": event.description,
                }for event in home.events.all()
            ]
        })


class CoeView(APIView):
    pass


class ManagementView(APIView):
    pass


class AchievementView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response([
            {
                'name': file.name,
                'url': file.file_name.url

            } for file in dept.achievements.all()]

        )


class EventsDetailView(APIView):
    def get(self, request, pk):
        event = Events.objects.get(pk=pk)
        return Response({
            'pk': event.pk,
            'name': event.name,
            'image': event.image.url,
            'date': event.date,
            'description': event.description,
            'contact': event.contact,
            'email': event.email,
            'file': event.pdf_file.url,
        })


class PublicationView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'author': pub.author_name,
                'title': pub.title,
                'journals': pub.journals_name,
                'issn_no': pub.issn_no,
                'volume': pub.volume,
                'year': pub.year,
                'publisher': pub.publisher_name,
                'dcopes': pub.scopes

            }

            for pub in dept.publications.all()])


class ProposalsView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'title': pro.title,
                'target_group': pro.target_group,
                'duration': pro.duration,
                'amount': pro.amount,
                'name': pro.name,
                'des': pro.des,
            }

            for pro in dept.proposals.all()])


class PatentsView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'title': pat.title,
                'name': pat.name,
                'date': pat.date_applied,
                'status': pat.status,
                'no': pat.no
            }

            for pat in dept.patents.all()])


class Mous1View(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'industry': mou1.industry,
                'date': mou1.date,
                'activity': mou1.activity,
            }

            for mou1 in dept.mous1.all()])


class HigherstudiesView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'name': hs.name,
                'batch': hs.batch,
                'cource': hs.cource,
                'college': hs.college
            }

            for hs in dept.higherstudies.all()])



class ProjectsponceredView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'title': ps.title,
                'agency': ps.agency_name,
                'person': ps.investigator,
                'amount': ps.amount
            }

            for ps in dept.projectsponcered.all()])


class DisaluminiView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'name': ds.name,
                'batch': ds.batch,
                'company': ds.company,
            }

            for ds in dept.disalumini.all()])


class PhddetailsView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)

        return Response([
            {
                'name': phd.name,
                'area': phd.area,
                'status': phd.status,
            }

            for phd in dept.phddetails.all()])

class DlibraryView(APIView):
    def get(self,request,name):
        dept=get_object_or_404(Department,name=name)
        return Response([{
            'desc':lib.description,
            'img':lib.image.url
        } for lib in dept.library.all()])

        

class SupportingFacultyView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response([
            {
                'name': faculty.name,
                'image': faculty.img.url,
                'pos': faculty.pos,
                'email': faculty.email,
                'file': faculty.pdf_file.url,

            }

            for faculty in dept.sfacultys.all()])


class ResultsView(APIView):
    def get(self, request):
        return Response(
            [{
                "name": result.name,
                "url": result.url
            }for result in Result.objects.all()]
        )


class TimeTableView(APIView):
    def get(self, request):
        return Response([
            {
                "name": tt.name,
                "pdf": tt.pdf.url
            }for tt in TimeTable.objects.all()
        ])


class CalenderView(APIView):
    def get(self, request):
        return Response([
            {
                "name": cal.name,
                "pdf": cal.pdf.name
            }
            for cal in Calender.objects.all()])


class PrincipalView(APIView):
    def get(self, request):
        pr = Principal.objects.first()
        return Response({
            "img": pr.img.url,
            "name": pr.name,
            "des": pr.des,
            "phone": pr.phone,
            "pdf": pr.pdf.url
        })


class PlacementView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response({
            "ufuir3": [{
                "year": plac.year,
                "students": [{
                    "name": student.name,
                    "comp": student.company_name
                }for student in plac.students.all()]
            }for plac in dept.placements.all()],
            "rec": [rec.img.url for rec in dept.recuriters.all()]
        })


class AdmissionView(APIView):
    def get(self, request):
        return Response([
            {
                'name': admission.name,
                'file': admission.pdf_file.url,
            }
            for admission in Admission.objects.all()])


class FacilitesView(APIView):
    def get(self, request):
        return Response([
            {
                'img': facility.img.url,
                'title': facility.title,
                'description': facility.description
            }
            for facility in Facilities.objects.all()])


class LibraryView(APIView):
    def get(self, request):
        return Response({
            "name": [
                {
                    'faculty_name': lib.staff_name
                }
                for lib in Library.objects.all()],
            "img": [img.img.url for img in LibraryImage.objects.all()]

        })


class CollegeGalleryView(APIView):
    def get(self, request):
        return Response([
            {
                'img': item.img.url,
                'description': item.description
            }
            for item in CollegeGallery.objects.all()])


class FormView(APIView):
    def get(self, request):
        return Response([
            {
                'name': item.name,
                'pdf': item.pdf.url
            }
            for item in Form.objects.all()])


class NirfView(APIView):
    def get(self, request):
        return Response([
            {
                'name': item.name,
                'pdf': item.pdf.url
            }
            for item in Nirf.objects.all()])


class DownloadsView(APIView):
    def get(self, request):
        return Response([
            {
                'name': item.name,
                'pdf': item.pdf.url
            }
            for item in Downloads.objects.all()])


class FooterView(APIView):
    def get(self, request):
        return Response(
            {
                'brochures': [

                    {
                        'name': item.name,
                        'pdf': item.pdf.url
                    }
                    for item in Brochure.objects.all()],
                'downloads': [
                    {
                        'name': item.name,
                        'pdf': item.pdf.url
                    }
                    for item in Downloads.objects.all()],

                'reports': [
                    {
                        'name': item.name,
                        'pdf': item.pdf.url
                    }
                    for item in Reports.objects.all()]
            })


class AssociationView(APIView):
    def get(self, request, name):
        dept = get_object_or_404(Department, name=name)
        return Response([{
            'name': association.name,
            "images": [
                {
                    'img': img.img.url,
                    'des': img.des
                }
                for img in association.images.all()],
            "facultys": [
                {
                    'name': fac.name,
                    'position': fac.position,
                    'email': fac.email,
                    'phone_num': fac.phone_num
                }
                for fac in association.faculties.all()],
            "students": [
                {
                    'name': student.name,
                    'class': student.class_name,
                    'designation': student.designation

                }
                for student in association.students.all()],
            "achievements": [
                {
                    'name': achievement.name,
                    'pdf': achievement.pdf.url
                }
                for achievement in association.achievements.all()]


        } for association in dept.associations.all()])
