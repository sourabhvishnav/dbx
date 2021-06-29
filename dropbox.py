import dropbox


class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        f = open(fileFrom, 'rb')
        dbx.files_upload(f.read(), fileTo)


def main():
    access_token = 'A5vZeE72izYAAAAAAAAAAYw7sW_rPKrM4POJ91czYEKV6R5eByQxKe77-7dpE0dF'
    transferData = TransferData(access_token)
    fileFrom = input('Enter file path to transfer : ')
    fileTo = input('Enter the full path to upload to dropbox : ')
    transferData.uploadFile(fileFrom, fileTo)
    print('File has been moved')


main()
