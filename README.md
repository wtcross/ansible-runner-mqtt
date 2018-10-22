# ansible-runner-mqtt

This project is a plugin for [Ansible Runner](https://github.com/ansible/ansible-runner) that allows publishing Ansible status and event payloads to an MQTT topic. This allows systems subscribed to this MQTT topic to be notified when Ansible jobs are run and when key events occur.

For more details on `Runner` and the latest documentation see: https://ansible-runner.readthedocs.io/en/latest

## Installation
Simply ensure this plugin is installed on the same control host as `Runner`.

## Settings
This plugin can be configured in the `env/settings` file of your `Runner` directory hierarchy. All config items for this plugin are prefixed with `mqtt_` Here is an example:

```yaml
---
idle_timeout: 600
job_timeout: 3600
pexpect_timeout: 10
pexpect_use_poll: True
suppress_ansible_output: True

# MQTT plugin configuration
mqtt_topic: ansible
mqtt_host: my.mqtt.host
mqtt_qos: 2
```

If `mqtt_topic` is not set then the plugin is disabled. Everything else is optional and is passed through to the [`paho.mqtt.publish.single`](https://github.com/eclipse/paho.mqtt.python#single) function. Any of the keyword arguments that this function accepts can be prefixed with `mqtt_` and used as a setting in `env/settings`.

## License
[MIT License](LICENSE)
