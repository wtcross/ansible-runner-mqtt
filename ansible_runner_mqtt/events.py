import os
import logging
import json
import paho.mqtt.publish as mqtt_publish

logger = logging.getLogger('ansible-runner')


def publish(topic, data, **kwargs):
    logger.debug("publishing payload to topic '{}'".format(topic))
    payload = json.dumps(data)
    mqtt_publish.single(topic, payload, **kwargs)


def get_configuration(runner_config):
    def get_config_value(long_key):
        value = runner_config.settings.get(long_key, None)
        return os.getenv(long_key.upper(), value)

    keys = ['topic', 'payload', 'qos', 'retain', 'hostname', 'port',
            'client_id', 'keepalive', 'will', 'auth', 'tls', 'protocol',
            'transport']

    config = dict()
    for key in keys:
        long_key = 'mqtt_{}'.format(key)
        value = get_config_value(long_key)
        if value is not None:
            config[key] = value

    return config


def handler(runner_config, data):
    plugin_config = get_configuration(runner_config)
    topic = plugin_config.pop('topic', None)
    if topic is not None:
        publish(topic, data, **plugin_config)


def status_handler(runner_config, data):
    handler(runner_config, data)


def event_handler(runner_config, data):
    handler(runner_config, data)
