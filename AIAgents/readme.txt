Project Omnibus
An OpenAI Agent Toolshed

Project Description

Python sample code, built on the OpenAI Beta Assistant API, to aid the integration of OpenAI LLMs (e.g. ChatGPT4) into applications using MQTT messaging.

MQTT is a light-weight, easy-to-use, publish-subscribe messaging bus widely used in internet of things (IoT) communications. It is multi-platform (e.g. Windows, Linux) and is supported by all major software languages. The site is https://mosquitto.org/ and downloads are available at https://mosquitto.org/download/.

WARNING: The OpenAI Assistant API and the OpenAI runtime environment is BETA and subject to change with intermittent downtime and slow response.

Repository
https://github.com/upperbayhawk/C2_AIAgents.git

Code Summary

The code is 100% Python 3.12 developed on Windows 11 with Microsoft VSCode.

The code consists of a folder with a set of console apps that perform different functions associated with a specific GPT-4 Assistant that resides in the OpenAI cloud.

The GPT-4 assistant is created by makeagent.py. Use https://platform.openai.com/assistants to verify creation. All agent behavior is in this file. See https://platform.openai.com/docs/overview. 

NOTE: Delete assistant using OpenAI API site.

The runserver.py is the primary local agent that communicates directly with the cloud assistant. It sends messages to the assistant and waits for responses. Other functions include:
	• Messages can be entered on the command line or received in an MQTT message.
	• Maintains a local cache of tag/data values that is refreshed from the runsource.py agent. The runsource.py agent collects whatever external data it desires and sends that data in JSON to the runserver.py agent via an MQTT message and is available through the function call-backs.
	• Provides call-back functions that GPT-4 can call whenever he/she/it desires. 

Agent libraries include:
	• Openailib.py
		○ Handles Assistant communications
	• Xfunctionlib.py
		○ Handles function call-backs
	• Xnetworklib.py
		○ Handles MQTT messaging
	• Xcachelib.py
		○ Handles runserver.py tag/value caching
	• Thingsspeaklib.py
		○ Handles access to thingspeak.com

Other agents are optional. They are:
	• runclient.py
		○ Sends prompts using MQTT to and from runserver.py
	• runsink.py
		○ Receives MQTT messages from GPT-4 function call-backs in runserver.py
	• runsource.py
		○ Sends JSON MQTT messages to runserver.py using tag/value. This data is available to GPT-4 using function call-backs
	• runpump.py
		○ Periodically sends fully-dressed prompt messages with both text and data to runserver.py

These console apps have a simple structure that extends the OpenAI Assistant API in a straight forward if not elegant way. No attempt has been made to create production code. The purpose of this code is to help experiment and explore the capabilities of GPT-4 and provide a means to integrate GPT4 with your own apps, regardless of where your apps are running.

Each console app creates threads to handle keyboard and MQTT message inputs. Incoming MQTT messages are pushed into queues and the main worker thread periodically scans and services the messages received. Other worker threads are spawned as needed. Most of the code is plumbing and can be changed to do whatever.

The runserver.py agent can only handle one prompt run at a time so interleaved prompts from multiple agents will result in bad behavior.

Readme.txt provides further information about the Python environment.

Use these apps to play around and learn about the API.

The following are personal play toys and can be disregarded:
	• GridLoadMan
	• HomePowerMan
	• ThingsSpeakMan
	• Weatherman

Usage

	• Git clone the repository to a local folder
		○ git clone https://github.com/upperbayhawk/C2_AIAgents.git
	• Obtain an openai key from your openai.com API account and set the OPENAI_API_KEY using powershell setx
	• Create a new agent by cloning and renaming the "OmniBus" directory
	• Modify makeagent.py to create the assistant with the characteristics desired
	• Run makeagent.py and confirm creation on openai API site
	• Modify runserver.py and prompt data to support the function call-backs. Change the MQTT hub IP address, MQTT  messages and functionality as desired.
	• Test using keyboard prompts
	• Run more agents as desired
	• Build custom agents
