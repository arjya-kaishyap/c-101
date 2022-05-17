import dropbox 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'sl.BHwTuYYhHedMSbRhDztdnoMNSh80eMCezVvSqE_nDC-B_YSUNZzZc1YmWvDATAXb8QYhbJfbcn0nt4Z85W6TbFvODu-Rm2np24wfY7x-EtM1GpCFCKOoZtsVABXYvwmKgUrlK_4'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer :- ")
    file_to = input("Enter the full path to upload to dropbox :- ")
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()