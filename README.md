For deployment guide with screenshot, please refer to following word document. Please download and open it. 

https://github.com/BurgahJasper/LSDManagement/blob/main/ApplicationInstallationGuide.docx

Otherwise proceed with this README file contentt for steps without Screenshots.

-----------------------
Deployment Guide:
-----------------------

Download the installable file ( WordPress eXtended RSS file also call WXR file ) from following location
[https://github.com/BurgahJasper/LSDManagement/tree/main/installable](https://github.com/BurgahJasper/LSDManagement/blob/main/installable/coolerlsdmfakenews.2023-04-30.xml)

You need to have access to WordPress. 

Approach 1 is to have wordpress running in your EC2 instance and then install this application. 
****Approach 1 needed to have wordpress installed with all packages 
in ec2 instance and guide is available in this link. https://github.com/BurgahJasper/LSDManagement/blob/main/EC2_WordpressInstalation_Readme.txt


Approach 2 is - create a user in wordpress.com and install the application there (paid domain is needed to run dynamic application). 



-----------------------------------------------------------------------------------------
Approach 1
(Installing the application in EC2 instance running wordpress and maria DB )
-----------------------------------------------------------------------------------------
Step 1: Go to WordPress admin home page.
 
Step2: Have the installable extract (WordPress eXtended RSS or WXR) file coolerlsdmfakenews.2023-04-30.xml handy.

Step3: Click Tools --> Import
 

Step4: Click Install Now click near WordPress option.

 

Step5: You will get “Importer Installed Successfully”
 

Step7:  Click on Run Importer


Step8: You will get option to import WXR file ( .xml format)
 

Step9: Click Choose File and once dialog box opens, select the provided WXR file coolerlsdmfakenews.2023-04-30.xml
 

Step10: Click “Upload file and Import”
Step11: Select existing User or create a new and check the check box Download and import attachments, and click submit. It will deploy the application

 



----------------------------------------------------------------------------------------

**Approach 2: Install/Deploy the application in wordpress.com.**

----------------------------------------------------------------------------------------

Step1: Login to your wordpress account in wordpress dotcom and go to dashboard home page. 
 
Step2 : Go to Tools --> Import and click
 
Step3: Select WordPress option, Drag and drop the WXR file (coolerlsdmfakenews.2023-04-30.xml) and Click on Start Import once provided that option. 

Step4: Click on Start Import
 
Step 5: Once imported (Deployed) Successfully, View Site option will be provided. 
 
Step6: Click on view site to get Visit Site option at top right corner. 
 
Step7: Click on it to get Launch Site option
 
Step7: Select the paid domain to get the site up and running in proper form as it is a dynamic site.  

 
