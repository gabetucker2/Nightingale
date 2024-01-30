# imports

# -------------------------------------------------------------------------------------------------
# static primary parameters

consoleLogs = True


priorAuthFormName = 'Medicare'
patientName = 'patient1'
prescriberName = 'prescriber1'


priorAuthTermBlacklist = [
    'other',
    'undefined',
    'check-box',
    'checkbox',
    'explanation',
    'text'
]

hardMatchPatient = {
    'patient-name' : 'full-name',
    'address' : 'address',
    'city' : 'city',
    'state' : 'state',
    'zip' : 'zip',
    'member-id' : 'insurance-primary-id',
    'plan-name' : 'insurance-primary-plan',
    'home-phone' : 'phone-number',
    'sex-circle-m-f' : 'sex',
    'dob' : 'dob',
    'heightweight' : 'height-weight',
    'drug-allergies' : 'drug-allergies',
}

hardMatchPrescriber = {
    'address2' : 'address',
    'city2' : 'city',
    'state2' : 'state',
    'zip2' : 'zip',
    'fax' : 'office-fax-number',
    'prescriber-name' : 'full-name',
    'npi-if-available' : 'npi-number',
    'phone' : 'main-phone',
    'office-phone' : 'office-phone-number',
    'office-fax' : 'office-fax-number',
    'contact-person' : 'office-contact-person',
}

# -------------------------------------------------------------------------------------------------
# static peripheral parameters

priorAuthFolderPath = 'C:\\Users\\gabe\\OneDrive\\Desktop\\Nightingale\\data\\PriorAuthData\\'
patientFolderPath = 'C:\\Users\\gabe\\OneDrive\\Desktop\\Nightingale\\data\\PatientData\\'
prescriberFolderPath = 'C:\\Users\\gabe\\OneDrive\\Desktop\\Nightingale\\data\\PrescriberData\\'

outputPath = 'C:\\Users\\gabe\\OneDrive\\Desktop\\Nightingale\\outputs\\'

# -------------------------------------------------------------------------------------------------
# procedural parameters

priorAuthInputPath = f"{priorAuthFolderPath}{priorAuthFormName}.pdf"
patientPath = f"{patientFolderPath}{patientName}.csv"
prescriberPath = f"{prescriberFolderPath}{prescriberName}.csv"
