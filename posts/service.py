import requests


class service:
    def __init__(self,root_url):
        if root_url[-1]=='/':
            self.root = root_url[:-1]
            print(self.root)
        self.root= root_url

    def get(self,*args):
        self.url = self.root+'/'
        for arg in args:
            self.url +=arg
            self.url+='/'
        #self.url = self.url[:-1]
        print('--------------------------------'+self.url)
        response = requests.get(self.url)
        if response.status_code ==200 :
            print(response.json())
            return response.json()

        else :
            return 404

        




