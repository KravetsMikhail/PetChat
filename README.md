# PetChat

## Программная документация

Используется **Sphinx**

ссылка: <https://www.sphinx-doc.org/en/master/index.html>

## Пакеты для инсталляции

1. Инициация проекта:

   ```bash
   pip install -U sphinx
   ```

   ```bash
   sphinx-quickstart
   ```

2. Установка темы:

   ```bash
   pip install sphinx-rtd-theme
   ```

3. Установка модуля переключения темы светлая/темная:

   ```bash
   pip install sphinx-rtd-dark-mode
   ```

4. Установка модуля добавления кнопки копирования в блоках кода:

   ```bash
   pip install sphinx-copybutton
   ```

5. Установка модуля отображения описания API

   ```bash
   pip install sphinxcontrib-httpdomain
   ```

   пример разметки:

   ```text
   .. http:post:: /posts/(int:post_id)

   Replies a comment to the post.

   :param post_id: post's unique id
   :type post_id: int
   :form email: author email address
   :form body: comment body
   :reqheader Accept: the response content type depends on
                      :mailheader:`Accept` header
   :reqheader Authorization: optional OAuth token to authenticate
   :resheader Content-Type: this depends on :mailheader:`Accept`
                            header of request
   :status 302: and then redirects to :http:get:`/posts/(int:post_id)`
   :status 400: when form parameters are missing

   .. http:get:: /posts/(int:post_id)

   Fetches the post

   (...)
   ```

6. Установка пакета конвертации в PDF

   ```bash
   pip install rst2pdf
   ```

7. Для построения диаграмм используется библиотека graphViz

   ссылка: <https://graphviz.org>

8. Установка модуля plantUML + Pillow (для поддержки параметра scale)

   ```bash
   pip install sphinxcontrib-plantuml
   pip install --upgrade Pillow
   ```

   ссылка: <https://github.com/sphinx-contrib/plantuml>

9. Установка модуля openAPI

   ```bash
   pip install sphinxcontrib-openapi
   ```

   ссылка: <https://github.com/sphinx-contrib/openapi>

10. Установка модуля reDoc

   ```bash   
   pip install setuptools

   pip install sphinxcontrib-redoc
   ```

   ссылка: <https://github.com/sphinx-contrib/redoc>


## Компиляция локально

Установка модуля

   ```bash
   pip install sphinx-autobuild
   ```

Запуск автокомпиляции

   ```bash
   cd project  
   sphinx-autobuild -a ./source ./build/html 
   ```

смотреть тут: <http://127.0.0.1:8000>

## Публикация на сервере "Read the Docs"

Для отображения диаграмм plantUML необходимо создать файл - scripts/pre_install.sh

   ```bash
   #!/bin/bash

   # Stop and exit on error
   set -euox pipefail

   # Check for required tools
   java -version
   dot -V

   # This folder is on PATH and does not require sudo
   # Download latest plantuml.jar from github
   curl -o ${READTHEDOCS_VIRTUALENV_PATH}/bin/plantuml.jar -L https://github.com/plantuml/plantuml/releases/download/v1.2024.3/plantuml-1.2024.3.jar
   # Create an executable script for plantuml
   printf '#!/bin/bash\nexec java -Djava.awt.headless=true -jar ${READTHEDOCS_VIRTUALENV_PATH}/bin/plantuml.jar "$@"' > ${READTHEDOCS_VIRTUALENV_PATH}/bin/plantuml
   chmod +x ${READTHEDOCS_VIRTUALENV_PATH}/bin/plantuml

   # Check plantuml version
   plantuml -version
   ```
В файл .readthedocs.yaml добавить секцию "jobs":

   ```yaml
   version: 2

   build:
   os: ubuntu-22.04
   tools:
      python: "3.12"

   apt_packages:
      - default-jre
      - graphviz

   jobs:
      pre_install:
         - bash ./scripts/pre_install.sh

   ```

ссылка на статью: https://stackoverflow.com/questions/77869766/how-do-i-specify-the-plantuml-version-with-readthedocs

