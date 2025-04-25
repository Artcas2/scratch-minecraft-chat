# scratch-livestats

Demo project: https://scratch.mit.edu/projects/1165634488

## Installation
Run the following command in your command prompt/shell to install the required packages :
```cmd
pip install -U scratchattach mcpq python-dotenv
```

Then download the python file [here](https://raw.githubusercontent.com/Artcas2/scratch-minecraft-chat/refs/heads/main/chat.py). Remix the demo project or download it [here](https://raw.githubusercontent.com/Artcas2/scratch-minecraft-chat/refs/heads/main/demo.sb3).

## Configuration
*You can get your session id from your browser's cookies. [More information](https://github.com/TimMcCool/scratchattach/wiki/Get-your-session-id)*

Create a file named `.env` in the same folder and enter the following:
```env
SESSION_ID="your_session_id"
USERNAME=your_username
PROJECT_ID=your_project_id
```

## Usage
On your Minecraft (Spigot, Paper, etc.) server, download and install the [mcpq-plugin](https://github.com/mcpq/mcpq-plugin/releases/latest) (.jar) plugin. Start your server, run the Python script, and you're good to go!
