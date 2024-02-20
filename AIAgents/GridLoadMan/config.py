# config.py

# Copyright (C) Upperbay Systems, LLC - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Dave Hardin <dave@upperbay.com>, 2023

import logbook

agent_name = "GridLoadMan-1-0-0"
# MQTT Broker settings. USE IP or "localhost".
MQTT_BROKER = "192.168.0.131"
MQTT_PORT = 1883
mqtt_base_topic = "openai/assistant/"
mqtt_base_topic_c2agent = "C2Agent"

MQTT_TOPIC_TOASSISTANT = mqtt_base_topic + agent_name + "/ToAssistant"
MQTT_TOPIC_TOCLIENT = mqtt_base_topic + agent_name + "/ToClient"
#
MQTT_TOPIC_COMMAND = mqtt_base_topic + agent_name + "/CommandCenter"
MQTT_TOPIC_CONTROL = mqtt_base_topic + agent_name + "/ControlPanel"
MQTT_TOPIC_ALARM = mqtt_base_topic + agent_name + "/AlarmPanel"
MQTT_TOPIC_NOTICE = mqtt_base_topic + agent_name + "/NoticePanel"
MQTT_TOPIC_ALERT = mqtt_base_topic + agent_name + "/AlertPanel"
MQTT_TOPIC_C2AGENT = mqtt_base_topic_c2agent
#
MQTT_TOPIC_DATAFEED = mqtt_base_topic + agent_name + "/DataFeed"
# Logger level
logging_level = logbook.DEBUG

class GridPeakDetected:
    def __init__ (self, type_name, agent_name, message, start_date_time, duration_mins, peak_lmp, grid_node):
        self.type_name = type_name
        self.agent_name = agent_name
        self.message = message
        self.start_date_time = start_date_time
        self.duration_mins = duration_mins
        self.peak_lmp = peak_lmp
        self.grid_node = grid_node