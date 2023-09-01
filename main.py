from cmislib.model import CmisClient

class AlfrescoCmis:
    def __init__(self, url: str, user: str, password: str):
        self.url = url
        self.password = password
        self.user = user

    def list_repositories(self):
        try:
            print('Connecting...')
            client = CmisClient(self.url, self.user, self.password)
            print('Connected!')
            default = client.getDefaultRepository()
            print('default repository',default)
            repositories = client.getRepositories()
            print('Available Repositories:',repositories)
            for repo in repositories:
                print(f"Repository Name: {repo.getName()}")
                print(f"Repository ID: {repo.getRepositoryId()}")
                print(f"Repository Description: {repo.getDescription()}")
                print(f"Vendor Name: {repo.getVendorName()}")
                print(f"Product Name: {repo.getProductName()}")
                print(f"Product Version: {repo.getProductVersion()}")
                print("--------------------------------------------------")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    url = 'http://localhost:8080/alfresco/api/-default-/public/cmis/versions/1.1/atom'
    user = 'admin'
    password = 'sys123#'

    alfresco = AlfrescoCmis(url, user, password)
    alfresco.list_repositories()

