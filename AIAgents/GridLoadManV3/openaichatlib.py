# ==============================================================================
# Module: openailib.py
# Author: Dave Hardin, Upperbay Systems LLC
# Author URL: https://upperbay.com
# License: MIT
# Date: 1/2024
# Description: Library to handle communications to the OpenAI Assistant
# Notes: https://platform.openai.com/docs/api-reference?lang=python
# ==============================================================================

import logbook
import json
import time

import openai

import config
from xfunctionlib import XFunction

class OpenAIChatLib:
   
    def __init__(self):
        self.is_initialized = False
        self.model = "gpt-4o"
        #self.model = "o1"
        self.SEPARATOR = "======================="
        self.functions = [
            {
            "name": "sendAlarmSignalToNetworkNode",
            "description": "Send an alarm signal to a destination network node.",
            "parameters": {
                "type": "object",
                "properties": {
                "network_node": {"type": "string", "description": "The name of a node on the network. Network node names include AlarmPanel, ControlPanel, NoticePanel, AlertPanel, CommandCenter."},
                "message": {"type": "string", "description": "The contents of the alarm signal message."},
                },
                "required": ["network_node", "message"]
            }
        }, 
        {
            "name": "sendControlSignalToNetworkNode",
            "description": "Send a control signal to a destination network node.",
            "parameters": {
                "type": "object",
                "properties": {
                "network_node": {"type": "string", "description": "The name of a node on the network. Network node names include AlarmPanel, ControlPanel, NoticePanel, AlertPanel, CommandCenter."},
                "message": {"type": "string", "description": "The contents of the control signal message."},
                },
                "required": ["network_node", "message"]
            }
        },
        {
            "name": "sendNoticeSignalToNetworkNode",
            "description": "Send a notice signal to a destination network node.",
            "parameters": {
                "type": "object",
                "properties": {
                "network_node": {"type": "string", "description": "The name of a node on the network. Network node names include AlarmPanel, ControlPanel, NoticePanel, AlertPanel, CommandCenter."},
                "message": {"type": "string", "description": "The contents of the notice signal message."},
                },
                "required": ["network_node", "message"]
            }
        },
        {
            "name": "sendCommandSignalToNetworkNode",
            "description": "Send a command signal to a destination network node.",
            "parameters": {
                "type": "object",
                "properties": {
                "network_node": {"type": "string", "description": "The name of a node on the network. Network node names include AlarmPanel, ControlPanel, NoticePanel, AlertPanel, CommandCenter."},
                "message": {"type": "string", "description": "The contents of the command signal message."},
                },
                "required": ["network_node", "message"]
            }
        },
        {
            "name": "sendAlertSignalToNetworkNode",
            "description": "Send an alert signal to a destination network node.",
            "parameters": {
                "type": "object",
                "properties": {
                "network_node": {"type": "string", "description": "The name of a node on the network. Network node names include AlarmPanel, ControlPanel, NoticePanel, AlertPanel, CommandCenter."},
                "message": {"type": "string", "description": "The contents of the alert signal message."},
                },
                "required": ["network_node", "message"]
            }
        },
        {
            "name": "getNickname",
            "description": "Get the nickname of a city",
            "parameters": {
                "type": "object",
                "properties": {
                "location": {"type": "string", "description": "The city and state e.g. San Francisco, CA"},
                },
                "required": ["location"]
            }
        },
        {
            "name": "getMagicNumber",
            "description": "This number is magical.",
            "parameters": {
                "type": "object",
                "properties": {
                "tagname": {"type": "string", "description": "The name of the magic number"},
                },
                "required": ["tagname"]
            }
        },
        {
            "name": "getSensorValuebyName",
            "description": "Get the value of a sensor by its name. The value is NOTFOUND if the sensor is not available",
            "parameters": {
                "type": "object",
                "properties": {
                "tagname": {"type": "string", "description": "The name of the sensor."},
                },
                "required": ["tagname"]
            }
        },
        {
            "name": "putSensorValuebyName",
            "description": "Put the value of a sensor into the cache using its name.",
            "parameters": {
                "type": "object",
                "properties": {
                "tagname": {"type": "string", "description": "The name of the sensor."},
                "value": {"type": "string", "description": "The value of the sensor."},
                },
                "required": ["tagname","value"]
            }
        },
        {
            "name": "sendGridPeakDetected",
            "description": "Send a grid peak detected to a destination network node.",
            "parameters": {
                "type": "object",
                "properties": {
                "network_node": {"type": "string", "description": "The name of a node on the network. Network node names include C2Agent, AlarmPanel, ControlPanel, NoticePanel, AlertPanel, CommandCenter."},
                "message": {"type": "string", "description": "The description of the peak detected."},
                "start_date_time": {"type": "string", "description": "The datetime of the peak detected."},
                "duration_mins": {"type": "string", "description": "The duration in minutes of the peak detected."},
                "peak_lmp": {"type": "string", "description": "The LMP for a megawatt-hour during the peak detected."},
                "grid_node": {"type": "string", "description": "The grid pricing node for the peak detected ."},
                "award_level": {"type": "string", "description": "The award level of the game. Values can be BRONZE, SILVER and GOLD"},
                "game_type": {"type": "string", "description": "The type of game that is being played. The values can be SHEDPOWER or HARVESTPOWER"},
                },
                "required": ["network_node", "message","start_date_time","duration_mins","peak_lmp","grid_node","award_level","game_type"]
            }
        },
        {
            "name": "getNickname3",
            "description": "Get the nickname of a city",
            "parameters": {
                "type": "object",
                "properties": {
                "location": {"type": "string", "description": "The city and state e.g. San Francisco, CA"},
                },
                "required": ["location"]
            }
        } 
    ]

    def run_functions (self,function_name,arguments):

        if function_name == "sendAlarmSignalToNetworkNode":
            try:
                my_args = json.loads(arguments)
                if "network_node" in my_args:
                    print("From Json location = " + my_args["network_node"])
                    network_node = my_args["network_node"]
                    message = my_args["message"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.sendAlarmSignalToNetworkNode(network_node,message)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value
                else:
                    self.log.error("network_node argument is missing: {e}:" + function_name)
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value
            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "sendControlSignalToNetworkNode":
            try:
                my_args = json.loads(arguments)
                if "network_node" in my_args:
                    print("From Json location = " + my_args["network_node"])
                    network_node = my_args["network_node"]
                    message = my_args["message"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.sendControlSignalToNetworkNode(network_node,message)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value
                else:
                    self.log.error("network_node argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value
            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "sendNoticeSignalToNetworkNode":
            try:
                my_args = json.loads(arguments)
                if "network_node" in my_args:
                    print("From Json location = " + my_args["network_node"])
                    network_node = my_args["network_node"]
                    message = my_args["message"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.sendNoticeSignalToNetworkNode(network_node,message)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value
                else:
                    self.log.error("network_node argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value

            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "sendCommandSignalToNetworkNode":
            try:
                my_args = json.loads(arguments)
                if "network_node" in my_args:
                    print("From Json location = " + my_args["network_node"])
                    network_node = my_args["network_node"]
                    message = my_args["message"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.sendCommandSignalToNetworkNode(network_node,message)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value

                else:
                    self.log.error("network_node argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value

            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "sendAlertSignalToNetworkNode":
            try:
                my_args = json.loads(arguments)
                if "network_node" in my_args:
                    print("From Json location = " + my_args["network_node"])
                    network_node = my_args["network_node"]
                    message = my_args["message"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.sendAlertSignalToNetworkNode(network_node,message)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value

                else:
                    self.log.error("network_node argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value

            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "getNickname":
            try:
                my_args = json.loads(arguments)
                if "location" in my_args:
                    print("From Json location = " + my_args["location"])
                    location = my_args["location"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.getNickname(location)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value

                else:
                    self.log.error("location argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value

            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "getMagicNumber":
            try:
                my_args = json.loads(arguments)
                if "tagname" in my_args:
                    print("From Json name = " + my_args["tagname"])
                    my_name = my_args["tagname"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.getMagicNumber(my_name)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1} " + function_name)
                    return return_value

                else:
                    self.log.error("tagname argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value
            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e} " + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "getSensorValuebyName":
            try:
                my_args = json.loads(arguments)
                if "tagname" in my_args:
                    print("From Json tagname = " + my_args["tagname"])
                    tagname = my_args["tagname"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.getSensorValuebyName(tagname)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value

                else:
                    self.log.error("location argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value
            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "putSensorValuebyName":
            try:
                my_args = json.loads(arguments)
                if "tagname" in my_args:
                    print("From Json tagname = " + my_args["tagname"])
                    tagname = my_args["tagname"]
                    tagvalue = my_args["value"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.putSensorValuebyName(tagname,tagvalue)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value

                else:
                    self.log.error("location argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value
            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////
        if function_name == "getNickname3":
            try:
                if "location" in my_args:
                    my_args = json.loads(arguments)
                    print("From Json location = " + my_args["location"])
                    location = my_args["location"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        return_value = xfunc.getNickname3(location)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value

                else:
                    self.log.error("location argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value
            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")

        if function_name == "sendGridPeakDetected":
            try:
                my_args = json.loads(arguments)
                if "network_node" in my_args:
                    print("From Json location = " + my_args["network_node"])
                    network_node = my_args["network_node"]
                    message = my_args["message"]
                    start_date_time = my_args["start_date_time"]
                    duration_mins = my_args["duration_mins"]
                    peak_lmp = my_args["peak_lmp"]
                    grid_node = my_args["grid_node"]
                    award_level = my_args["award_level"]
                    game_type = my_args["game_type"]
                    return_value = "ERROR"
                    try:
                        xfunc = XFunction()
                        print("Calling " + "sendGridPeakDetected")
                        return_value = xfunc.sendGridPeakDetected(network_node,message,start_date_time,duration_mins,peak_lmp,grid_node,award_level,game_type)
                        print("function: " + function_name + " = " + return_value)
                    except Exception as e1:
                        self.log.error("FUNCTION ERROR: {e1}: " + function_name)
                    return return_value

                else:
                    self.log.error("network_node argument is missing: {e}:" + function_name)    
                    return_value = "ERROR"
                    print("function: " + function_name + " = " + return_value)
                    return return_value

            except Exception as e:
                self.log.error("FUNCTION WRAPPER ERROR: {e}:" + function_name)
                return("WRAPPER ERROR")
        #////////////////////////////////////////////////////////

     
    def initialize(self,agent_name,agent_init_prompt_file,agent_init_instructions_file,agent_output_file):
        # Add initialization code

        self.log = logbook.Logger("openaichatlib", 0)
        self.log.debug("Initializing OpenAIChatLib...")

        self.agent_name = agent_name
        self.agent_init_prompt_file = agent_init_prompt_file
        self.agent_init_instructions_file = agent_init_instructions_file
        self.agent_output_file = agent_output_file

        with open(self.agent_output_file, "a", encoding="utf-8") as file:
            file.write("\n" + self.SEPARATOR + "\n\n")

        # Open the initialization file and read its contents
        with open(self.agent_init_prompt_file, 'r', encoding='utf-8') as init_file:
            self.init_file_contents = init_file.read()
        self.log.debug(self.init_file_contents)

        self.messages = [
            {"role": "user", "content": self.init_file_contents}
        ]

        # Open the instructions file and read its contents
        with open(self.agent_init_instructions_file, 'r', encoding='utf-8') as instruction_file:
            self.instruct__file_contents = instruction_file.read()

        self.messages.append({"role": "user", "content": self.instruct__file_contents})



    def run(self, input_message):
            #print("Running OpenChatAILib...")
            # Add code to execute AI-related tasks here
            #print ("processing")
            self.log.debug ("Input Message: " + input_message + "\n")
            self.last_message = "NULL"

            self.messages.append = ({"role": "user", "content": input_message})

            # 3) Call the ChatCompletion with the conversation and functions
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.messages,
                functions=self.functions
            )
            
            assistant_message = response["choices"][0]["message"]

            # 4) If there's a function call, handle it
            if assistant_message.get("function_call"):
                function_name = assistant_message["function_call"]["name"]
                arguments_str = assistant_message["function_call"]["arguments"]
                try:
                    args = json.loads(arguments_str)
                except json.JSONDecodeError:
                    # If there's an error decoding JSON, handle it gracefully
                    args = {}
                
                result = self.run_function(function_name, args)

                # Create a function role message with the result
                function_response_message = {
                    "role": "function",
                    "name": function_name,
                    "content": result
                }

                # Append the function call + response to the conversation
                self.messages.append(assistant_message)
                self.messages.append(function_response_message)

                # Make a follow-up call so GPT can finalize a user-facing answer
                followup_response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=self.messages
                )
                final_answer = followup_response["choices"][0]["message"]["content"]
                print(f"Assistant: {final_answer}")
                self.log.debug(f"Assistant: {final_answer}")
                self.messages.append({"role": "assistant", "content": final_answer})
                self.last_message = str(final_answer)
            else:
                # If the model didn't call a function, just print the content
                answer_text = assistant_message["content"]
                print(f"Assistant: {answer_text}")
                self.log.debug(f"Assistant: {answer_text}")
                self.messages.append({"role": "assistant", "content": answer_text})
                self.last_message = str(answer_text)

            with open(self.agent_output_file, "a", encoding="utf-8") as file:
                file.write(str(input_message + "\n"))
                file.write(str(self.last_message + "\n"))
           
            return("OK")

   

# Instantiate OpenAILib class to make it a singleton instance
#openaichatlib_instance = OpenAIChatLib()