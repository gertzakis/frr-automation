from jinja2 import Template
from jinja2.environment import load_extensions
from yaml import load
import yaml, sys


def get_config_data(yaml_file):
    with open(yaml_file) as file:
        config_data = yaml.load(file, Loader=yaml.FullLoader)
    return config_data


def load_template(template_file):
    """Loads Jinja2 template from file"""
    try:
        with open(template_file) as t:
            template = Template(t.read())
        return template
    except IOError as e:
        print(f"Template file '{ template_file }' could not be opened!")
        print(f"I/O error { e.errno } ({e.strerror})")
        sys.exit(1)


def render_config(hostname, config_data, template):
    """Renders configuration from Jinja2 template"""
    # logging.info(f"{ hostname }: rendering configuration...")

    ready_config = template.render(hostname=hostname, data=config_data)
    return ready_config

def main():
    yaml_data = get_config_data("data.yaml")

    for key, value in yaml_data["devices"].items():
        router_config = render_config(
            hostname=key, config_data=value, template=load_template("templates/frr_conf.j2")
        )
        with open(f"configs/{key}.cfg", "w") as config_file:
            config_file.write(router_config)

if __name__== "__main__":
    main()
