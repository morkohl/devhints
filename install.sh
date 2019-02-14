#!/usr/bin/env bash

PROGRAM_NAME="devhints"
INSTALL_PATH=$HOME/.${PROGRAM_NAME}

install_program () {
    mkdir -p ${INSTALL_PATH}/bin && cp -r ./bin/* ${INSTALL_PATH}/bin
    mkdir -p ${INSTALL_PATH}/data && echo "{}" > ${INSTALL_PATH}/data/hints.json

    chmod u+x ${INSTALL_PATH}/bin/devhints

    echo "Installation finished. To execute devhints from anywhere add ${INSTALL_PATH/bin} to your path in your .bashrc"
}

if [[ -d ${INSTALL_PATH} ]]
then
    echo "Directory already exists. Reinstalling..."
    rm -rf ${INSTALL_PATH}
    install_program
else
    install_program
fi