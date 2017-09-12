# Script que atualiza todos os pacotes instalados através do pip.
#
# Obs: execute como administrador para atualizar pacotes que afetam todos
#      os usuários.

# Fonte: uma das respostas da questão abaixo do Stack Overflow
# https://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip

import pip
from subprocess import call

for dist in pip.get_installed_distributions():
    call("pip3 install --upgrade " + dist.project_name, shell=True)
