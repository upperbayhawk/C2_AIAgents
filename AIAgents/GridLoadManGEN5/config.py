# ==============================================================================
# Module: config.py
# Author: Dave Hardin, Upperbay Systems LLC
# Author URL: https://upperbay.com
# License: MIT
# Date: 1/2024
# Description: Agent configuration parameters
# Notes:
# ==============================================================================

import logbook

agent_name = "GridLoadMan-2-0-0"

# AI model and endpoint

# AI_MODEL = "gpt-4o"
# AI_KEY = "VOID"
# AI_URL = "VOID"
#
# AI_MODEL = "qwen/qwq-32b"
# AI_KEY = "VOID"
# #AI_URL = "http://192.168.0.131:1234/v1/"
# AI_URL = "http://192.168.0.198:1234/v1/"

# AI_MODEL = "gpt-4.5-preview"
# AI_KEY = "VOID"
# AI_URL = "VOID"

# AI_MODEL = "o3-mini"
# AI_KEY = "VOID"
# AI_URL = "VOID"
# #
# AI_MODEL = "o3-mini-high"
# AI_KEY = "VOID"
# AI_URL = "VOID"
#
# AI_MODEL = "o1"
# AI_KEY = "VOID"
# AI_URL = "VOID"

# AI_MODEL = "mistral-7b-instruct-v0.2"
# AI_KEY = "VOID"
# AI_URL = "http://192.168.0.198:1234/v1/"

# AI_MODEL = "qwen2.5-7b-instruct-1m"
# AI_KEY = "VOID"
# AI_URL = "http://127.0.0.1:1234/v1/"
#AI_URL = "http://192.168.0.198:1234/v1/"


# AI_MODEL = "llama3-empower-functions-small-v1.1"
# AI_KEY = "VOID"
# AI_URL = "http://192.168.0.198:1234/v1/"


AI_MODEL = "grok-2-latest"
AI_KEY = " "
AI_URL = "https://api.x.ai/v1"

# AI_MODEL = "deepseek-r1-distill-qwen-7b"
# AI_KEY = "VOID"
# AI_URL = "http://127.0.0.1:1234/v1/"

#AI_MODEL = "qwen2.5-3b-instruct:2"
#AI_KEY = "VOID"
#AI_URL = "http://127.0.0.1:1234/v1/"

#AI_MODEL = "llama-3.2-1b-instruct"
#AI_KEY = "VOID"
#AI_URL = "http://127.0.0.1:1234/v1/"

#AI_MODEL = "deepseek-chat"
#AI_KEY = "VOID"
#AI_URL = "https://api.deepseek.com/"

# MQTT Broker settings. USE IP or "localhost".
MQTT_BROKER = "192.168.0.111"
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
MQTT_TOPIC_OPCUA = "Site_Riverdale/ProcessCell_South/Unit2_Boiler"
# Logger level DEBUG, INFO
logging_level = logbook.DEBUG

ai_polling_interval = 1



class GridPeakDetected:
    def __init__ (self, type_name, agent_name, message, start_date_time, duration_mins, peak_lmp, grid_node,award_level,game_type):
        self.type_name = type_name
        self.agent_name = agent_name
        self.message = message
        self.start_date_time = start_date_time
        self.duration_mins = duration_mins
        self.peak_lmp = peak_lmp
        self.grid_node = grid_node
        self.award_level = award_level
        self.game_type = game_type