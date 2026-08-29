import os
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

MODES = [
    "vanilla",
    "sword",
    "uhc",
    "smp",
    "axe",
    "mace",
    "nethop",
    "diapot",
]

ICON_MAP = {
    "vanilla": "vanilla.png",
    "sword": "sword.png",
    "uhc": "uhc.png",
    "smp": "smp.png",
    "axe": "axe.png",
    "mace": "mace.png",
    "nethop": "nethop.png",
    "diapot": "diapot.png",
}

PLAYERS = {
    # Add new players here.
    # Use UUIDs without dashes.
    #
    # "1234567890abcdef1234567890abcdef": {
    #     "name": "MinecraftName",
    #     "rankings": {
    #         "sword": {
    #             "tier": 3,
    #             "pos": 0,
    #             "display": "HT3 §9Sword"
    #         }
    #     }
    # }
}


def get_host():
    host = request.host_url.rstrip("/")

    if "replit.app" in host or "repl.co" in host or "pythonanywhere" in host:
        host = host.replace("http://", "https://")

    return host


def build_rankings(player_data, host):
    rankings = {}

    for mode in MODES:
        entry = player_data.get("rankings", {}).get(mode)

        if not entry:
            continue

        if entry.get("tier") == 5 or "No Tier" in entry.get("display", ""):
            continue

        ranking = dict(entry)
        icon_url = f"{host}/static/{ICON_MAP[mode]}"

        ranking["icon"] = icon_url
        ranking["icon_url"] = icon_url

        rankings[mode] = ranking

    return rankings


@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add(
        "Access-Control-Allow-Headers",
        "Content-Type, Authorization"
    )
    response.headers.add(
        "Access-Control-Allow-Methods",
        "GET, PUT, POST, DELETE, OPTIONS"
    )

    return response


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        path
    )


@app.route("/v2/profile/<uuid>")
def get_profile(uuid):
    normalized_uuid = uuid.replace("-", "").lower()
    player_data = PLAYERS.get(normalized_uuid)

    if not player_data:
        return jsonify({})

    rankings = build_rankings(player_data, get_host())

    if not rankings:
        return jsonify({})

    return jsonify({
        "uuid": uuid,
        "name": player_data.get("name", "Unknown"),
        "rankings": rankings,
    })


@app.route("/v2/profile/<uuid>/rankings")
def get_rankings(uuid):
    normalized_uuid = uuid.replace("-", "").lower()
    player_data = PLAYERS.get(normalized_uuid)

    if not player_data:
        return jsonify({})

    return jsonify(build_rankings(player_data, get_host()))


@app.route("/v2/profile/by-name/<query>")
def get_profile_by_name(query):
    for uuid, player_data in PLAYERS.items():
        if player_data.get("name", "").lower() != query.lower():
            continue

        rankings = build_rankings(player_data, get_host())

        if not rankings:
            return jsonify({
                "error": "Player has no active rankings"
            }), 404

        return jsonify({
            "uuid": uuid,
            "name": player_data.get("name"),
            "rankings": rankings,
        })

    return jsonify({
        "error": "Player not found"
    }), 404


@app.route("/v2/mode/list")
def list_modes():
    host = get_host()

    return jsonify({
        mode: {
            "title": mode.capitalize(),
            "short_name": mode,
            "icon_url": f"{host}/static/{ICON_MAP[mode]}",
        }
        for mode in MODES
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)