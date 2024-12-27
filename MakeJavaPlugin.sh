#!/bin/bash

JDIR="./MyAdventures/java/"
PLUGINDIR="./Server/plugins"

# Compilar el Archivo del Plugin
javac -cp ${JDIR}spigot-1.12.jar ${JDIR}ChatListener.java -d ${JDIR}/ChatListener

# el archivo plugin.yml debe estar fuera de la carpeta ChatListener
jar cvf ${JDIR}/ChatListener.jar -C ${JDIR}/ChatListener/ . -C ${JDIR} plugin.yml

mv ${JDIR}/ChatListener.jar ${PLUGINDIR}
