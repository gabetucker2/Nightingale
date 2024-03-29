# nightingale

<h1>LINKS</h1>

* Prior authorization form samples: https://eforms.com/prior-authorization/

* Lucidchart: https://lucid.app/lucidchart/db5649b2-73a5-4ec3-8603-e3525ddcdc9c/edit?invitationId=inv_70d50131-b608-4c73-a01c-7203b5cbd204&page=0_0#

<h1>TODO</h1>

* Make Acrobat capable of parsing generated PDFs
* Lookat autofilling online portal, find sample for it
* Use tts and llm to autofill explanations

<h1>SETUP AND USAGE TUTORIAL</h1>

<h2>Hello!  I am Tour Guide Gabe.  Buckle up for your tour!</h2>

<img src="images/tutorial1.png" width="200"/>

Open your terminal.

<img src="images/tutorial2.png" width="600"/>

In the image are these commands.  Feel free to copy + paste into your terminal (press enter to run a command):

```
cd C:\Users\gabe\OneDrive\Desktop\
git clone https://github.com/gabetucker2/Nightingale
cd Nightingale
```

<img src="images/tutorial3.png" width="600"/>

<img src="images/tutorial4.png" width="600"/>

<h2>Ahh, a tiger!  Better go the other way!</h2>

<img src="images/tutorial1.png" width="200"/>

Open the folder you just created using your file explorer/finder.

<img src="images/tutorial5.png" width="600"/>

Edit the `parameters.py` file to your liking.
* outputName specifies the name of the pdf file created in the 'Nightingale/outputs' folder.
* priorAuthFormName specifies the name of the prior authorization form in the Nightingale/data/PriorAuthData folder.
* patientRow and prescriberRow specify the rows of the patient/prescriber in the Nightingale/data/PatientData and Nightingale/data/PrescriberData folders' spreadsheets.
* If consoleLogs is True, then your console will print data letting you know what's going on behind the scenes.  Otherwise, it will be all quiet.

<img src="images/tutorial6.png" width="600"/>

In the image is this command.  Feel free to copy + paste:

```
py model.py
```

Run this command (after making sure your terminal is in the correct folder by doing `cd path-to-Nightingale-folder`) beforehand) every time you want to create a new PDF file.

<img src="images/tutorial7.png" width="600"/>

Here is a photo of what all the interfaces you can interact with look like to make this process work.

<img src="images/tutorial8.png" width="1200"/>

<h2>I hope you enjoyed your tour!</h2>

<img src="images/tutorial1.png" width="200"/>
