#!/bin/bash

say() {
  msg="$@"
  if [ -t 1 ]; then
    printf "\033[1;34;49m%s\033[m\n" "$msg"
  else
    echo "$msg"
  fi
}

complain() {
  msg="$@"
  if [ -t 1 ]; then
    printf "\033[1;31;49m%s\033[m\n" "$msg"
  else
    echo "$msg"
  fi
}

run() {
  say "\$ $@"
  local rc=0
  "$@" || rc=$?
  if [ $rc -ne 0 ]; then
    complain "E: The command \"$@\" failed with status code $status, we cannot proceed."
    complain "I: If you have no idea of what went wrong, please feel free to ask for help in the Noosfero community. Check the contact information in the project website (http://noosfero.org/)."
    exit 1
  fi
}

quiet() {
  say "\$ $@"
  local tmpfile=$(mktemp)
  local rc=0
  "$@" > "$tmpfile" 2>&1 || rc=$?
  if [ $rc -ne 0 ]; then
    cat "$tmpfile"
  fi
  rm -f "$tmpfile"
  return $rc
}


say "Tested on python 2.7"

say "Installing dependencies"

run sudo python -m pip install --upgrade pip
run sudo pip install -r requirements.txt

say "Installed successfully"