# Copyright 2018 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path

from kubernetes import client, config, utils


def create_from_file():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    k8s_client = client.ApiClient()
    utils.create_from_yaml(k8s_client, "nginx-deployment.yaml")
    k8s_api = client.ExtensionsV1beta1Api(k8s_client)
    deps = k8s_api.read_namespaced_deployment("nginx-deployment", "default")
    print("Deployment {0} created".format(deps.metadata.name))

    
def create_from_str():
    k8s_client = client.api_client.ApiClient(configuration=self.config)
    with open(self.path_prefix + "apps-deployment.yaml") as f:
        yml_obj = yaml.safe_load(f)

    yml_obj["metadata"]["name"] = "nginx-app-3"

    utils.create_from_dict(k8s_client, yml_obj)

    app_api = client.AppsV1beta1Api(k8s_client)
    dep = app_api.read_namespaced_deployment(name="nginx-app-3", namespace="default")
    
    # ---
    
    k8s_client = k8s_api_connect()
    yml_str = render_to_string('template.yaml', variables)
    yml_obj = yaml.safe_load(yml_str)
    kubernetes.utils.create_from_dict(k8s_client, yml_obj)


if __name__ == '__main__':
    create_from_file()
    create_from_str()
