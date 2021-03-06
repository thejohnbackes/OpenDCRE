============
Introduction
============

OpenDCRE provides a securable RESTful API for monitoring and control of data center and IT equipment - via power line communications (PLC) over a DC bus bar, or via IPMI over LAN. The OpenDCRE API is easy to integrate into third-party monitoring, management and orchestration providers, while providing a simple, ``curl``-able interface for common and custom devops tasks.

Features
--------

- Simple ``curl``-able RESTful API
- Analog and digital sensor support (temperature, thermistor, humidity, fan speed, pressure).
- Power control and status, including power consumption and power supply status.
- Asset information for servers.
- Physical and chassis location awareness.
- Fan speed control and status.
- Chassis "identify" LED control and status.
- System boot target selection (hdd, pxe).
- Securable via TLS/SSL.
- Integration with existing Auth providers (OAuth, LDAP, AD, etc.).
- IPMI Bridge - all OpenDCRE commands can use IPMI 2.0 over LAN as transport layer.
- Redfish support (future) - all OpenDCRE commands can use Redfish over LAN as transport layer.

Architecture
------------

OpenDCRE is part of the OpenMistOS Linux distribution that runs on the Raspberry Pi 2 Model B (Raspberry Pi 3 support coming soon).  OpenMistOS includes a custom Docker package (v1.10.1), compiled for ARMv7 (armhf), and OpenDCRE is packaged as a Docker container.

OpenDCRE exposes a RESTful API via an HTTP endpoint in the OpenDCRE container.  The HTTP endpoint is comprised of nginx as the front-end, with uwsgi as a reverse proxy for a Python Flask application.  Within Flask, OpenDCRE uses a byte-level serial protocol to communicate with the OpenDCRE device bus, which is the primary communications channel between API users and the device bus.

.. image:: images/OpenDCRE_diagram01.png
    :align: center

The OpenDCRE device bus is comprised of a set of boards and devices, individually addressable, and globally scannable for a real-time inventory of addressable devices attached to the bus.  The OpenDCRE device bus allows devices to be read and written, and for various actions to be carried out, such as power control (on/off/cycle/status).  Additionally, when a physical OpenDCRE device bus is not present, a software emulator can be used to simulate OpenDCRE API commands and functionality, or the included IPMI2.0 bridge may be used for IPMI communications.

All included components of OpenDCRE can be customized, integrated and secured via configuration file (nginx, uwsgi), and output their logs to a common location (/var/log/opendcre).

Applications
------------

OpenMistOS and OpenDCRE can be used as an open platform for monitoring and managing data center hardware, software and environmental characteristics. Given the small form-factor of the Raspberry Pi plus its HAT board, there are a wide variety of possible applications, deployments, physical mounting strategies, and network connectivity options.  Community support helps OpenDCRE grow, and enables new functionality.

OpenMistOS
----------

OpenMistOS (OMOS) is an open-source operating system distribution for the Raspberry Pi, featuring OpenDCRE, the Open Data Center Runtime Environment.  OMOS was developed for the purpose of using a small, single-board computer like the Raspberry Pi to perform data center sensorfication and control, particularly in concert with, but not limited to, OpenCompute-based open hardware.

OMOS v1.1.0 is Debian (jessie)-based, featuring Docker capabilities baked into the OS, with OpenDCRE running as a Dockerized service of the OS.  OpenMistOS was developed by a team with decades of experience in data centers large and small, and is working to take the pain out of proprietary and arcane technologies.
