import os_client_config

cloud = os_client_config.OpenStackConfig().get_one_cloud()

print(cloud.config)
