#!/usr/bin/env bash

CURRENT_DIR=$(dirname ${0})

if [ "${1}" == 'dev' ]; then
  shift
  COMMAND="docker-compose -f docker-compose.yml -f docker-compose.dev.yml"
else
  COMMAND="docker-compose"
fi

if [ "${1}" == 'run' ]; then
  shift
  COMMAND="${COMMAND} run --rm"
fi

if [ "${1}" = 'test' ] ||
   [ "${1}" = 'migrate' ] ||
   [ "${1}" = 'makemigrations' ] ||
   [ "${1}" = 'showmigrations' ] ||
   [ "${1}" = 'makemessages' ] ||
   [ "${1}" = 'compilemessages' ]; then
  COMMAND="${COMMAND} server python manage.py ${1}"
  shift
fi

${COMMAND} ${@}
