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

reinstall_program() {
    echo "Directory already exists. Reinstalling..."

    TMP_HINT_FILE=/tmp/${PROGRAM_NAME}_hint_file.json

    cat ${HINT_FILE} > ${TMP_HINT_FILE}

    rm -rf ${INSTALL_PATH}

    install_program

    cat ${TMP_HINT_FILE} > ${HINT_FILE}
}



if [[ -d ${INSTALL_PATH} ]]
then
    reinstall_program
else
    install_program
fi