
A small Flask API for a Minecraft Tier Tagger.

The API can show Minecraft player profiles, rankings, game modes, and icon URLs as JSON.

## Features

- Player profiles by UUID
- Player profiles by Minecraft username
- Player rankings
- Support for multiple Minecraft modes
- Mode icon URLs
- CORS support
- Easy player management inside `flask_app.py`

## Requirements

Before installing the project, make sure you have:

- Python 3.10 or newer
- Flask
- The `flask_app.py` file
- A folder called `static`

The `static` folder should contain these icon files:

```text
vanilla.png
sword.png
uhc.png
smp.png
axe.png
mace.png
nethop.png
diapot.png
```

Your project should look like this:

```text
minecraft-tier-tagger/
├── flask_app.py
├── README.md
├── LICENSE
├── requirements.txt
└── static/
    ├── vanilla.png
    ├── sword.png
    ├── uhc.png
    ├── smp.png
    ├── axe.png
    ├── mace.png
    ├── nethop.png
    └── diapot.png
```

## Installation

### 1. Download the project

Download the project from GitHub.

You can also clone it with Git:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Then enter the project folder:

```bash
cd YOUR_PROJECT_FOLDER
```

Replace `YOUR_PROJECT_FOLDER` with the real name of your project folder.

### 2. Install Flask

Open a terminal inside the project folder.

Run this command:

```bash
pip install flask
```

If that does not work, try:

```bash
python -m pip install flask
```

### 3. Start the API

Start the Flask server with:

```bash
python flask_app.py
```

If your computer uses `python3`, use:

```bash
python3 flask_app.py
```

The API will normally run at:

```text
http://localhost:5000
```

Keep the terminal open while the API is running.

### 4. Stop the API

To stop the API, go to the terminal and press:

```text
CTRL + C
```

## Adding Players

Adding a player is easy.

You only need to edit the `PLAYERS` section in `flask_app.py`.

### Step 1: Open `flask_app.py`

Open the file called:

```text
flask_app.py
```

### Step 2: Find `PLAYERS`

Near the top of the file, find this section:

```python
PLAYERS = {
}
```

This is the place where you add players.

### Step 3: Copy this example

Copy this code:

```python
"1234567890abcdef1234567890abcdef": {
    "name": "MinecraftName",
    "rankings": {
        "sword": {
            "tier": 3,
            "pos": 0,
            "display": "HT3 §9Sword"
        }
    }
},
```

Paste it inside the `PLAYERS` section.

### Step 4: Change the player information

Change these values:

```text
1234567890abcdef1234567890abcdef
```

Replace this with the player's Minecraft UUID.

The UUID must not contain dashes.

Example:

```text
Correct:
1234567890abcdef1234567890abcdef

Incorrect:
12345678-90ab-cdef-1234-567890abcdef
```

Change this:

```text
MinecraftName
```

to the player's Minecraft username.

Change this:

```text
sword
```

to the game mode.

Change this:

```text
tier: 3
```

to the player's tier.

Change this:

```text
pos: 0
```

to the correct position:

- `0` means High Tier
- `1` means Low Tier

Change this:

```text
display: "HT3 §9Sword"
```

to the text that should be displayed by the Tier Tagger.

## Player Example

Here is a complete example:

```python
PLAYERS = {
    "1234567890abcdef1234567890abcdef": {
        "name": "Steve",
        "rankings": {
            "sword": {
                "tier": 2,
                "pos": 0,
                "display": "HT2 §9Sword"
            },
            "uhc": {
                "tier": 3,
                "pos": 1,
                "display": "LT3 §6UHC"
            }
        }
    }
}
```

This player has:

```text
Sword: HT2
UHC: LT3
```

## Adding More Than One Player

To add another player, add a comma after the first player.

Example:

```python
PLAYERS = {
    "firstplayeruuid": {
        "name": "Steve",
        "rankings": {
            "sword": {
                "tier": 2,
                "pos": 0,
                "display": "HT2 §9Sword"
            }
        }
    },

    "secondplayeruuid": {
        "name": "Alex",
        "rankings": {
            "axe": {
                "tier": 1,
                "pos": 1,
                "display": "LT1 §bAxe"
            }
        }
    }
}
```

Remember:

- Every player needs a unique UUID.
- Every player needs a name.
- Use a comma between players.
- Do not add a comma after the last player.

## Available Modes

These modes are currently supported:

```text
vanilla
sword
uhc
smp
axe
mace
nethop
diapot
```

Example:

```python
"mace": {
    "tier": 3,
    "pos": 0,
    "display": "HT3 §5Mace"
}
```

## Ranking Information

The ranking has three important values:

```python
{
    "tier": 3,
    "pos": 0,
    "display": "HT3 §9Sword"
}
```

### `tier`

The tier number of the player.

Examples:

```text
1 = Tier 1
2 = Tier 2
3 = Tier 3
4 = Tier 4
5 = No active tier
```

### `pos`

The position inside the tier.

```text
0 = High Tier
1 = Low Tier
```

### `display`

The text shown in the Tier Tagger.

Examples:

```text
HT1 §9Sword
LT2 §6UHC
HT3 §5Mace
```

## Hidden Rankings

Rankings with `tier: 5` are not shown.

Example:

```python
"axe": {
    "tier": 5,
    "pos": 0,
    "display": "No Tier"
}
```

Rankings that contain `No Tier` in the display text are also not shown.

## Important: Restart After Changes

After adding or changing a player:

1. Save `flask_app.py`.
2. Stop the running API with `CTRL + C`.
3. Start it again:

```bash
python flask_app.py
```

The changes will then be active.

## API Endpoints

### Get a player profile by UUID

```text
GET /v2/profile/<uuid>
```

Example:

```text
http://localhost:5000/v2/profile/1234567890abcdef1234567890abcdef
```

### Get only a player's rankings

```text
GET /v2/profile/<uuid>/rankings
```

Example:

```text
http://localhost:5000/v2/profile/1234567890abcdef1234567890abcdef/rankings
```

### Get a player by Minecraft name

```text
GET /v2/profile/by-name/<name>
```

Example:

```text
http://localhost:5000/v2/profile/by-name/Steve
```

### Get all available modes

```text
GET /v2/mode/list
```

Example:

```text
http://localhost:5000/v2/mode/list
```

## Testing the API

After starting the server, open your browser and visit:

```text
http://localhost:5000/v2/mode/list
```

You should see a JSON response containing the available modes.

To test a player profile, open:

```text
http://localhost:5000/v2/profile/PLAYER_UUID
```

Replace `PLAYER_UUID` with a UUID that you added to `PLAYERS`.

## Troubleshooting

### Flask is not installed

Run:

```bash
python -m pip install flask
```

### The server does not start

Make sure you are inside the correct project folder:

```bash
cd YOUR_PROJECT_FOLDER
```

Then run:

```bash
python flask_app.py
```

### The player is not found

Check the following:

- The UUID is correct.
- The UUID has no dashes.
- The username is spelled correctly.
- The player is inside the `PLAYERS` dictionary.
- The file was saved.
- The API was restarted.

### Icons do not load

Make sure:

- The folder is named exactly `static`.
- The image names are spelled correctly.
- The files are PNG files.
- The icon files are inside the `static` folder.

## Contact

If you find a bug or need help, you can contact me on Discord:

```text
doctoaxolotl-161
```