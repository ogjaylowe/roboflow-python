import requests
import json
from roboflow.core.project import Project
from roboflow.config import *

class Workspace():
    def __init__(self, info, api_key, default_workspace):
        workspace_info = info['workspace']
        self.name = workspace_info['name']
        self.project_list = workspace_info['projects']
        self.members = workspace_info['members']
        self.url = workspace_info['url']

        self.__api_key = api_key


    def list_projects(self):
        print(self.project_list)

    def projects(self):
        projects_array = []
        for a_project in self.project_list:
            proj = Project(self.__api_key, a_project)
            projects_array.append(proj)

        return projects_array


    def project(self, project_name):

        if "/" in project_name:
            raise RuntimeError("Do not re-specify the workspace {} in your project request".format(project_name.rsplit()[0]))

        dataset_info = requests.get(API_URL + "/" + self.url + "/" + project_name + "?api_key=" + self.__api_key)

        # Throw error if dataset isn't valid/user doesn't have permissions to access the dataset
        if dataset_info.status_code != 200:
            raise RuntimeError(dataset_info.text)

        dataset_info = dataset_info.json()['project']

        return Project(self.__api_key, dataset_info)

    def __str__(self):
        json_value = {'name': self.name,
                      'url': self.url,
                      'members': self.members,
                      'projects': self.projects
                      }

        return json.dumps(json_value, indent=2)

