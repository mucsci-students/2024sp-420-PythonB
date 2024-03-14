no_venv= [ -z "$VIRTUAL_ENV" ];

env_name="venv"
if $no_venv; then
    read -p "No venv activated; insert name of existing or new venv: " env_name
    no_venv_path= [ ! -d "$VENV_PATH" ]
    if $no_venv_path; then
        python3 -m venv "$env_name"
    fi
fi

source "$PWD/$env_name/bin/activate"
pip install "$PWD"
clear
python3 uml.py
clear