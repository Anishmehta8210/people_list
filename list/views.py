from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from .forms import *
from webdriver_manager.chrome import ChromeDriverManager
import time
from .models import *

def download_pdf(request):    
    district = request.GET.get('district', '')
    
    district = VoterList.objects.get(district=district)    

    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    driver.get("https://ceoelection.maharashtra.gov.in/searchlist/")    
    
    district_select = driver.find_element_by_id("ddlDistrict")

    district_select.send_keys(district.name)
    open_pdf_button = driver.find_element_by_id("btnDownload")
    open_pdf_button.click()
    time.sleep(5) 
    driver.quit()    
    return HttpResponse("PDF file downloaded successfully.")