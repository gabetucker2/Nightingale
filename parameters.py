# imports
import os

# -------------------------------------------------------------------------------------------------
# static primary parameters

outputName = 'output1'
priorAuthFormName = 'Medicare'
patientRow = 3
prescriberRow = 5

consoleLogs = True

# -------------------------------------------------------------------------------------------------
# static peripheral parameters

priorAuthTermBlacklist = [
    'other',
    'undefined',
    'check-box',
    'checkbox',
    'explanation',
    'text'
]

# -------------------------------------------------------------------------------------------------
# hard match parameters

hardMatchPatientMedicare = {
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

hardMatchPrescriberMedicare = {
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

hardMatchPatientAnthem = {
    'planmedical-group-name': 'insurance-primary-name',
    'planmedical-group-phone': 'insurance-primary-phone-number',
    'planmedical-group-fax': 'insurance-primary-fax-number',
    'first-name': 'first-name',
    'first-name': 'first-name',
    'last-name': 'last-name',
    'mi': 'middle-initial',
    'phone-number': 'phone-number',
    'address': 'address',
    'city': 'city',
    'state': 'state',
    'zip-code': 'zip',
    'date-of-birth': 'dob',
    'height-incm': 'height',
    'weight-lbkg': 'weight',
    'allergies': 'drug-allergies',
    'patients-authorized-representative-if-applicable': 'authorized-representative-name',
    'authorized-representative-phone-number': 'authorized-representative-phone-number',
    'primary-insurance-name': 'insurance-primary-name',
    'patient-id-number': 'insurance-primary-id',
    'secondary-insurance-name': 'insurance-secondary-name',
    'patient-id-number2': 'insurance-secondary-id',
    'patient-name': 'full-name',
    'id': 'id',
}

hardMatchPrescriberAnthem = {
    'first-name2': 'first-name',
    'last-name2': 'last-name',
    'specialty': 'specialty',
    'address2': 'address',
    'city2': 'city',
    'state2': 'state',
    'zip-code2': 'zip',
    'requestor-if-different-than-prescriber': 'requestor',
    'office-contact-person': 'office-contact-person',
    'npi-number-individual': 'npi-number',
    'phone-number2': 'main-phone',
    'dea-number-if-required': 'dea-number',
    'fax-number-in-hipaa-compliant-area': 'office-fax-number',
    'email-address': 'email-address',
}

hardMatchMap = {
    'Medicare' : [hardMatchPatientMedicare, hardMatchPrescriberMedicare],
    'Anthem' : [hardMatchPatientAnthem, hardMatchPrescriberAnthem],
}

# -------------------------------------------------------------------------------------------------
# procedural parameters

projectPath = f'{os.getcwd()}\\'

priorAuthFolderPath = f'{projectPath}data\\PriorAuthData\\'
patientFolderPath = f'{projectPath}data\\PatientData\\'
prescriberFolderPath = f'{projectPath}data\\PrescriberData\\'
outputPath = f'{projectPath}outputs\\'

priorAuthInputPath = f"{priorAuthFolderPath}{priorAuthFormName}.pdf"
patientPath = f"{patientFolderPath}patients.csv"
prescriberPath = f"{prescriberFolderPath}prescribers.csv"

thisHardMatchMap = hardMatchMap[priorAuthFormName]
