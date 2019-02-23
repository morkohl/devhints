#!/usr/bin/env bash

PROGRAM_NAME="devhints"

INSTALL_PATH=$HOME/.${PROGRAM_NAME}
HINT_FILE=${INSTALL_PATH}/data/hints.json


install_program () {
    mkdir -p ${INSTALL_PATH}/bin && cp -r ./bin/* ${INSTALL_PATH}/bin
    mkdir -p ${INSTALL_PATH}/data && echo "{}" > ${HINT_FILE}

    chmod u+x ${INSTALL_PATH}/bin/devhints

    echo "Installation finished. To execute devhints from anywhere add ${INSTALL_PATH/bin} to your path in your .bashrc"
}

if [[ -d ${INSTALL_PATH} ]]
then
    echo "Directory already exists. Reinstalling..."

    if [[ "$1" == "--preserve-hint-file" ]] || [[ "$1" == "-p" ]]
    then
        TMP_HINT_FILE=/tmp/${PROGRAM_NAME}_hint_file.json

        echo "Preserved hint file is ${TMP_HINT_FILE}"

        cat ${HINT_FILE} > ${TMP_HINT_FILE}

        rm -rf ${INSTALL_PATH}

        install_program

        cat ${TMP_HINT_FILE} > ${HINT_FILE}
    else
        rm -rf ${INSTALL_PATH}

        install_program
    fi

else
    install_program
fi